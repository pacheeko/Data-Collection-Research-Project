# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 18:00:04 2021

@author: bpach
"""

import datetime
import random

inputfile = "removedDuplicatesOutput.txt"
epsilon = 4000000
minNeighbours = 2000

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

def getNeighbours(matchData, fileIn):
    fileIn.seek(0)
    line = "notEmpty"
    neighbours = []
    while (line != ""):
        line = fileIn.readline()
        lineCut = line[1:]
        splitLine = lineCut.split(",")
        matchID = splitLine[0]
        matchTime = convertDatetimeToEpoch(convertMatchtimeToDatetime(splitLine[1]))
        if (abs(matchData[1]-matchTime) < epsilon):
            neighbours.append((matchID, matchTime))
    return neighbours
    

def DBSCAN1(filename):
    print("starting dbscan..")
    #Find the number of data points to cluster, then rewind the file to the beginning
    fileIn = open(filename, "r")
    numLines = sum(1 for line in fileIn)
    print("clustering " + str(numLines) + " data points")
    fileIn.seek(0)
    neighbourhoods = []
    clusters = []
    DataPointsSearched = {}
    
    #Get the initial data point: matchID and time in epochs
    initialPoint = random.randint(0, numLines)
    i = 0
    while i < initialPoint:
        line = fileIn.readline()
    cutLine = line[1:]
    splitLine = cutLine.split(",")
    initialMatchID = splitLine[0]
    initialMatchTime = convertDatetimeToEpoch(convertMatchtimeToDatetime(splitLine[1]))
    DataPointsSearched[initialMatchID] = True
    
    #Look through each data point and decide if it's in the neighbourhood of the initial point
    fileIn.seek(0)
    neighbourhoods.append([initialMatchID])
    line = "notEmpty"
    while (line != ""):
        line = fileIn.readline()
        lineCut = line[1:]
        splitline = lineCut.split(",")
        matchID = splitline[0]
        DataPointsSearched[matchID] = False
        matchTime = convertDatetimeToEpoch(convertMatchtimeToDatetime(splitLine[1]))
        if (abs(initialMatchTime-matchTime) < epsilon):
            neighbourhoods[0].append((matchID, matchTime))
    
    #If the neighbourhood of the initial point is less than the min neighbours, restart the clustering
    if (len(neighbourhoods[0]) < minNeighbours):
        fileIn.close()
        print("Initial point is not a core point, trying again..")
        DBSCAN1(filename)
        return
    
    #Otherwise, set that neighbourhood as the first cluster
    clusters.append(neighbourhoods[0])
    
    for item in neighbourhoods[0]:
        if DataPointsSearched[item] == False:
            DataPointsSearched[item] = True
            neighbours = getNeighbours(item, fileIn)
            if (neighbours)
            
DBSCAN1(inputfile)




