# LangGraph Agent - README

## Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file from example
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

## Run

```bash
python src/workflow.py
```

## What It Does

1. **Summarizes** the contract
2. **Analyzes** clauses with focus on payment, liability, termination
3. **Assesses risk** level
4. **Notifies** legal team if risk is HIGH or CRITICAL

## Architecture

Uses LangGraph's StateGraph for deterministic, stateful workflow execution.
