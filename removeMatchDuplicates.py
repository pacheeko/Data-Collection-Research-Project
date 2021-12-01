# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 14:20:36 2021

@author: bpach
"""

#File to remove duplicate matches from
InputFilename = "matchData.txt"
OutputFilename = "removedDuplicatesOutput.txt"

matchIDs = []

fileIn = open(InputFilename, "r")
fileOut = open(OutputFilename, "w")

line = "notempty"
while (line != ""):
    line = fileIn.readline()
    lineCut = line[1:]
    splitline = lineCut.split(",")
    matchID = splitline[0]
    if (matchID not in matchIDs):
        matchIDs.append(matchIDs)
        fileOut.write(line)
        
