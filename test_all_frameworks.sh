#!/bin/bash
# Quick working test - runs each framework in its own venv

echo "🧪 3-FRAMEWORK COMPARISON - High-Risk Contract"
echo "="*60
echo ""

CONTRACT="test-data/contracts/sample-contract-2-high-risk.txt"

# Test 1: LangGraph
echo "1️⃣ Testing LangGraph..."
cd 02-langgraph-agent
source venv/bin/activate
python3 << 'PYTHON'
import sys
sys.path.insert(0, 'src')
from workflow import run_contract_analysis
import time

contract = open("../test-data/contracts/sample-contract-2-high-risk.txt").read()
start = time.time()
try:
    result = run_contract_analysis(contract)
    elapsed = time.time() - start
    print(f"   ✅ Success: {elapsed:.2f}s")
    print(f"   Notification: {result.get('notification_sent', False)}")
except Exception as e:
    print(f"   ❌ Error: {e}")
PYTHON
deactivate
cd ..
echo ""

# Test 2: CrewAI
echo "2️⃣ Testing CrewAI..."
cd 03-crewai-agent
source venv/bin/activate
python3 << 'PYTHON'
import sys
sys.path.insert(0, 'src')
from crew_workflow import run_contract_analysis
import time

contract = open("../test-data/contracts/sample-contract-2-high-risk.txt").read()
start = time.time()
try:
    result = run_contract_analysis(contract)
    elapsed = time.time() - start
    print(f"   ✅ Success: {elapsed:.2f}s")
except Exception as e:
    print(f"   ❌ Error: {e}")
PYTHON
deactivate
cd ..
echo ""

# Test 3: Custom
echo "3️⃣ Testing Custom Orchestrator..."
cd 05-custom-orchestrator
source venv/bin/activate
python3 << 'PYTHON'
import sys
import os
sys.path.insert(0, 'src')
sys.path.insert(0, '../02-langgraph-agent/src')
from orchestrator import ContractOrchestrator, ToolExecutor
from mcp_client import MCPClient, MCPTools
import time

contract = open("../test-data/contracts/sample-contract-2-high-risk.txt").read()
mcp_client = MCPClient(os.getenv("MCP_SERVER_PATH"))
mcp_client.start()

try:
    mcp_tools = MCPTools(mcp_client)
    executor = ToolExecutor(mcp_tools)
    orchestrator = ContractOrchestrator(os.getenv("ANTHROPIC_API_KEY"), executor)

    prompt = f"Analyze this contract: {contract}"

    start = time.time()
    result = orchestrator.run(prompt)
    elapsed = time.time() - start

    print(f"   ✅ Success: {elapsed:.2f}s")
    print(f"   Iterations: {result.get('iterations', 0)}")
    notified = any(tc['tool'] == 'send_notification' for tc in result.get('tool_calls', []))
    print(f"   Notification: {notified}")
finally:
    mcp_client.stop()
PYTHON
deactivate
cd ..

echo ""
echo "="*60
echo "✅ Test Complete!"
