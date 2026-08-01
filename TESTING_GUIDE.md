# 🚀 Complete Testing & Comparison Guide

## You Now Have: Option B + C Complete!

### ✅ Option C: Comprehensive Test Suite
- **6 diverse contracts** covering all scenarios
- Low risk, high risk, balanced, SaaS, NDA, minimal
- Edge cases and missing clauses tested
- Complete test documentation

### ✅ Option B: All Frameworks Ready
- LangGraph (stateful workflow)
- CrewAI (multi-agent)
- Custom (raw orchestration)
- Unified test runner
- Automated setup script

---

## 🎯 Quick Start (5 Minutes)

### Step 1: Run Automated Setup
```bash
cd /path/to/mcp-agentic-frameworks-comparison

# Run setup script
./setup_all.sh
```

**What this does:**
- ✅ Checks Python & Node.js
- ✅ Verifies MCP server is built
- ✅ Creates virtual environments for all 3 frameworks
- ✅ Installs all dependencies
- ✅ Creates .env files with correct paths

### Step 2: Add Your API Key
```bash
# Edit each .env file and add your Anthropic API key
# Or use this quick command:
export ANTHROPIC_API_KEY="your-key-here"

# Then update all .env files
echo "ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY" >> 02-langgraph-agent/.env
echo "ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY" >> 03-crewai-agent/.env
echo "ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY" >> 05-custom-orchestrator/.env
```

### Step 3: Run Your First Test
```bash
# Test the high-risk contract with LangGraph
python3 test_runner.py --framework langgraph --contract contract-2-high-risk
```

**Expected output:**
- ✅ Contract loaded
- ✅ LangGraph executes workflow
- ✅ Risk: CRITICAL detected
- ✅ Notification sent
- ✅ Results saved

---

## 📊 Test Execution Options

### Option 1: Test Single Framework
```bash
# Test all contracts with LangGraph only
python3 test_runner.py --framework langgraph

# Test all contracts with CrewAI only
python3 test_runner.py --framework crewai

# Test all contracts with Custom only
python3 test_runner.py --framework custom
```

### Option 2: Test Single Contract
```bash
# Test high-risk contract across all frameworks
python3 test_runner.py --contract contract-2-high-risk

# Test balanced contract across all frameworks
python3 test_runner.py --contract contract-3-balanced
```

### Option 3: Full Comparison (Recommended)
```bash
# Run ALL contracts through ALL frameworks
python3 test_runner.py
```

**This runs:**
- 6 contracts × 3 frameworks = **18 tests total**
- Takes ~5-10 minutes
- Generates complete comparison data

---

## 📈 Understanding Results

### Console Output
```
📄 Contract: contract-2-high-risk
   [1/18] Testing with langgraph...
      ✅ Success | 8.45s | Risk: CRITICAL | Notify: True
   [2/18] Testing with crewai...
      ✅ Success | 12.30s | Risk: CRITICAL | Notify: False
   [3/18] Testing with custom...
      ✅ Success | 6.75s | Risk: CRITICAL | Notify: True
```

### Results File
Saved to: `test-results/results-YYYYMMDD-HHMMSS.json`

```json
{
  "timestamp": "2026-08-01T15:30:00",
  "results": [
    {
      "framework": "langgraph",
      "contract_id": "contract-2-high-risk",
      "execution_time_seconds": 8.45,
      "success": true,
      "risk_level": "CRITICAL",
      "notification_sent": true,
      "tool_call_count": 4
    }
  ]
}
```

---

## 🔍 What to Look For in Comparison

### Speed Comparison
**Question:** Which framework is fastest?

**Expected:**
- Custom orchestrator: ~6-8 seconds (least overhead)
- LangGraph: ~8-10 seconds (state management)
- CrewAI: ~10-15 seconds (multi-agent coordination)

### Reliability Comparison
**Question:** Which is most consistent?

**Check:**
- Does each framework detect the same risk levels?
- Are notifications triggered consistently?
- Do any frameworks have errors?

### Tool Usage Comparison
**Question:** How many tools does each use?

**Expected:**
- All should call 4 tools for complete analysis
- Check if any skip steps
- Verify notification logic

### Accuracy Comparison
**Question:** Do all frameworks identify risks correctly?

**Expected Risk Levels:**
- Contract 1 (standard): LOW (15-25)
- Contract 2 (high-risk): CRITICAL (70-80) ✅ TESTED
- Contract 3 (balanced): LOW (10-20)
- Contract 4 (software): MEDIUM (30-40)
- Contract 5 (NDA): LOW (5-10)
- Contract 6 (minimal): MEDIUM-HIGH (40-55)

