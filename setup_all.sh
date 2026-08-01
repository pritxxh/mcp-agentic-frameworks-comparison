#!/bin/bash
# Setup script for all Python frameworks

set -e

echo "=========================================="
echo "Multi-Agent Framework Setup"
echo "=========================================="
echo ""

# Check Python version
echo "1. Checking Python version..."
python3 --version || { echo "❌ Python 3.10+ required"; exit 1; }
echo "✅ Python OK"
echo ""

# Check Node.js
echo "2. Checking Node.js..."
node --version || { echo "❌ Node.js required for MCP server"; exit 1; }
echo "✅ Node.js OK"
echo ""

# Check MCP server is built
echo "3. Checking MCP server..."
if [ -f "01-mcp-server/build/index.js" ]; then
    echo "✅ MCP server built"
else
    echo "⚠️  MCP server not built. Building now..."
    cd 01-mcp-server
    npm run build
    cd ..
    echo "✅ MCP server built"
fi
echo ""

# Get absolute MCP path
MCP_PATH=$(pwd)/01-mcp-server/build/index.js
echo "MCP Server Path: $MCP_PATH"
echo ""

# Setup LangGraph
echo "4. Setting up LangGraph (02-langgraph-agent)..."
cd 02-langgraph-agent
if [ ! -d "venv" ]; then
    echo "   Creating virtual environment..."
    python3 -m venv venv
fi
source venv/bin/activate
echo "   Installing dependencies..."
pip install -q langgraph langchain-anthropic python-dotenv anthropic
echo "   Creating .env file..."
cat > .env << EOF
ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY:-your_key_here}
MCP_SERVER_PATH=$MCP_PATH
EOF
deactivate
cd ..
echo "✅ LangGraph setup complete"
echo ""

# Setup CrewAI
echo "5. Setting up CrewAI (03-crewai-agent)..."
cd 03-crewai-agent
if [ ! -d "venv" ]; then
    echo "   Creating virtual environment..."
    python3 -m venv venv
fi
source venv/bin/activate
echo "   Installing dependencies..."
pip install -q crewai crewai-tools langchain-anthropic python-dotenv anthropic
echo "   Creating .env file..."
cat > .env << EOF
ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY:-your_key_here}
MCP_SERVER_PATH=$MCP_PATH
EOF
deactivate
cd ..
echo "✅ CrewAI setup complete"
echo ""

# Setup Custom Orchestrator
echo "6. Setting up Custom Orchestrator (05-custom-orchestrator)..."
cd 05-custom-orchestrator
if [ ! -d "venv" ]; then
    echo "   Creating virtual environment..."
    python3 -m venv venv
fi
source venv/bin/activate
echo "   Installing dependencies..."
pip install -q anthropic python-dotenv
echo "   Creating .env file..."
cat > .env << EOF
ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY:-your_key_here}
MCP_SERVER_PATH=$MCP_PATH
EOF
deactivate
cd ..
echo "✅ Custom Orchestrator setup complete"
echo ""

# Create test-results directory
mkdir -p test-results

echo "=========================================="
echo "✅ SETUP COMPLETE!"
echo "=========================================="
echo ""
echo "📋 Next Steps:"
echo ""
echo "1. Add your Anthropic API key to .env files:"
echo "   - 02-langgraph-agent/.env"
echo "   - 03-crewai-agent/.env"
echo "   - 05-custom-orchestrator/.env"
echo ""
echo "2. Run a quick test:"
echo "   python3 test_runner.py --framework langgraph --contract contract-2-high-risk"
echo ""
echo "3. Run full comparison:"
echo "   python3 test_runner.py"
echo ""
echo "4. View results in test-results/ directory"
echo ""
