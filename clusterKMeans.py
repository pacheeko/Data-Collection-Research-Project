# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 20:22:38 2021

@author: bpach
"""

import numpy as np
import datetime
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

inputFile = "removedDuplicatesOutput.txt"
c1Output = "cluster1.txt"
c2Output = "cluster2.txt"
c3Output = "cluster3.txt"


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
        arr.append([matchTime])
 
#getNumFromTier(splitLine[3])
npArray = np.asarray(arr)
#data_scaler = StandardScaler().fit(arr)
#arr = data_scaler.transform(arr)
#print(*arr)

clustering = KMeans(n_clusters=3).fit(arr)
zeros = 0
ones = 0
twos = 0
threes = 0
fours = 0

for label in clustering.labels_:
    if (label == 0):
        zeros += 1
    elif (label == 1):
        ones += 1
    elif (label == 2):
        twos += 1
    elif (label == 3):
        threes += 1
    else:
        fours += 1
        
        
print("0s: " + str(zeros) + " 1s: " + str(ones) + " 2s: " + str(twos) + " 3s: " + str(threes) + " 4s: " + str(fours))
cluster1 = convertEpochToDatetime(int(clustering.cluster_centers_[0]))
cluster2 = convertEpochToDatetime(int(clustering.cluster_centers_[1]))
cluster3 = convertEpochToDatetime(int(clustering.cluster_centers_[2]))
#cluster4 = convertEpochToDatetime(int(clustering.cluster_centers_[3]))
#cluster5 = convertEpochToDatetime(int(clustering.cluster_centers_[4]))
print("Cluster 0: " + cluster1)
print("Cluster 1: " + cluster2)
print("Cluster 2: " + cluster3)
#print("Cluster 3: " + cluster4)
#print("Cluster 4: " + cluster5)
print("Iterations: " + str(clustering.n_iter_))
print("Deviation from cluster centroids: " + str(clustering.inertia_))
    
fileIn.seek(0)
c1 = open(c1Output, "w")
c2 = open(c2Output, "w")
c3 = open(c3Output, "w")
line = "notEmpty"
it = 0
while (it < 20634):
    line = fileIn.readline()
    cluster = clustering.labels_[it]
    it += 1
    if (cluster == 0):
        c1.write(line)
    elif (cluster == 1):
        c2.write(line)
    else:
        c3.write(line)

fileIn.close()
c1.close()
c2.close()
c3.close()

    
    
    