# League of legends match data analysis

We collected league of legends game data through the riot api. 
The script 'getMatchData' selects a random player from the region, tier, and division that can be set
inside in the script. The script will output game data from the player in the following format: 

(matchID, creationTime, region, division, red, redTeamOutcome, redChampion1, redChampion2, redChampion3, redChampion4, 
 redChampion5, blue, blueTeamOutcome, blueChampion1, blueChampion2, blueChampion3, blueChampion4, blueChampion5).

There is example data in the file 'LXqOb-Gg6sDhr_ZNmVNr.txt'. The filename is the first 20 digits of the puuid, 
which is the encrypted id of the randomly selected player. The script was created using the anaconda distribution
platform and the spyder IDE. The cassiopeia library is required to run the script, and can be installed using
'pip install cassiopeia'. The link to the cassiopeia repository and documentation is: 

https://github.com/meraki-analytics/cassiopeia

https://cassiopeia.readthedocs.io/en/latest/cassiopeia/index.html#methods-and-class-constructors

NOTE: The api_key has to be regenerated every 24 hours. A new API key can be acquired by making an account 
      through https://developer.riotgames.com/.
