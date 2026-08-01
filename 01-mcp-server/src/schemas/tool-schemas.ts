// Tool schema definitions for MCP server

export const SUMMARIZE_SCHEMA = {
  type: "object",
  properties: {
    text: {
      type: "string",
      description: "The contract text to summarize"
    },
    max_length: {
      type: "number",
      description: "Maximum length of summary in words (default: 100)"
    }
  },
  required: ["text"]
} as const;

export const ANALYZE_SCHEMA = {
  type: "object",
  properties: {
    text: {
      type: "string",
      description: "The contract text to analyze"
    },
    focus_areas: {
      type: "array",
      items: { type: "string" },
      description: "Specific areas to focus on (e.g., 'payment terms', 'liability')"
    }
  },
  required: ["text"]
} as const;

export const RISK_SCHEMA = {
  type: "object",
  properties: {
    text: {
      type: "string",
      description: "The contract text to assess for risk"
    }
  },
  required: ["text"]
} as const;

export const NOTIFICATION_SCHEMA = {
  type: "object",
  properties: {
    recipient: {
      type: "string",
      description: "Email address of the recipient"
    },
    subject: {
      type: "string",
      description: "Email subject line"
    },
    message: {
      type: "string",
      description: "Email message content"
    },
    priority: {
      type: "string",
      enum: ["LOW", "MEDIUM", "HIGH"],
      description: "Priority level (default: MEDIUM)"
    }
  },
  required: ["recipient", "subject", "message"]
} as const;
