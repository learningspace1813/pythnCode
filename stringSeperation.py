#----------------------------------------
import re

text = "Youraj is a no. 1 cricketer. scored 10000runs and 345wickets."

# \d+ matches one or more digits
numbers = re.findall(r'\d+', text)

# Join the numbers with comma
output = ", ".join(numbers)
print(output)  # Output: 1, 10000, 345
