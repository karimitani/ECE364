import re
from pprint import pprint as pp

"""
The following examples are from Google Developers Website:

https://developers.google.com/edu/python/regular-expressions
"""


"""
    Example 1: The idea
"""

expr = r"word:\w\w\w"
str = 'an example word:Cat!!'

match = re.search(expr, str)

# If-statement after search() tests if it succeeded
if match:
    print('found', "'" + match.group() + "'")  # 'found word:Dog'
else:
    print('did not find')


"""
    Example 2: Basics
"""

## Search for pattern 'iii' in string 'piiig'.
## All of the pattern must match, but it may appear anywhere.
## On success, match.group() is matched text.

match = re.search(r'iii', 'piiig')
print(match.group())

match = re.search(r'igs', 'piiig')
print(match)
# print(match.group())  => Error!

## . = any char but \n
match = re.search(r'..g', 'piXXg')
print(match.group())

# \d = digit char, \w = word char
match = re.search(r'\d{3}', 'p456123g')
print(match.group())

match = re.search(r'(\w\w\w)!', '@@abcd!!')
print(match.group())
print(match.group(1))

match = re.search(r'(\w\w\w)', '@@abcd!!')
print(match.group())
print(match.group(1))


"""
    Example 3: Repetitions
"""


# i+ = one or more i's, as many as possible.
match = re.search(r'pi+', 'piiig')
print(match.group())

## Finds the first/leftmost solution, and within it drive the +
## as far as possible (aka 'leftmost and largest').
match = re.search(r'(i+).(i+)', 'piigiiii')
print(match.group())
print(match.group(1))
print(match.group(2))


## \s* = zero or more whitespace chars
## Here look for 3 digits, possibly separated by whitespace.
pat = r'\d\s*\d\s*\d'
match = re.search(pat, 'xx1 2   3xx')
print(match.group())

match = re.search(pat, 'xx12  3xx')
print(match.group())

match = re.search(pat, 'xx123xx')
print(match.group())


## ^ = matches the start of string. (Does NOT match anything.)
match = re.search(r'b\w+', 'foobar')
if match:
    print(match.group())
else:
    print("Nothing found.")

## but without the ^ it succeeds:
match = re.search(r'^b\w+', 'foobar')
if match:
    print(match.group())
else:
    print("Nothing found.")


"""
    Example 4: Email
"""


str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)

if match:
    print(match.group())

match = re.search(r'\w+@\w+', str)
if match:
    print(match.group())

"""
    Example 5: Groups
"""

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search('(?P<user>[\w.-]+)@(?P<domain>[\w.-]+)', str)
if match:
    print(match.group())   # 'alice-b@google.com' (the whole match)
    print(match.group(1))  # 'alice-b' (the username, group 1)
    print(match.group(2))  # 'google.com' (the host, group 2)
    print(match.group("domain"))  # 'google.com'

    pp(match.groupdict())

# # Nested groups.
# match = re.search('\s(?P<complete>(?P<user>[\w.-]+)@(?P<domain>[\w.-]+)\s)', str)
# if match:
#     print("'{}'".format(match.group()))   # (the whole match)
#     pp(match.groupdict())
#
"""
    Example 6: Find All
"""

# Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

# Here re.findall() returns a list of all the found email strings.
emails = re.findall(r'([\w.-]+)@([\w.-]+)', str)

for email in emails:
    # do something with each found email string
    print(email)

# # Nested groups.
# str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
# emails = re.findall(r'(([\w.-]+)@([\w.-]+))', str)
# for email in emails:
#     print(email)

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
resultTuples = re.findall(r'([\w.-]+)@([\w.-]+)', str)
print(resultTuples)

for address, domain in resultTuples:
    print("Address: '{0}' and domain: '{1}'".format(address, domain))

"""
    Example 6: Substitution
"""

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## re.sub(pat, replacement, str) -- returns new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement

print(str)
print(re.sub(r'([\w.-]+)@([\w.-]+)', r'\2@\1', str))
## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher

