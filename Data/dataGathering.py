import requests
import json
import os
from dotenv import load_dotenv
import pandas as pd

# Getting the api key from .env
load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
print(APIKey)
# Getting the data from a json file to a string
matchData = requests.get('http://canisback.com/matchId/matchlist_na1.json')
matchesID = json.loads(matchData.text)

def getMatchID():
    for matchID in matchesID:
        getInfoWithMatchID(matchID)

def getInfoWithMatchID(matchID):
    print(matchID)
    URL = "https://na1.api.riotgames.com/lol/match/v4/matches/" + str(matchID) + "?api_key=" + str(APIKey)
    info = requests.get(URL)
    return info

print(getInfoWithMatchID(matchesID[1]))


