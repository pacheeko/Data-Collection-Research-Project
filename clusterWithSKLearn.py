# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 16:02:07 2021

@author: bpach
"""

import numpy as np
from sklearn.cluster import DBSCAN
import datetime

inputFile = "removedDuplicatesOutput.txt"

epsilon = 1000000
minNeighbours = 1000

testEpoch = 1623715100
dt = datetime.datetime(2021, 6, 15, 0, 0)
testMatchTime = "2021-11-02T06:15:27+00:00"

def convertEpochToDatetime(epoch):
    return datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%dT%H:%M:%S+00:00')
    
def convertDatetimeToEpoch(time):
    return (time - datetime.datetime(1970, 1, 1)).total_seconds()
    
def convertMatchtimeToDatetime(matchTime):
    year = int(matchTime[0:4])
    month = int(matchTime[5:7])
    day = int(matchTime[8:10])
    hour = int(matchTime[11:13])
    minutes = int(matchTime[14:16])
    seconds = int(matchTime[17:19])
    return datetime.datetime(year, month, day, hour, minutes, seconds)
    
def convertDatetimeToMatchtime(time):
    monthStr = str(time.month)
    dayStr = str(time.day)
    hourStr = str(time.hour)
    minuteStr = str(time.minute)
    secondStr = str(time.second)
    if (len(monthStr) == 1):
        monthStr = "0" + monthStr
        
    if (len(dayStr) == 1):
        dayStr = "0" + dayStr
    if (len(hourStr) == 1):
        hourStr = "0" + hourStr
        
    if (len(minuteStr) == 1):
        minuteStr = "0" + minuteStr
    
    if (len(secondStr) == 1):
        secondStr = "0" + secondStr
    
    return str(time.year) + "-" + monthStr + "-" + dayStr + "T" + hourStr + ":" + minuteStr + ":" + secondStr + "+00:00"
    

#print(convertEpochToDatetime(testEpoch))
#print(round(convertDatetimeToEpoch(dt)))
#print(convertMatchtimeToDatetime(testMatchTime))
#print(convertDatetimeToMatchtime(dt))
def getNumFromTier(tier):
    if (tier == "DIAMOND"):
        return 0
    elif (tier == "PLATINUM"):
        return 1
    elif (tier == "GOLD"):
        return 2
    elif (tier == "SILVER"):
        return 3
    else:
        return 4


arr = []
fileIn = open(inputFile, "r")
line = "notEmpty"
while (line != ""):
    line = fileIn.readline()
    lineCut = line[1:]
    splitLine = lineCut.split(",")
    if (len(splitLine) > 1):
        matchTime = convertDatetimeToEpoch(convertMatchtimeToDatetime(splitLine[1]))
        
        arr.append([matchTime, getNumFromTier(splitLine[3])])
 
npArray = np.asarray(arr)
clustering = DBSCAN(eps=epsilon, min_samples=minNeighbours).fit(npArray)
print(*clustering.labels_)


