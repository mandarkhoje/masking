import re
def redact_emails(text):
 # Regular expression to match email addresses
 email_pattern = r'[\w\.-]+@[\w\.-]+'
 # Replacement pattern
 replacement = "[REDACTED EMAIL]"
 # Redact the emails
 redacted_text = re.sub(email_pattern, replacement, text)
 return redacted_text
# Example usage
text_with_emails = "Please contact us at support@example.com for assistance."
redacted_text = redact_emails(text_with_emails)
print(redacted_text)
