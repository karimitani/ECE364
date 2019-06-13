#! /usr/bin/env python3.4
import sys
import os
import re
def parseSimple(fileName):
    filedir = "labfiles/"+fileName
    with open(filedir, 'r') as myFile:
        result = {}
        lines = myFile.readlines()
        for i in lines:
            m = re.search(r"\"(?P<key>[\w]+)\"\s?\:\s?\"(?P<val>[\w.\-\,\s\#]+)\"",i)
            if m:
                result[m.group("key")] = m.group("val")
            else:
                pass
        return result

def parseLine(fileName):
    filedir = "labfiles/"+fileName
    with open(filedir, 'r') as myFile:
        result = {}
        lines = myFile.readlines()
        find = re.findall(r"\"(?P<key>[\w.-]+)\"\s?\:\s?\"(?P<val>[\w.\-\,\s\#]+)\"",lines[0])
        for i in find:
            result[i[0]] = i[1]
        return result


def parseComplex(fileName):
    filedir = "labfiles/"+fileName
    with open(filedir, 'r') as myFile:
        result = {}
        lines = myFile.readlines()
        for i in lines:
            m = re.search(r"\"(?P<key>[\w.-]+)\"\s?\:\s?\"?(?P<val>[\w.\-\s\#]+)\"?",i)
            if m:
                if m.group("val") == "true":
                    result[m.group("key")] = True
                elif m.group("val") == "false":
                    result[m.group("key")] = False
                else:
                    value = re.sub(r"\n","",m.group("val"))
                    result[m.group("key")] = value
            else:
                pass
        return result


def parseComposite(fileName):
    filedir = "labfiles/"+fileName
    with open(filedir, 'r') as myFile:
        result = {}
        lines = myFile.readlines()
        for i in lines:
            m = re.search(r"\"(?P<key>[\w.-]+)\"\s?\:\s?\"?(?P<val>[\w.\-\s\#\[\]]+)\"?",i)
            if m:
                if m.group("val") == "true":
                    result[m.group("key")] = True
                elif m.group("val") == "false":
                    result[m.group("key")] = False
                else:
                    value = re.sub(r"\n","",m.group("val"))
                    result[m.group("key")] = value
            else:
                pass
        return result

if __name__ == "__main__":
    print(parseSimple("simple.json"))
    print(parseLine("simple2.json"))
    print(parseComplex("complex.json"))
    print(parseComposite("composite.json"))