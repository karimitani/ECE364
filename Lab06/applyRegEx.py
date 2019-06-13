import sys
import os
import re
import collections

file = "SiteRegistration.txt"
main_dict={} ## stores all the infor-->key is person's name
name=""
num=""
new_num=""

## making a dictionary with all the info for all the people in the file
with open(file,'r') as f:
    for line in f.readlines():
        num=""
        new_num=""
        line = line.replace('\n',"")
        info = re.search(r"^(\w+[,]?\s)(\w+)[,;\s]*([[a-z][\w\._]*@*[\w\.]*]*)[,;\s]*([\d*\-*\(?\)?\s*]*)[,;\s]*([\w\s*]*)$", line)
        if(info.group(4) != ""):
            num=info.group(4)
            num = num.replace('-','')
            num = num.replace('(','')
            num = num.replace(')','')
            num = num.replace(' ','')
            new_num += "(" + num[0:3] + ")" + " " + num[3:6] + "-" + num[6:10]
            #print(new_num)

        if(re.search(r",",info.group(1)) == None):
            name += info.group(1) + info.group(2)
            if(len(info.group(3)) == 1):
                name += info.group(3)
                main_dict[name] = ("",new_num,info.group(5))
            else:
                main_dict[name] = (info.group(3),new_num,info.group(5))

        else:
            name += info.group(2)
            if(len(info.group(3)) == 1):
                name += info.group(3)
                name += " " + info.group(1).replace(', ','')
                main_dict[name] = ("",new_num,info.group(5))
            else:
                 name += " " + info.group(1).replace(', ','')
                 main_dict[name] = (info.group(3),new_num,info.group(5))

        name=""

    print(main_dict)

def getRejectedUsers():
    name_list=[]
    flag=0
    for key,value in main_dict.items():
        for item in value:
            if (item == ""):
                continue
            else:
                flag=1
        if(flag == 0):
            name_list.append(key)
        flag=0
    name_list.sort()
    return name_list


def getUsersWithCompleteInfo():
    result={}
    flag = 0
    for key,value in main_dict.items():
        for item in value:
            if(item != ""):
                continue
            else:
                flag=1
        if(flag==0):
            result[key] = value
        flag = 0

    return result

def getUsersWithEmails():
    result={}
    for key,value in main_dict.items():
        if (value[0] == ""):
            continue
        else:
            result[key] = value[0]
    #print(result)
    return result


def getUsersWithPhones():
    result={}
    for key,value in main_dict.items():
        if (value[1] == ""):
            continue
        else:
            result[key] = value[1]
    #print(result)
    return result

def getUsersWithStates():
    result={}
    for key,value in main_dict.items():
        if (value[2] == ""):
            continue
        else:
            result[key] = value[2]
    #print(result)
    return result

def getUsersWithoutEmails():
    rejected_users = getRejectedUsers()
    result=[]
    for key,value in main_dict.items():
        if (value[0] != ""):
            continue
        elif (key not in rejected_users):
            result.append(key)
    result = sorted(result)
    #print(result)
    return result


def getUsersWithoutPhones():
    rejected_users = getRejectedUsers()
    result=[]
    for key,value in main_dict.items():
        if (value[1] != ""):
            continue
        elif (key not in rejected_users):
            result.append(key)
    result = sorted(result)
    #print(result)
    return result


def getUsersWithoutStates():
    rejected_users = getRejectedUsers()
    result=[]
    for key,value in main_dict.items():
        if (value[2] != ""):
            continue
        elif (key not in rejected_users):
            result.append(key)
    result = sorted(result)
    #print(result)
    return result
