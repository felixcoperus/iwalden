import re
s = ". pik, PIK pikken"
p = re.compile('\b(pik)\b')

p1 = r'\b(pik)\b'

print(re.findall(p1, s, re.IGNORECASE))