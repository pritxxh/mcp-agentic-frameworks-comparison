# Custom Orchestrator using raw Anthropic API
import os
import json
from anthropic import Anthropic
from typing import List, Dict, Any
from dotenv import load_dotenv
import sys
sys.path.append('..')
from src.mcp_client import MCPClient, MCPTools

load_dotenv()


class ToolExecutor:
    """Executes MCP tools based on LLM requests."""

    def __init__(self, mcp_tools: MCPTools):
        self.tools = mcp_tools
        self.tool_map = {
            "summarize_contract": self._summarize,
            "analyze_contract": self._analyze,
            "assess_risk": self._assess_risk,
            "send_notification": self._notify
        }

    def execute(self, tool_name: str, arguments: Dict[str, Any]) -> str:
        """Execute a tool by name."""
        if tool_name not in self.tool_map:
            raise ValueError(f"Unknown tool: {tool_name}")
        return self.tool_map[tool_name](arguments)

    def _summarize(self, args: Dict) -> str:
        return self.tools.summarize_contract(args["text"], args.get("max_length", 100))

    def _analyze(self, args: Dict) -> str:
        return self.tools.analyze_contract(args["text"], args.get("focus_areas", []))

    def _assess_risk(self, args: Dict) -> str:
        return self.tools.assess_risk(args["text"])

    def _notify(self, args: Dict) -> str:
        return self.tools.send_notification(
            args["recipient"], args["subject"], args["message"], args.get("priority", "MEDIUM")
        )

    def get_tool_definitions(self) -> List[Dict]:
        """Return tool definitions for Claude API."""
        return [
            {
                "name": "summarize_contract",
                "description": "Summarize a contract document",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string", "description": "Contract text"},
                        "max_length": {"type": "number", "description": "Max words"}
                    },
                    "required": ["text"]
                }
            },
            {
                "name": "analyze_contract",
                "description": "Analyze contract clauses",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string"},
                        "focus_areas": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["text"]
                }
            },
            {
                "name": "assess_risk",
                "description": "Assess contract risk",
                "input_schema": {
                    "type": "object",
                    "properties": {"text": {"type": "string"}},
                    "required": ["text"]
                }
            },
            {
                "name": "send_notification",
                "description": "Send notification",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "recipient": {"type": "string"},
                        "subject": {"type": "string"},
                        "message": {"type": "string"},
                        "priority": {"type": "string"}
                    },
                    "required": ["recipient", "subject", "message"]
                }
            }
        ]


class ContractOrchestrator:
    """Custom orchestrator using raw Anthropic API."""

    def __init__(self, api_key: str, tool_executor: ToolExecutor):
        self.client = Anthropic(api_key=api_key)
        self.executor = tool_executor
        self.model = "claude-sonnet-4-20250514"
        self.max_iterations = 10

    def run(self, initial_prompt: str) -> Dict[str, Any]:
        """Run the orchestration loop."""
        messages = [{"role": "user", "content": initial_prompt}]
        tool_results = []
        iterations = 0

        while iterations < self.max_iterations:
            iterations += 1
            print(f"\n--- Iteration {iterations} ---")

            # Call Claude with tools
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                tools=self.executor.get_tool_definitions(),
                messages=messages
            )

            # Check stop reason
            if response.stop_reason == "end_turn":
                final_text = self._extract_text(response.content)
                return {
                    "success": True,
                    "result": final_text,
                    "iterations": iterations,
                    "tool_calls": tool_results
                }

            elif response.stop_reason == "tool_use":
                # Extract tool uses
                tool_uses = [block for block in response.content if block.type == "tool_use"]

                # Add assistant message
                messages.append({"role": "assistant", "content": response.content})

                # Execute tools
                tool_result_content = []
                for tool_use in tool_uses:
                    print(f"🔧 Tool: {tool_use.name}")

                    try:
                        result = self.executor.execute(tool_use.name, tool_use.input)
                        print(f"   ✅ Result: {result[:100]}...")

                        tool_result_content.append({
                            "type": "tool_result",
                            "tool_use_id": tool_use.id,
                            "content": result
                        })

                        tool_results.append({
                            "tool": tool_use.name,
                            "args": tool_use.input,
                            "result": result
                        })

                    except Exception as e:
                        print(f"   ❌ Error: {e}")
                        tool_result_content.append({
                            "type": "tool_result",
                            "tool_use_id": tool_use.id,
                            "content": f"Error: {str(e)}",
                            "is_error": True
                        })

                # Add tool results
                messages.append({"role": "user", "content": tool_result_content})

            else:
                return {
                    "success": False,
                    "error": f"Unexpected stop reason: {response.stop_reason}",
                    "iterations": iterations
                }

        return {
            "success": False,
            "error": "Max iterations reached",
            "iterations": iterations
        }

    def _extract_text(self, content: List) -> str:
        """Extract text from content blocks."""
        return "\n".join([block.text for block in content if hasattr(block, 'text')])


if __name__ == "__main__":
    # Initialize MCP
    mcp_client = MCPClient(os.getenv("MCP_SERVER_PATH"))
    mcp_client.start()

    try:
        mcp_tools = MCPTools(mcp_client)
        executor = ToolExecutor(mcp_tools)
        orchestrator = ContractOrchestrator(os.getenv("ANTHROPIC_API_KEY"), executor)

        test_contract = """
        SERVICE AGREEMENT
        Provider: TechCorp. Client: StartupCo.
        Payment: $10,000/month. UNLIMITED LIABILITY.
        No termination clause.
        """

        prompt = f"""Analyze this contract:
1. Summarize it
2. Analyze focusing on payment and liability
3. Assess the risk
4. If risk is HIGH, notify legal@startup.co

Contract: {test_contract}"""

        print("🚀 Starting Custom Orchestrator...")
        result = orchestrator.run(prompt)

        print("\n=== FINAL RESULT ===")
        print(f"Success: {result['success']}")
        print(f"Iterations: {result['iterations']}")
        print(f"Tool calls: {len(result.get('tool_calls', []))}")

    finally:
        mcp_client.stop()
