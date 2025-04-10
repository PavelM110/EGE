import re

text = "AB AC DC BB CA AD"

pattern = r'((?<!A)\w){2}'
match = re.findall(pattern, text)

for i in match:
    print(i)