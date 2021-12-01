# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 14:40:40 2021

@author: bpach
"""

# Selects a random player from the region, tier, and division selected and outputs the match history to the filename given
# formatted as such (matchID, creationTime, region, division, red, redTeamOutcome, redChampion1, redChampion2, redChampion3, 
# redChampion4, redChampion5, blue, blueTeamOutcome, blueChampion1, blueChampion2, blueChampion3, blueChampion4, blueChampion5)

#Version 2 of getMatchData. Instead of inputting values for tier, division, and region, keep adding data to the output file
#until time is up, choosing a new set of matches each time it's done parsing
import random
from time import time
import cassiopeia as cass

def getAPI_key():
    f = open("api_key.txt", "r")
    return f.read()

def getRandRegion():
    index = random.randint(0,2)
    if index == 0:
        return "NA"
    elif index == 1:
        return "EUW"
    elif index == 2:
        return "BR"
    return "bad region"

def getRandTier():
    index = random.randint(0, 3)
    if index == 0:
        return "DIAMOND"
    elif index == 1:
        return "PLATINUM"
    elif index == 2:
        return "GOLD"
    elif index == 3:
        return "SILVER"
    return "bad tier"

def getRandDivision(tier):
    index = random.randint(0,3)
    if index == 0:
        return "I"
    elif index == 1:
        return "II"
    elif index == 2:
        return "III"
    elif index == 3:
        return "IV"
    return "bad division"

# Choose one: DIAMOND, PLATINUM, GOLD, SILVER

# Choose one: I, II, III, IV

# Choose one: NA, KR, EUW

#------------------------------------------------------------------------------------------------------------------------------------
queueVar = "RANKED_SOLO_5x5"
beginTimeVar = 1623788842
ten_minutes = 600
end = time() + ten_minutes
fileName = "matchData.txt"
#while time() < end:  
while True:
    regionVar = getRandRegion()
    tierVar = getRandTier()
    divisionVar = getRandDivision(tierVar)
    
    if (regionVar == "NA" or regionVar == "BR"):
        continentVar = "AMERICAS"
    elif (regionVar == "EUW"):
        continentVar = "EUROPE"
    else:
        continentVar = "bad continent"
        
    cass.set_riot_api_key(getAPI_key())  # This overrides the value set in your configuration/settings.
    
    leaguePlayers = cass.get_paginated_league_entries(queue = queueVar, tier = tierVar, division = divisionVar, region = regionVar)[:200]
    
    index = random.randint(0,200)
    if (len(leaguePlayers) < index):
        index = len(leaguePlayers)/2
    #print("Summoner ID: {sID}".format(sID=leaguePlayers[0].summonerId))
    player = leaguePlayers[index].summoner
    
    matches = cass.get_match_history(continent=continentVar, puuid = player.puuid, queue = queueVar, begin_time = beginTimeVar, end_index=100)
    
    #Write match numbers to a file
    f = open(fileName, "a")
    for match in matches:
         m = cass.Match(id = match.id, region = regionVar)
         redTeam = []
         blueTeam = []
         for p in m.participants:
             if (p.side == cass.Side(100)): 
                 blueTeam.append(p.champion.name)
             else:
                 redTeam.append(p.champion.name)
        
         if (m.red_team().win):
             red = "win"
             blue = "lose"
         else:
             red = "lose"
             blue = "win"
             
         output = "(" + str(m.id) + "," + str(m.creation) + "," + regionVar + "," + tierVar + "," + "red," + red + ","
         for champion in redTeam:
             output = output + champion
             output = output + ","
         
         output = output + "blue," + blue + ","
         
         for champion in blueTeam:
             output = output + champion
             output = output + ","
             
         output = output[0:-1] + ")\n"
         print(output)
         f.write(output)        
    
    f.close()
    print("Seconds left: " + str(end-time()))
    