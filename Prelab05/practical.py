#! /usr/local/bin/python 3.4

import sys
import os
import math

def getFreeByName(names):
    result = {}
    for keys in names:
        with open('Availability.txt','r') as myFile:
            lines = myFile.readlines()
            dates = lines[1].split()
            for i in range(3,len(lines)):
                info = lines[i].replace('|',',').split(',')
                for j in range(len(info)):
                    info[j] = info[j].strip()
                name = info[0]+", "+info[1]
                for k in range(2,len(info)):
                    if info[k] == "1" and name == keys:
                        if name not in result:
                            availabledate = []
                            availabledate.append(dates[k])
                            result[name] = availabledate
                        else:
                            result[name].append(dates[k])

    return result

def getFreeByRange(date1, date2):
    with open('Availability.txt','r') as myFile:
        lines = myFile.readlines()
        dates = lines[1].split()
        col1 = 0
        col2 = 0
        names = []
        for i in range(2,len(dates)):
            if dates[i] == date1:
                col1 = i
            if dates[i] == date2:
                col2 = i
        for j in range(3,len(lines)):
            info = lines[j].replace('|',',').split(',')
            notchange = 0
            for k in range(len(info)):
                info[k] = info[k].strip()
            for l in range(col1,col2+1):
                if info[l] == "0":
                    notchange = 1
            if notchange == 0:
                names.append(info[0]+", "+info[1])
        print(set(names))



def getStatebyCounty(county):
    latitude = []
    longitude = []
    with open('Counties.txt','r')as myCounty:
        lines = myCounty.readlines()
        for i in range(2,len(lines)):
            info = lines[i].split()
            if info[2].strip() == county:
                latitude.append(info[0].strip())
                longitude.append(info[1].strip())
    with open('LatLong.txt','r')as myLatLong:
        lines = myLatLong.readlines()
        for j in range()



if __name__ == "__main__":
    getFreeByName({'Sang, Chanell', 'Chock, Velvet'})

    getFreeByRange("08/08","08/12")