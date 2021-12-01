# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 18:00:04 2021

@author: bpach
"""

import time
import datetime

finished = False
cluster1 = "cluster1.txt"
cluster2 = "cluster2.txt"
cluster3 = "cluster3.txt"

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
print(convertDatetimeToMatchtime(dt))