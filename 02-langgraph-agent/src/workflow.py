# LangGraph Contract Analysis Workflow
import os
from typing import TypedDict, Annotated
import operator
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from src.mcp_client import MCPClient, MCPTools

load_dotenv()

# Initialize MCP
mcp_client = MCPClient(os.getenv("MCP_SERVER_PATH"))
mcp_client.start()
mcp_tools = MCPTools(mcp_client)


class ContractState(TypedDict):
    """State for contract analysis workflow."""
    contract_text: str
    summary: str
    analysis: str
    risk_assessment: str
    notification_sent: bool
    messages: Annotated[list, operator.add]


def create_workflow():
    """Create a multi-step contract analysis workflow."""

    workflow = StateGraph(ContractState)

    # Step 1: Summarize
    def summarize_step(state: ContractState):
        result = mcp_tools.summarize_contract(state["contract_text"])
        return {
            "summary": result,
            "messages": [f"✅ Summary completed"]
        }

    # Step 2: Analyze
    def analyze_step(state: ContractState):
        result = mcp_tools.analyze_contract(
            state["contract_text"],
            focus_areas=["payment", "liability", "termination"]
        )
        return {
            "analysis": result,
            "messages": [f"✅ Analysis completed"]
        }

    # Step 3: Risk Assessment
    def risk_step(state: ContractState):
        result = mcp_tools.assess_risk(state["contract_text"])
        return {
            "risk_assessment": result,
            "messages": [f"✅ Risk assessment completed"]
        }

    # Step 4: Notification (conditional)
    def notification_step(state: ContractState):
        # Check if risk is HIGH or CRITICAL
        if "HIGH" in state["risk_assessment"] or "CRITICAL" in state["risk_assessment"]:
            result = mcp_tools.send_notification(
                recipient="legal@startup.co",
                subject="High Risk Contract Alert",
                message=f"Risk Assessment:\n{state['risk_assessment']}",
                priority="HIGH"
            )
            return {
                "notification_sent": True,
                "messages": [f"✅ Notification sent to legal team"]
            }
        return {
            "notification_sent": False,
            "messages": [f"ℹ️ Risk acceptable, no notification needed"]
        }

    # Build workflow
    workflow.add_node("summarize", summarize_step)
    workflow.add_node("analyze", analyze_step)
    workflow.add_node("assess_risk", risk_step)
    workflow.add_node("notify", notification_step)

    # Define flow
    workflow.set_entry_point("summarize")
    workflow.add_edge("summarize", "analyze")
    workflow.add_edge("analyze", "assess_risk")
    workflow.add_edge("assess_risk", "notify")
    workflow.add_edge("notify", END)

    return workflow.compile()


def run_contract_analysis(contract_text: str):
    """Run the complete workflow on a contract."""
    app = create_workflow()

    initial_state = {
        "contract_text": contract_text,
        "summary": "",
        "analysis": "",
        "risk_assessment": "",
        "notification_sent": False,
        "messages": []
    }

    result = app.invoke(initial_state)
    return result


if __name__ == "__main__":
    # Test with sample contract
    test_contract = """
    SERVICE AGREEMENT

    This agreement is made between TechCorp (Provider) and StartupCo (Client).

    1. Services: Provider will deliver software development services.
    2. Payment: $10,000 per month, payable within 30 days.
    3. Liability: Provider assumes UNLIMITED LIABILITY for all damages.
    4. Term: 12 months starting January 1, 2026.
    5. Termination: Either party may terminate with 30 days notice.
    """

    print("🚀 Running LangGraph Contract Analysis Workflow...")
    result = run_contract_analysis(test_contract)

    print("\n=== RESULTS ===")
    print(f"Notification sent: {result['notification_sent']}")
    print("\nWorkflow steps:")
    for msg in result['messages']:
        print(f"  {msg}")

    mcp_client.stop()
