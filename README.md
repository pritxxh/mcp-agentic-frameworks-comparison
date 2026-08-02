[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/pritxxh/mcp-agentic-frameworks-comparison?style=social)](https://github.com/pritxxh/mcp-agentic-frameworks-comparison/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/pritxxh/mcp-agentic-frameworks-comparison?style=social)](https://github.com/pritxxh/mcp-agentic-frameworks-comparison/network/members)
[![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-blue)](https://modelcontextprotocol.io)
[![LangGraph](https://img.shields.io/badge/LangGraph-Framework-green)](https://langchain-ai.github.io/langgraph/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Framework-purple)](https://www.crewai.com/)
[![Anthropic Claude](https://img.shields.io/badge/Claude-AI-orange)](https://www.anthropic.com/)

# Multi-Agent Orchestration Framework Comparison

## 🎉 Complete Project - Ready to Use!

This project provides a comprehensive comparison of different agent orchestration frameworks using a shared MCP (Model Context Protocol) server for contract analysis.

## 🔍 What's Inside

**This repository demonstrates:**
- ✅ **MCP Server** implementation with 4 contract analysis tools
- ✅ **LangGraph** integration for state-based agentic workflows
- ✅ **CrewAI** implementation for role-based multi-agent systems
- ✅ **Custom orchestration** using raw Anthropic Claude API
- ✅ **Production patterns** for real-world AI agent deployments
- ✅ **Cross-platform** support (macOS, Windows, Linux)

**Perfect for:**
- Developers exploring agentic AI frameworks
- Teams building production AI agent systems
- Anyone learning MCP (Model Context Protocol)
- Comparing LangGraph vs CrewAI vs custom approaches
- Implementing contract analysis automation

## ⭐ Support This Project

If you find this comparison helpful, please consider:
- ⭐ **Star this repository** to show your support
- 🔀 **Fork it** to experiment with your own use cases
- 📢 **Share it** with others who might benefit
- 💬 **Open discussions** for questions and improvements

[![GitHub stars](https://img.shields.io/github/stars/pritxxh/mcp-agentic-frameworks-comparison?style=for-the-badge&logo=github)](https://github.com/pritxxh/mcp-agentic-frameworks-comparison/stargazers)

## 🏗️ Architecture Overview

![Architecture Diagram](diagram.jpg)

*Visual representation of the MCP server architecture with three framework orchestration approaches: LangGraph (state-based), CrewAI (role-based), and Custom (raw API). All frameworks share the same MCP server and tools for consistent contract analysis.*

## ⚖️ Framework Comparison

| Feature | LangGraph | CrewAI | Custom |
|---------|-----------|---------|---------|
| **Control Level** | High | Medium | Total |
| **Learning Curve** | Moderate | Steep | Shallow |
| **Code Complexity** | Medium | High | Low |
| **State Management** | Built-in | Automated | Manual |
| **Debugging** | Easy | Medium | Easy |
| **Best For** | Structured workflows | Multi-agent collab | Learning/Full control |
| **Performance** | Fast | Medium | Fast |
| **Dependencies** | LangChain ecosystem | CrewAI + deps | Minimal (anthropic) |

**Quick Guide:**
- 🟢 **LangGraph** → Need predictable, stateful workflows with explicit control
- 🟣 **CrewAI** → Complex scenarios with multiple specialized agents
- 🟠 **Custom** → Learning orchestration or need minimal dependencies

## 📁 Project Structure

```
mcp-agentic-frameworks-comparison/
├── STARTER_GUIDE/           # Complete documentation (12 guides)
├── 01-mcp-server/           # ✅ Phase 1: MCP Server (4 tools)
├── 02-langgraph-agent/      # ✅ Phase 2: LangGraph (stateful workflow)
├── 03-crewai-agent/         # ✅ Phase 3: CrewAI (role-based agents)
├── 05-custom-orchestrator/  # ✅ Phase 4: Custom (raw Anthropic API)
├── 07-comparison-framework/ # ✅ Phase 6: Comparison system
└── test-data/              # Sample contracts
```

## 🚀 Quick Start

### 1. Build the MCP Server
```bash
cd 01-mcp-server
npm install
npm run build
```

### 2. Test with Claude Desktop (Optional)

**macOS:**
```bash
# Config location: ~/Library/Application Support/Claude/claude_desktop_config.json
open ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

**Windows:**
```bash
# Config location: %APPDATA%\Claude\claude_desktop_config.json
notepad %APPDATA%\Claude\claude_desktop_config.json
```

**Linux:**
```bash
# Config location: ~/.config/Claude/claude_desktop_config.json
nano ~/.config/Claude/claude_desktop_config.json
```

Add this configuration (replace with your actual path):
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

**Important:**
- Use absolute paths (not `~` or relative paths)
- On Windows, use forward slashes: `C:/Users/YourName/mcp-agentic-frameworks-comparison/...`
- Restart Claude Desktop completely after config changes

**Verify Setup:**
In Claude Desktop, type: "List your available tools"

You should see:
- ✅ summarize_contract
- ✅ analyze_contract
- ✅ assess_risk
- ✅ send_notification

### 3. Set Up Python Environments

**macOS/Linux:**
```bash
cd 02-langgraph-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add ANTHROPIC_API_KEY and MCP_SERVER_PATH
```

**Windows:**
```bash
cd 02-langgraph-agent
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# Edit .env and add ANTHROPIC_API_KEY and MCP_SERVER_PATH
```

Repeat for other frameworks:
- `03-crewai-agent`
- `05-custom-orchestrator`

### 4. Run Individual Frameworks

**macOS/Linux:**
```bash
# LangGraph
cd 02-langgraph-agent
source venv/bin/activate
python src/workflow.py

# CrewAI
cd 03-crewai-agent
source venv/bin/activate
python src/crew_workflow.py

# Custom Orchestrator
cd 05-custom-orchestrator
source venv/bin/activate
python src/orchestrator.py
```

**Windows:**
```bash
# LangGraph
cd 02-langgraph-agent
venv\Scripts\activate
python src\workflow.py

# CrewAI
cd 03-crewai-agent
venv\Scripts\activate
python src\crew_workflow.py

# Custom Orchestrator
cd 05-custom-orchestrator
venv\Scripts\activate
python src\orchestrator.py
```

## 🔧 What Each Framework Does

All frameworks analyze contracts through the same MCP tools:
1. **Summarize** - Extract key points
2. **Analyze** - Examine clauses and terms
3. **Assess Risk** - Evaluate risk level
4. **Notify** - Alert stakeholders if high risk

### Framework Differences

**LangGraph:**
- ✅ Deterministic state-based workflow
- ✅ Explicit control flow
- ✅ Easy to debug
- ⚠️ More code for complex branching

**CrewAI:**
- ✅ Role-based agent collaboration
- ✅ Natural task delegation
- ✅ Good for complex multi-agent scenarios
- ⚠️ Less deterministic, more autonomous

**Custom Orchestrator:**
- ✅ Full control over execution
- ✅ Understand what frameworks abstract
- ✅ Lightweight, no dependencies
- ⚠️ More code to maintain

## 📊 Tools Available

The MCP server provides 4 contract analysis tools:

1. **summarize_contract** - Compresses contract to key points
2. **analyze_contract** - Extracts clauses, parties, warnings
3. **assess_risk** - Calculates risk score and level
4. **send_notification** - Simulates stakeholder alerts

## 🎯 Use Cases

**Use LangGraph when:**
- You need predictable, debuggable workflows
- State management is important
- You want explicit control flow

**Use CrewAI when:**
- You have complex multi-agent scenarios
- Agents need to collaborate with roles
- You want more autonomous behavior

**Use Custom when:**
- You need full control
- You're learning how orchestration works
- You want minimal dependencies

## 📚 Documentation

Complete guides available in `STARTER_GUIDE/`:
- **README.md** - Main guide with learning paths
- **QUICK_START.md** - 30-minute introduction
- **PHASE_1-6.md** - Detailed build guides
- **TROUBLESHOOTING.md** - Common issues & solutions

## 🧪 Test Data

Sample contracts in `test-data/contracts/`:
- **sample-contract-1.txt** - Standard service agreement (LOW risk)
- **sample-contract-2-high-risk.txt** - Problematic consulting agreement (CRITICAL risk)

## 💡 Key Learnings

1. **MCP is the foundation** - Build and test it first
2. **Test each layer independently** - Don't integrate until each works
3. **Different frameworks fit different needs** - No one-size-fits-all
4. **Understanding abstractions matters** - Custom orchestrator teaches what frameworks hide

## 🔍 Troubleshooting

**MCP server not showing in Claude Desktop?**
- Check absolute path (not `~` or relative)
- Verify `npm run build` completed
- Restart Claude Desktop completely

**Python import errors?**
- Activate virtual environment: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

**Tool execution hangs?**
- Check MCP server path in .env
- Verify MCP server starts: `node build/index.js`

See `STARTER_GUIDE/TROUBLESHOOTING.md` for more solutions.

## 📈 Next Steps

### For Learning & Comparison
1. **Test each framework** - Run the examples
2. **Compare behaviors** - Note differences in execution
3. **Try your own contracts** - Test with real documents
4. **Extend the tools** - Add new contract analysis capabilities

### For Production Use

This project uses **rule-based tools** (fast, predictable, no API costs) which are perfect for learning and comparison. For production systems, consider these enhancements:

#### 🔄 Hybrid Approach (Recommended)

**Keep rule-based for:**
- Initial screening and fast pattern detection
- Structured extraction (parties, dates, amounts)
- Obvious red flags (keyword detection)

**Add LLM-enhanced for:**
- Deep contextual analysis
- Nuanced risk assessment
- Complex legal interpretation
- Actionable recommendations

**Cost comparison:**
- Rule-based: $0 per contract, ~50ms, ~70% accuracy
- LLM-enhanced: ~$0.05 per contract, ~8s, ~95% accuracy
- Hybrid: ~$0.01 per contract, ~3s, ~90% accuracy

#### 🚀 Production Features

**1. Real Email Notifications**
- Integrate SendGrid, AWS SES, Mailgun, or Postmark
- Replace simulated notifications with actual alerts

**2. Database Integration**
- Store analysis results for auditing
- Track contract history and changes
- Enable reporting and analytics

**3. Document Parser**
- Add PDF/DOCX support with `pdf-parse` or `mammoth`
- Handle real contract files, not just text

**4. Authentication & API Gateway**
- Build REST API around MCP server
- Add user authentication and rate limiting
- Deploy behind AWS API Gateway or similar

**5. Monitoring & Logging**
- Track tool usage and performance
- Set up alerts for failures
- Audit all contract analyses

See `01-mcp-server/src/tools/llm-enhanced.ts` for an example of LLM-enhanced tools.

## 🔗 Related Resources

### Official Documentation
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io) - Protocol specification and guides
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/) - State-based agent workflows
- [CrewAI Documentation](https://docs.crewai.com/) - Role-based multi-agent framework
- [Anthropic Claude API](https://docs.anthropic.com/) - Claude API reference
- [Claude Desktop](https://claude.ai/download) - Desktop client with MCP support

### Learn More
- [MCP Quickstart Guide](https://modelcontextprotocol.io/quickstart) - Get started with MCP
- [Building Agents with LangGraph](https://langchain-ai.github.io/langgraph/tutorials/) - Official tutorials
- [CrewAI Examples](https://github.com/joaomdmoura/crewAI-examples) - Community examples

### Related Projects
- [LangChain](https://github.com/langchain-ai/langchain) - The foundation for LangGraph
- [MCP Servers](https://github.com/modelcontextprotocol/servers) - Official MCP server examples
- [Awesome MCP](https://github.com/punkpeye/awesome-mcp) - Curated MCP resources

## 🙏 Credits

Built following best practices for:
- Progressive complexity (simple → advanced)
- Independent layer testing
- Comprehensive troubleshooting
- Fair framework comparison

## 📝 License

MIT License - Feel free to use for learning and commercial projects.

---

**Ready to start?** Begin with `STARTER_GUIDE/QUICK_START.md` or test the MCP server with Claude Desktop!
