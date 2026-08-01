// Notification tool implementation

export function sendNotification(
  recipient: string,
  subject: string,
  message: string,
  priority: 'LOW' | 'MEDIUM' | 'HIGH' = 'MEDIUM'
): string {
  // Simulated notification (in production, this would send actual emails)
  const timestamp = new Date().toISOString();

  // Log to stderr for debugging (stdout is used by MCP protocol)
  console.error(`[NOTIFICATION ${timestamp}] To: ${recipient}, Priority: ${priority}`);

  // Priority-based formatting
  const priorityEmoji = {
    LOW: '📋',
    MEDIUM: '📧',
    HIGH: '🚨'
  };

  const priorityLabel = {
    LOW: '[INFO]',
    MEDIUM: '[NOTICE]',
    HIGH: '[URGENT]'
  };

  // Format the notification
  const notification = `
${priorityEmoji[priority]} NOTIFICATION SENT ${priorityLabel[priority]}

To: ${recipient}
Subject: ${subject}
Priority: ${priority}
Timestamp: ${timestamp}

Message:
${message}

---
Status: ✅ Successfully queued for delivery
Note: This is a simulated notification. In production, this would send via email/SMS.
`;

  return notification.trim();
}
