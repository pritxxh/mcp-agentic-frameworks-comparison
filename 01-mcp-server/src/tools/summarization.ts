// Summarization tool implementation

export function summarizeContract(text: string, maxLength: number = 100): string {
  // Split into words
  const words = text.split(/\s+/).filter(word => word.trim().length > 0);

  // Extract first maxLength words
  const summary = words.slice(0, maxLength).join(' ');

  // Add statistics
  const totalWords = words.length;
  const summaryWords = Math.min(maxLength, totalWords);

  return `SUMMARY (${totalWords} words → ${summaryWords} words):

${summary}${totalWords > maxLength ? '...' : ''}

Key Statistics:
- Total contract length: ${totalWords} words
- Summary length: ${summaryWords} words
- Compression ratio: ${((summaryWords / totalWords) * 100).toFixed(1)}%`;
}
