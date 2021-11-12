# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:45:09 2021

@author: bpach
"""
# Selects a random player from the region, tier, and division selected and outputs the match history
# formatted as such (matchID, creationTime, region, division, red, redTeamOutcome, redChampion1, redChampion2, redChampion3, 
# redChampion4, redChampion5, blue, blueTeamOutcome, blueChampion1, blueChampion2, blueChampion3, blueChampion4, blueChampion5)

import random

import cassiopeia as cass

def getAPI_key():
    f = open("api_key.txt", "r")
    return f.read()

# Choose one: CHALLENGER, GRANDMASTER, MASTER, DIAMOND PLATINUM, GOLD, SILVER, BRONZE, IRON
tierVar = "GOLD"

# Choose one: I, II, III, IV
divisionVar = "I"

# Choose one: NA, KR, EU, ...
regionVar = "NA"

#------------------------------------------------------------------------------------------------------------------------------------
queueVar = "RANKED_SOLO_5x5"
beginTimeVar = 1623788842

if (regionVar == "NA"):
    continentVar = "AMERICAS"
elif (regionVar == "EU"):
    continentVar = "EUROPE"
else:
    continentVar = "ASIA"
    
cass.set_riot_api_key(getAPI_key())  # This overrides the value set in your configuration/settings.

leaguePlayers = cass.get_paginated_league_entries(queue = queueVar, tier = tierVar, division = divisionVar, region = regionVar)

index = random.randint(0,10000)


#print("Summoner ID: {sID}".format(sID=leaguePlayers[0].summonerId))
player = leaguePlayers[index].summoner

matches = cass.get_match_history(continent=continentVar, puuid = player.puuid, queue = queueVar, begin_time = beginTimeVar)

#Write match numbers to a file
fileName = player.puuid[0:20] + ".txt"
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
     
     f.write(output)        

f.close()