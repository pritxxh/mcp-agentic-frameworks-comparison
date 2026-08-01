// Contract analysis tool implementation

export interface AnalysisResult {
  total_clauses: number;
  key_terms: string[];
  focus_analysis: Record<string, string>;
  warnings: string[];
  parties: string[];
}

export function analyzeContract(
  text: string,
  focusAreas: string[] = []
): AnalysisResult {
  // Detect clauses (paragraphs or numbered sections)
  const clauses = text.split(/\n\n+/).filter(c => c.trim().length > 0);

  // Extract key terms (words in all caps or quoted phrases)
  const capsTerms = text.match(/\b[A-Z]{2,}\b/g) || [];
  const quotedTerms = text.match(/"[^"]+"/g) || [];
  const allTerms = [...new Set([...capsTerms, ...quotedTerms])];
  const keyTerms = allTerms.slice(0, 10); // Top 10 terms

  // Extract parties (common patterns)
  const partyPatterns = [
    /(?:between|by and between)\s+([A-Z][^\n,]+?)(?:\s+and\s+|\s*\()/gi,
    /(?:Provider|Client|Company|Consultant|Party [AB]):\s*([A-Z][^\n]+)/gi
  ];
  const parties: string[] = [];
  for (const pattern of partyPatterns) {
    const matches = text.matchAll(pattern);
    for (const match of matches) {
      if (match[1]) parties.push(match[1].trim());
    }
  }

  // Focus area analysis
  const focusAnalysis: Record<string, string> = {};
  for (const area of focusAreas) {
    const regex = new RegExp(area, 'gi');
    const mentions = (text.match(regex) || []).length;

    // Find relevant clauses
    const relevantClauses = clauses.filter(clause =>
      clause.toLowerCase().includes(area.toLowerCase())
    );

    focusAnalysis[area] = `Found ${mentions} mentions of "${area}". ${
      relevantClauses.length > 0
        ? `Appears in ${relevantClauses.length} clause(s).`
        : 'No dedicated clause found.'
    }`;
  }

  // Generate warnings based on common red flags
  const warnings: string[] = [];

  if (text.toLowerCase().includes('unlimited liability')) {
    warnings.push('⚠️ CRITICAL: Unlimited liability clause detected');
  }

  if (!text.toLowerCase().includes('termination')) {
    warnings.push('⚠️ WARNING: No termination clause found');
  }

  if (!text.toLowerCase().includes('insurance')) {
    warnings.push('⚠️ WARNING: No insurance requirements specified');
  }

  if (text.toLowerCase().includes('indemnif')) {
    warnings.push('⚠️ NOTICE: Indemnification clause present - review carefully');
  }

  if (!text.toLowerCase().includes('confidential')) {
    warnings.push('⚠️ NOTICE: No confidentiality clause found');
  }

  return {
    total_clauses: clauses.length,
    key_terms: keyTerms,
    focus_analysis: focusAnalysis,
    warnings,
    parties: [...new Set(parties)]
  };
}
