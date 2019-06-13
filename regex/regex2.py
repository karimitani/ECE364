import re
from pprint import pprint as pp

# Exact Match.
s = "Today is Monday. Tomorrow is Tuesday"
pp(s.find("Tuesday"))

# Motivation.
s = "Mary is scheduled for Feb 1st, and Lisa for Feb 3rd."
pattern = r"(\dst|\dnd|\drd)"
multiple = re.findall(pattern, s)
pp(multiple)

# OR-ing Options.
s = "Today is Monday. Tomorrow is Tuesday"
pattern = r"(Friday|Sunday|Monday|Tuesday)"

single = re.search(pattern, s)
pp(single.group(1))

multiple = re.findall(pattern, s)
pp(multiple)

# Grouping.
s = "The side fell off during the ride. Let's hide!!"
single = re.search(r"(([f\-asrh])ide)", s)
pp(single.group(1))

multiple = re.findall(r"((s|r|h)ide)", s)
pp(multiple)

# Quantifiers.
s = "4 / 3 = 1.33333333333"
single = re.search(r"(1\.\|3?)", s)
pp(single.group(1))

single = re.search(r"(1\.3*)", s)
pp(single.group(1))

single = re.search(r"(1\.3{5})", s)
pp(single.group(1))

# Sets
s = "It is 55.9 and not 31.222."
single = re.search(r"([0-9]{2}\.[0-9]{2,})", s)
pp(single.group(1))

single = re.search(r"([^0-3]{2}\.[0-9]+)", s)
pp(single.group(1))

# The Dot & Symbols.
s = "It is 55.9 and not 31.222."
single = re.search(r"(\d{2}\.\d{2,})", s)
pp(single.group(1))

s = "It is 55.19 and not AC.222."
single = re.search(r"(.{2}\.\d{2,})", s)
pp(single.group(1))

multiple = re.findall(r"(.{2}\.\d{2,})", s)
pp(multiple)