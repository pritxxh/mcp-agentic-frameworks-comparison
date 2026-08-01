# CrewAI Multi-Agent Contract Analysis
import os
from crewai import Agent, Task, Crew, Process
from langchain_anthropic import ChatAnthropic
from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import sys
sys.path.append('..')
from src.mcp_client import MCPClient, MCPTools

load_dotenv()

# Initialize MCP
mcp_client = MCPClient(os.getenv("MCP_SERVER_PATH"))
mcp_client.start()
mcp_tools = MCPTools(mcp_client)

# LLM
llm = ChatAnthropic(model="claude-sonnet-4-20250514", temperature=0)


# CrewAI Tool Wrappers
class SummarizeInput(BaseModel):
    text: str = Field(..., description="Contract text to summarize")

class SummarizeTool(BaseTool):
    name: str = "Summarize Contract"
    description: str = "Summarizes a contract document"
    args_schema: Type[BaseModel] = SummarizeInput

    def _run(self, text: str) -> str:
        return mcp_tools.summarize_contract(text)


class AnalyzeInput(BaseModel):
    text: str = Field(..., description="Contract text to analyze")

class AnalyzeTool(BaseTool):
    name: str = "Analyze Contract"
    description: str = "Analyzes contract clauses"
    args_schema: Type[BaseModel] = AnalyzeInput

    def _run(self, text: str) -> str:
        return mcp_tools.analyze_contract(text, ["payment", "liability", "termination"])


class RiskInput(BaseModel):
    text: str = Field(..., description="Contract text")

class RiskTool(BaseTool):
    name: str = "Assess Risk"
    description: str = "Assesses contract risk"
    args_schema: Type[BaseModel] = RiskInput

    def _run(self, text: str) -> str:
        return mcp_tools.assess_risk(text)


# Agents
def create_agents():
    analyst = Agent(
        role="Contract Analyst",
        goal="Analyze contracts thoroughly",
        backstory="Expert contract analyst with 15 years experience",
        tools=[SummarizeTool(), AnalyzeTool()],
        llm=llm,
        verbose=False
    )

    assessor = Agent(
        role="Risk Assessor",
        goal="Identify contract risks",
        backstory="Risk management expert",
        tools=[RiskTool()],
        llm=llm,
        verbose=False
    )

    return analyst, assessor


def run_contract_analysis(contract_text: str):
    """Run CrewAI analysis."""
    analyst, assessor = create_agents()

    analysis_task = Task(
        description=f"Analyze this contract:\n{contract_text}",
        agent=analyst,
        expected_output="Contract analysis with summary"
    )

    risk_task = Task(
        description=f"Assess risk for:\n{contract_text}",
        agent=assessor,
        expected_output="Risk assessment",
        context=[analysis_task]
    )

    crew = Crew(
        agents=[analyst, assessor],
        tasks=[analysis_task, risk_task],
        process=Process.sequential,
        verbose=False
    )

    result = crew.kickoff()
    return result


if __name__ == "__main__":
    test_contract = "Service Agreement between A and B. Payment: $10,000/month. UNLIMITED LIABILITY."

    print("🚀 Running CrewAI Analysis...")
    result = run_contract_analysis(test_contract)
    print(f"\n✅ Result: {result}")

    mcp_client.stop()
