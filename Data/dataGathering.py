import requests
import json
import os
from dotenv import load_dotenv
import pandas as pd

# Getting the api key from .env
load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
# Getting the data from a json file to a string
matchData = requests.get('http://canisback.com/matchId/matchlist_na1.json')
matchesID = json.loads(matchData.text)
pdata = pd.DataFrame(pd.DataFrame({"kills":[],
                      "deaths":[],
                      "assists":[],
                      "creepsPerMin":[],
                      "goldPerMin":[],
                      "lane":[],
                      "tier":[],
                      "rank":[]}))

def getMatchID():
    for matchID in matchesID:
        getInfoWithMatchID(matchID)

def getRankedPosition(accountId):
    URL = "https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + str(accountId) + "?api_key=" + str(API_KEY)
    info = requests.get(URL)
    info = json.loads(info.text)
    while True:
        try:
            tier = info[0]["tier"]
            rank = info[0]["rank"]
            return tier,rank
        except:
            tier = "Unranked"
            rank = 0
            return tier,rank

def getInfoWithMatchID(matchID):
    URL = "https://na1.api.riotgames.com/lol/match/v4/matches/" + str(matchID) + "?api_key=" + str(API_KEY)
    info = requests.get(URL)
    info = json.loads(info.text)
    for x in range(10):
        accountId = info["participantIdentities"][x]["player"]["accountId"]
        kills = info["participants"][x]["stats"]["kills"]
        deaths = info["participants"][x]["stats"]["deaths"]
        assists = info["participants"][x]["stats"]["assists"]
        creepsPerMin = info["participants"][x]["timeline"]["creepsPerMinDeltas"]["10-20"]
        goldPerMin = info["participants"][x]["timeline"]["goldPerMinDeltas"]["10-20"]
        lane = info["participants"][x]["timeline"]["lane"]
        tier,rank = getRankedPosition(accountId)
        print(accountId)
        pdata.append(pd.DataFrame({"kills":[kills],
                      "deaths":[deaths],
                      "assists":[assists],
                      "creepsPerMin":[creepsPerMin],
                      "goldPerMin":[goldPerMin],
                      "lane":[lane],
                      "tier":[tier],
                      "rank":[rank]}))
# getInfoWithMatchID(3501821963)
# print(pdata.head())

