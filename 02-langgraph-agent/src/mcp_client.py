# MCP Client for Python - connects to Node.js MCP server
import subprocess
import json
import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

class MCPClient:
    """Client to interact with MCP server via subprocess."""

    def __init__(self, server_path: str):
        self.server_path = server_path
        self.process: Optional[subprocess.Popen] = None
        self.request_id = 0

    def start(self):
        """Start the MCP server process."""
        try:
            self.process = subprocess.Popen(
                ['node', self.server_path],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1  # Line-buffered
            )
            logger.info(f"MCP server started from {self.server_path}")
        except Exception as e:
            logger.error(f"Failed to start MCP server: {e}")
            raise

    def send_request(self, method: str, params: Dict = None) -> Dict:
        """Send JSON-RPC request to MCP server."""
        if not self.process:
            raise RuntimeError("MCP server not started")

        self.request_id += 1
        request = {
            "jsonrpc": "2.0",
            "id": self.request_id,
            "method": method,
            "params": params or {}
        }

        try:
            request_json = json.dumps(request) + "\n"
            self.process.stdin.write(request_json)
            self.process.stdin.flush()

            response_line = self.process.stdout.readline()
            if not response_line:
                raise Exception("No response from MCP server")

            response = json.loads(response_line)

            if "error" in response:
                raise Exception(f"MCP Error: {response['error']}")

            return response.get("result", {})
        except Exception as e:
            logger.error(f"MCP request failed: {e}")
            raise

    def list_tools(self) -> List[Dict]:
        """List all available tools."""
        result = self.send_request("tools/list")
        return result.get("tools", [])

    def call_tool(self, name: str, arguments: Dict) -> Any:
        """Call a specific tool."""
        result = self.send_request("tools/call", {
            "name": name,
            "arguments": arguments
        })

        # Extract text content from MCP response
        content = result.get("content", [])
        if content and len(content) > 0:
            return content[0].get("text", "")
        return ""

    def stop(self):
        """Stop the MCP server process."""
        if self.process:
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
            logger.info("MCP server stopped")


class MCPTools:
    """High-level wrapper for MCP contract analysis tools."""

    def __init__(self, client: MCPClient):
        self.client = client

    def summarize_contract(self, text: str, max_length: int = 100) -> str:
        """Summarize a contract document."""
        return self.client.call_tool("summarize_contract", {
            "text": text,
            "max_length": max_length
        })

    def analyze_contract(self, text: str, focus_areas: List[str] = None) -> str:
        """Analyze contract clauses and terms."""
        return self.client.call_tool("analyze_contract", {
            "text": text,
            "focus_areas": focus_areas or []
        })

    def assess_risk(self, text: str) -> str:
        """Assess contract risk level."""
        return self.client.call_tool("assess_risk", {
            "text": text
        })

    def send_notification(self, recipient: str, subject: str,
                         message: str, priority: str = "MEDIUM") -> str:
        """Send notification to stakeholders."""
        return self.client.call_tool("send_notification", {
            "recipient": recipient,
            "subject": subject,
            "message": message,
            "priority": priority
        })
