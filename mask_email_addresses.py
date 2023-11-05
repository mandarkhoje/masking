import re
def mask_email_addresses(text):
 # Regular expression to match email addresses
 email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 # Function to mask each matched email
 def mask_email(match):
 email = match.group()
 local_part, domain_part = email.split('@')
 # Mask the local part and concatenate with the domain part
 masked_email = 'xxxxxxx' + '@' + domain_part
 return masked_email
 # Use the sub method to replace the local part of each email address
 masked_text = re.sub(email_regex, mask_email, text)
 return masked_text
# Example usage
original_text = "My email address is johndoe@example.com"
masked_text = mask_email_addresses(original_text)
print(masked_text)
