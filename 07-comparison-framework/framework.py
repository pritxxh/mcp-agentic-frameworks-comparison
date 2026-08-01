# Complete Comparison Framework
import json
import time
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime


class TestCase:
    def __init__(self, data: Dict):
        self.id = data['id']
        self.name = data['name']
        self.contract = data['contract']
        self.expected_tools = data['expected_tools']
        self.complexity = data.get('complexity', 'medium')

    def to_prompt(self) -> str:
        return f"""Analyze this contract:
1. Summarize it
2. Analyze key terms
3. Assess the risk level
4. If risk is HIGH or CRITICAL, notify legal@startup.co

Contract:
{self.contract}
"""


def load_test_cases() -> List[TestCase]:
    """Load all test cases from JSON files."""
    test_case_dir = Path(__file__).parent / 'test-cases'
    test_cases = []

    for file_path in test_case_dir.glob('*.json'):
        with open(file_path) as f:
            data = json.load(f)
            test_cases.append(TestCase(data))

    return sorted(test_cases, key=lambda tc: tc.complexity)


class MetricsCollector:
    """Collect and analyze metrics across frameworks."""

    def __init__(self):
        self.results = []

    def record_result(self, framework: str, test_case_id: str,
                     execution_time: float, success: bool,
                     tool_count: int = 0, error: str = None):
        """Record a single test result."""
        record = {
            "timestamp": datetime.now().isoformat(),
            "framework": framework,
            "test_case_id": test_case_id,
            "execution_time_seconds": execution_time,
            "success": success,
            "tool_count": tool_count,
            "error": error
        }
        self.results.append(record)

    def analyze_by_framework(self) -> Dict[str, Dict]:
        """Analyze metrics grouped by framework."""
        frameworks = {}

        for result in self.results:
            fw = result["framework"]
            if fw not in frameworks:
                frameworks[fw] = {
                    "total_runs": 0,
                    "successful_runs": 0,
                    "total_time": 0,
                    "total_tools": 0
                }

            frameworks[fw]["total_runs"] += 1
            if result["success"]:
                frameworks[fw]["successful_runs"] += 1
            frameworks[fw]["total_time"] += result["execution_time_seconds"]
            frameworks[fw]["total_tools"] += result["tool_count"]

        # Calculate averages
        for fw, data in frameworks.items():
            data["success_rate"] = data["successful_runs"] / data["total_runs"] if data["total_runs"] > 0 else 0
            data["avg_time"] = data["total_time"] / data["total_runs"] if data["total_runs"] > 0 else 0
            data["avg_tools_per_run"] = data["total_tools"] / data["total_runs"] if data["total_runs"] > 0 else 0

        return frameworks

    def generate_report(self) -> str:
        """Generate comparison report."""
        frameworks = self.analyze_by_framework()

        report = ["# Framework Comparison Report\n"]
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        report.append(f"Total test runs: {len(self.results)}\n")

        report.append("\n## Framework Summary\n")
        for fw, data in sorted(frameworks.items()):
            report.append(f"\n### {fw.upper()}")
            report.append(f"- Runs: {data['total_runs']}")
            report.append(f"- Success Rate: {data['success_rate']*100:.1f}%")
            report.append(f"- Avg Execution Time: {data['avg_time']:.2f}s")
            report.append(f"- Avg Tools per Run: {data['avg_tools_per_run']:.1f}")

        return "\n".join(report)

    def save_json(self, filepath: str):
        """Save raw results as JSON."""
        with open(filepath, 'w') as f:
            json.dump({
                "generated_at": datetime.now().isoformat(),
                "results": self.results,
                "analysis": self.analyze_by_framework()
            }, f, indent=2)

    def save_report(self, filepath: str):
        """Save report as markdown."""
        with open(filepath, 'w') as f:
            f.write(self.generate_report())


if __name__ == "__main__":
    # Load test cases
    test_cases = load_test_cases()
    print(f"Loaded {len(test_cases)} test cases")

    # Create collector
    collector = MetricsCollector()

    # Simulate some results (in real use, frameworks would run)
    print("\n📊 Comparison framework ready!")
    print("To run full comparison, use: python compare.py")
