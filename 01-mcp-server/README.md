# Contract Analysis MCP Server

A Model Context Protocol (MCP) server that provides contract analysis tools.

## Tools Available

1. **summarize_contract** - Summarize contract documents
2. **analyze_contract** - Detailed analysis of clauses and terms
3. **assess_risk** - Risk assessment with recommendations
4. **send_notification** - Send notifications to stakeholders

## Setup

```bash
# Install dependencies
npm install

# Build TypeScript
npm run build

# Start server
npm start
```

## Testing with Claude Desktop

1. Build the server: `npm run build`

2. Configure Claude Desktop at:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

3. Add this configuration:
```json
{
  "mcpServers": {
    "contract-analysis": {
      "command": "node",
      "args": ["/absolute/path/to/mcp-agentic-frameworks-comparison/01-mcp-server/build/index.js"]
    }
  }
}
```

4. Restart Claude Desktop completely (Quit and reopen)

5. Test by asking: "List your available tools"

## Test Contracts

Sample contracts are available in `../test-data/contracts/`:
- `sample-contract-1.txt` - Standard service agreement (low risk)
- `sample-contract-2-high-risk.txt` - High-risk consulting agreement

## Development

```bash
# Watch mode for development
npm run watch

# Test the server manually
node build/index.js
```

## Project Structure

```
01-mcp-server/
├── src/
│   ├── index.ts              # Main MCP server
│   ├── schemas/
│   │   └── tool-schemas.ts   # Tool input schemas
│   └── tools/
│       ├── summarization.ts   # Summarization tool
│       ├── contract-analysis.ts # Analysis tool
│       ├── risk-assessment.ts   # Risk assessment tool
│       └── notifications.ts     # Notification tool
├── build/                    # Compiled JavaScript
├── package.json
└── tsconfig.json
```

## Next Steps

After verifying the MCP server works with Claude Desktop:
1. Proceed to Phase 2: Build LangGraph agent
2. Connect LangGraph to this MCP server
3. Compare with other frameworks
