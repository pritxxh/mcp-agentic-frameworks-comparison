// Risk assessment tool implementation

export interface RiskAssessment {
  risk_level: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
  risk_score: number;
  risk_factors: string[];
  recommendations: string[];
  financial_risk: string;
  legal_risk: string;
}

export function assessRisk(text: string): RiskAssessment {
  let score = 0;
  const riskFactors: string[] = [];
  const recommendations: string[] = [];

  // Check for high-risk liability clauses
  if (text.toLowerCase().includes('unlimited liability')) {
    score += 30;
    riskFactors.push('UNLIMITED LIABILITY present - extreme financial exposure');
    recommendations.push('URGENT: Negotiate liability cap (e.g., 2-3x contract value)');
  }

  // Check for insurance requirements
  if (!text.toLowerCase().includes('insurance')) {
    score += 20;
    riskFactors.push('No insurance requirements - increased risk exposure');
    recommendations.push('Add insurance requirements (e.g., $1M E&O insurance)');
  }

  // Check for indemnification
  if (text.toLowerCase().includes('indemnif')) {
    score += 15;
    riskFactors.push('Indemnification clause present - potential liability transfer');
    recommendations.push('Review indemnification scope and mutual terms');
  }

  // Check for termination clause
  if (!text.toLowerCase().includes('termination')) {
    score += 15;
    riskFactors.push('No termination clause - difficult exit strategy');
    recommendations.push('Add termination clause with reasonable notice period');
  }

  // Check for payment terms
  if (text.toLowerCase().includes('net 90') || text.toLowerCase().includes('net 120')) {
    score += 10;
    riskFactors.push('Extended payment terms - cash flow risk');
    recommendations.push('Negotiate shorter payment terms (Net 30 or less)');
  }

  // Check for dispute resolution
  if (!text.toLowerCase().includes('arbitration') && !text.toLowerCase().includes('dispute')) {
    score += 10;
    riskFactors.push('No dispute resolution mechanism specified');
    recommendations.push('Add arbitration or mediation clause');
  }

  // Check for confidentiality
  if (!text.toLowerCase().includes('confidential')) {
    score += 5;
    riskFactors.push('No confidentiality provisions');
    recommendations.push('Add mutual confidentiality agreement');
  }

  // Check for data ownership/usage
  if (text.toLowerCase().includes('data') && !text.toLowerCase().includes('ownership')) {
    score += 10;
    riskFactors.push('Data mentioned but ownership unclear');
    recommendations.push('Clarify data ownership and usage rights');
  }

  // Check for auto-renewal
  if (text.toLowerCase().includes('auto-renew') || text.toLowerCase().includes('automatic renew')) {
    score += 5;
    riskFactors.push('Auto-renewal clause - may lock in unfavorable terms');
    recommendations.push('Ensure auto-renewal has reasonable opt-out period');
  }

  // Determine risk level
  let riskLevel: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
  if (score >= 70) {
    riskLevel = 'CRITICAL';
  } else if (score >= 50) {
    riskLevel = 'HIGH';
  } else if (score >= 30) {
    riskLevel = 'MEDIUM';
  } else {
    riskLevel = 'LOW';
  }

  // Assess specific risk categories
  const financialRisk = score >= 30
    ? 'HIGH - Significant financial exposure identified'
    : score >= 15
    ? 'MEDIUM - Moderate financial considerations'
    : 'LOW - Acceptable financial risk profile';

  const legalRisk = riskFactors.some(f => f.includes('UNLIMITED') || f.includes('indemnif'))
    ? 'HIGH - Legal review strongly recommended'
    : riskFactors.length > 3
    ? 'MEDIUM - Legal review recommended'
    : 'LOW - Standard legal protections advisable';

  // Add general recommendations
  if (score >= 50) {
    recommendations.unshift('⚠️ DO NOT SIGN without legal review');
  }
  if (riskFactors.length === 0) {
    recommendations.push('Conduct thorough review before signing');
  }

  return {
    risk_level: riskLevel,
    risk_score: score,
    risk_factors: riskFactors.length > 0 ? riskFactors : ['No major risk factors identified'],
    recommendations,
    financial_risk: financialRisk,
    legal_risk: legalRisk
  };
}
