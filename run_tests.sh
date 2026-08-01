#!/bin/bash
# Final execution script - Run complete test suite

echo "🎉 COMPLETE 3-FRAMEWORK TEST SUITE"
echo "="*60
echo ""

# Check all frameworks
echo "📋 Framework Status:"
echo ""

# LangGraph
if [ -d "02-langgraph-agent/venv" ] && [ -f "02-langgraph-agent/.env" ]; then
    echo "✅ LangGraph - READY"
    LG_READY=1
else
    echo "❌ LangGraph - NOT READY"
    LG_READY=0
fi

# CrewAI
if [ -d "03-crewai-agent/venv" ] && [ -f "03-crewai-agent/.env" ]; then
    echo "✅ CrewAI - READY"
    CREW_READY=1
else
    echo "⚠️  CrewAI - Installation may still be running"
    CREW_READY=0
fi

# Custom
if [ -d "05-custom-orchestrator/venv" ] && [ -f "05-custom-orchestrator/.env" ]; then
    echo "✅ Custom Orchestrator - READY"
    CUSTOM_READY=1
else
    echo "❌ Custom Orchestrator - NOT READY"
    CUSTOM_READY=0
fi

TOTAL_READY=$((LG_READY + CREW_READY + CUSTOM_READY))

echo ""
echo "📊 Status: $TOTAL_READY/3 frameworks ready"
echo ""

if [ $TOTAL_READY -eq 3 ]; then
    echo "🎯 ALL SYSTEMS GO!"
    echo ""
    echo "Choose your test:"
    echo "  1. Quick test (high-risk contract only):"
    echo "     python3 test_runner.py --contract contract-2-high-risk"
    echo ""
    echo "  2. Test one framework (all 6 contracts):"
    echo "     python3 test_runner.py --framework langgraph"
    echo ""
    echo "  3. FULL COMPARISON (all frameworks, all contracts):"
    echo "     python3 test_runner.py"
    echo ""
    echo "Results will be saved to: test-results/"
    echo ""
elif [ $TOTAL_READY -eq 2 ]; then
    echo "⚠️  2 frameworks ready. You can test now or wait for CrewAI."
    echo ""
    echo "Test with 2 frameworks:"
    echo "  python3 quick_test.py"
else
    echo "❌ Setup incomplete. Please complete framework setup."
fi

echo "="*60
