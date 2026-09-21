import re

# Sample text
text = """
Contact us at student@gmail.com
or admin@college.edu.
You can also email support123@yahoo.com.
"""

# Regular expression pattern for email
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Find all email addresses
emails = re.findall(pattern, text)

# Display the results
print("Email addresses found:")

for email in emails:
    print(email)