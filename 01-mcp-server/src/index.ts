#!/usr/bin/env node

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  ListToolsRequestSchema,
  CallToolRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

// Import schemas
import {
  SUMMARIZE_SCHEMA,
  ANALYZE_SCHEMA,
  RISK_SCHEMA,
  NOTIFICATION_SCHEMA,
} from "./schemas/tool-schemas.js";

// Import tool implementations
import { summarizeContract } from "./tools/summarization.js";
import { analyzeContract } from "./tools/contract-analysis.js";
import { assessRisk } from "./tools/risk-assessment.js";
import { sendNotification } from "./tools/notifications.js";

// Create MCP server
const server = new Server(
  {
    name: "contract-analysis-mcp",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Handle tool listing
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "summarize_contract",
        description: "Summarize a contract document to key points and statistics",
        inputSchema: SUMMARIZE_SCHEMA,
      },
      {
        name: "analyze_contract",
        description: "Perform detailed analysis of contract clauses, terms, and identify warnings",
        inputSchema: ANALYZE_SCHEMA,
      },
      {
        name: "assess_risk",
        description: "Assess the risk level of a contract and provide recommendations",
        inputSchema: RISK_SCHEMA,
      },
      {
        name: "send_notification",
        description: "Send a notification to stakeholders about contract findings",
        inputSchema: NOTIFICATION_SCHEMA,
      },
    ],
  };
});

// Handle tool execution
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    let result: string;

    switch (name) {
      case "summarize_contract": {
        const text = args?.text as string;
        const maxLength = (args?.max_length as number) || 100;

        if (!text) {
          throw new Error("Missing required parameter: text");
        }

        result = summarizeContract(text, maxLength);
        break;
      }

      case "analyze_contract": {
        const text = args?.text as string;
        const focusAreas = (args?.focus_areas as string[]) || [];

        if (!text) {
          throw new Error("Missing required parameter: text");
        }

        const analysis = analyzeContract(text, focusAreas);
        result = JSON.stringify(analysis, null, 2);
        break;
      }

      case "assess_risk": {
        const text = args?.text as string;

        if (!text) {
          throw new Error("Missing required parameter: text");
        }

        const assessment = assessRisk(text);
        result = JSON.stringify(assessment, null, 2);
        break;
      }

      case "send_notification": {
        const recipient = args?.recipient as string;
        const subject = args?.subject as string;
        const message = args?.message as string;
        const priority = (args?.priority as 'LOW' | 'MEDIUM' | 'HIGH') || 'MEDIUM';

        if (!recipient || !subject || !message) {
          throw new Error("Missing required parameters: recipient, subject, or message");
        }

        result = sendNotification(recipient, subject, message, priority);
        break;
      }

      default:
        throw new Error(`Unknown tool: ${name}`);
    }

    return {
      content: [
        {
          type: "text",
          text: result,
        },
      ],
    };
  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : String(error);
    console.error(`Error executing tool ${name}:`, errorMessage);

    return {
      content: [
        {
          type: "text",
          text: `Error: ${errorMessage}`,
        },
      ],
      isError: true,
    };
  }
});

// Start the server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);

  // Log to stderr (stdout is used for MCP protocol)
  console.error("Contract Analysis MCP Server running on stdio");
  console.error("Available tools:");
  console.error("  - summarize_contract");
  console.error("  - analyze_contract");
  console.error("  - assess_risk");
  console.error("  - send_notification");
}

main().catch((error) => {
  console.error("Fatal error starting MCP server:", error);
  process.exit(1);
});
