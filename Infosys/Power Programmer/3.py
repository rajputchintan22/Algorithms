import re
r1 = re.findall("[a-z]+[a-z0-9:]*/[a-z0-9]+\([a-z]+)]", "abc:/b1cabc")
print(r1)