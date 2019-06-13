import os
import sys
import re

def email_edit(file):
    with open(file,'r') as f:
        for line in f:
            if(re.search(r"purdue\.edu",line) and "ecn" not in line):
                line=re.sub(r'(purdue\.edu)',r'ecn.\1',line)
                line=re.sub(r"\d$","0/100",line)
            else:
                line=re.sub(r"\d$","0/100",line)
            print(line)

email_edit("Part2.in")