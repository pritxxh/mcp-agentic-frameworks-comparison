// Enhanced Summarization Tool with LLM
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY
});

export async function summarizeContractLLM(text: string, maxLength: number = 100): Promise<string> {
  const message = await client.messages.create({
    model: "claude-sonnet-4-20250514",
    max_tokens: 500,
    messages: [{
      role: "user",
      content: `Summarize this contract in approximately ${maxLength} words. Focus on key terms, parties, payment, and obligations:\n\n${text}`
    }]
  });

  const summary = message.content[0].type === 'text' ? message.content[0].text : '';

  return `LLM-ENHANCED SUMMARY:\n\n${summary}`;
}

// Similarly for analysis
export async function analyzeContractLLM(text: string, focusAreas: string[]): Promise<string> {
  const message = await client.messages.create({
    model: "claude-sonnet-4-20250514",
    max_tokens: 2000,
    messages: [{
      role: "user",
      content: `Analyze this contract. Focus on: ${focusAreas.join(', ')}

Extract:
1. All parties involved
2. Key clauses and their implications
3. Potential risks or red flags
4. Payment terms
5. Termination conditions

Contract:
${text}`
    }]
  });

  return message.content[0].type === 'text' ? message.content[0].text : '';
}

// Real risk assessment with LLM
export async function assessRiskLLM(text: string): Promise<string> {
  const message = await client.messages.create({
    model: "claude-sonnet-4-20250514",
    max_tokens: 1500,
    messages: [{
      role: "user",
      content: `Assess the risk level of this contract. Provide:
1. Risk Level (LOW/MEDIUM/HIGH/CRITICAL)
2. Specific risk factors identified
3. Actionable recommendations
4. Financial risk assessment
5. Legal risk assessment

Return as JSON with this structure:
{
  "risk_level": "HIGH",
  "risk_score": 75,
  "risk_factors": ["factor1", "factor2"],
  "recommendations": ["rec1", "rec2"],
  "financial_risk": "description",
  "legal_risk": "description"
}

Contract:
${text}`
    }]
  });

  return message.content[0].type === 'text' ? message.content[0].text : '';
}