---

## 🎯 Test Scenarios

### Scenario 1: Risk Detection Accuracy
**Goal:** Verify all frameworks detect high risk

```bash
python3 test_runner.py --contract contract-2-high-risk
```

**Success criteria:**
- ✅ All 3 frameworks score 70-80 points
- ✅ All detect "CRITICAL" or "HIGH"
- ✅ LangGraph and Custom send notifications
- ✅ (CrewAI may or may not - it's more autonomous)

### Scenario 2: Balanced Contract Handling
**Goal:** Verify frameworks don't over-flag safe contracts

```bash
python3 test_runner.py --contract contract-3-balanced
```

**Success criteria:**
- ✅ All score 10-20 points (LOW risk)
- ✅ None send notifications
- ✅ All complete successfully

### Scenario 3: Missing Clause Detection
**Goal:** Test edge case handling

```bash
python3 test_runner.py --contract contract-6-minimal
```

**Success criteria:**
- ✅ All detect missing clauses
- ✅ Risk score 40-55 (MEDIUM-HIGH)
- ✅ Flag incomplete contract

### Scenario 4: Performance Under Load
**Goal:** Test execution speed

```bash
time python3 test_runner.py --framework langgraph
time python3 test_runner.py --framework crewai
time python3 test_runner.py --framework custom
```

**Compare:**
- Total execution time
- Average time per contract
- Consistency of timing

---

## 📊 Expected Comparison Results

### Framework Strengths

**LangGraph:**
- ✅ Most deterministic
- ✅ Clear state management
- ✅ Easy to debug
- ✅ Consistent results
- ⚠️ More verbose code

**CrewAI:**
- ✅ Natural agent collaboration
- ✅ Role-based design
- ✅ Rich agent interactions
- ⚠️ More autonomous (less predictable)
- ⚠️ Longer execution time

**Custom:**
- ✅ Fastest execution
- ✅ Full transparency
- ✅ Minimal dependencies
- ✅ Easy to understand
- ⚠️ More code to maintain

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError"
```bash
# Reinstall dependencies
cd 02-langgraph-agent
source venv/bin/activate
pip install -r requirements.txt
deactivate
```

### Issue: "ANTHROPIC_API_KEY not found"
```bash
# Check .env files exist
ls -la */. env

# Manually add key
echo "ANTHROPIC_API_KEY=your-key" > 02-langgraph-agent/.env
```

### Issue: "MCP server not found"
```bash
# Rebuild MCP server
cd 01-mcp-server
npm run build
```

### Issue: Tests hang
- Check MCP server path in .env
- Verify Node.js is running
- Check for MCP server errors in stderr

---

## 📈 Next Steps After Testing

### 1. Analyze Results
- Compare execution times
- Check risk detection accuracy
- Note framework differences

### 2. Document Findings
Create a comparison report:
- Which framework is fastest?
- Which is most reliable?
- Which would you use in production?

### 3. Share Your Work
- Add to GitHub
- Write blog post
- Update resume/LinkedIn
- Create presentation

### 4. Enhance (Option C - Phase B)
Follow `ENHANCEMENT_GUIDE.md` to:
- Add LLM-powered tools
- Implement real notifications
- Add database storage
- Deploy to production

---

## 🎉 Success Checklist

After running full comparison, you should have:

- [ ] All 18 tests completed successfully
- [ ] Results JSON file generated
- [ ] Risk scores match expectations
- [ ] High-risk contract triggered notifications
- [ ] All frameworks completed without errors
- [ ] Timing data collected
- [ ] Framework differences documented

---

## 💡 Quick Commands Reference

```bash
# Setup everything
./setup_all.sh

# Single test
python3 test_runner.py --framework langgraph --contract contract-2-high-risk

# Test one framework fully
python3 test_runner.py --framework langgraph

# Full comparison
python3 test_runner.py

# View results
cat test-results/results-*.json | python3 -m json.tool
```

---

## 🎯 You Are Here

**Phase A: Learn & Compare** ✅ READY TO EXECUTE
- ✅ MCP server built and tested
- ✅ 6 test contracts created
- ✅ All frameworks set up
- ✅ Test runner created
- ✅ Ready to run!

**Phase B: Enhance for Production** 🔜 AFTER TESTING
- See `ENHANCEMENT_GUIDE.md`
- Add LLM intelligence
- Real integrations
- Production deployment

---

**Ready to run? Execute:**
```bash
cd /path/to/mcp-agentic-frameworks-comparison
./setup_all.sh
```

Then start testing! 🚀
