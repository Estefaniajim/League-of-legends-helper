import requests
import json
import os
from dotenv import load_dotenv
import pandas as pd
import pickle
import time

# Getting the api key from .env
load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
# Getting the data from a json file to a string
while True:
    try:
        matchesID = pickle.load(open("matchesId.p", "rb"))
        break
    except:
        matchData = requests.get('http://canisback.com/matchId/matchlist_na1.json')
        matchesID = json.loads(matchData.text)
        break
while True:
    try:
        matchesData = pickle.load(open("matchesData.p", "rb"))
        break
    except:
        matchesData = pd.DataFrame()
        break
print("All ready to go...")

def getMatchID(matchesData):
    for matchID in matchesID.copy():
        while True:
            try:
                print("\tGetting info for match " + str(matchID), end = '')
                matchesData = matchesData.append(getInfoWithMatchID(matchID))
                print(".", end='')
                matchesID.remove(matchID)
                print(".", end='')
                pickle.dump( matchesID, open( "matchesId.p", "wb" ))
                print(".", end='')
                pickle.dump( matchesData, open( "matchesData.p", "wb" ))
                print("Done")
                break
            except:
                print(" ERROR - Waiting 61 segs")
                time.sleep(64)
                print("Trying again")



def getRankedPosition(accountId):
    URL = "https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + str(accountId) + "?api_key=" + str(API_KEY)
    info = requests.get(URL)
    info = json.loads(info.text)
    while True:
        try:
            tier = str(info[0]["tier"])
            rank = str(info[0]["rank"])
            return tier,rank
        except:
            tier = "Unranked"
            rank = 0
            return tier,rank

def getInfoWithMatchID(matchID):
    URL = "https://na1.api.riotgames.com/lol/match/v4/matches/" + str(matchID) + "?api_key=" + str(API_KEY)
    info = requests.get(URL)
    info = json.loads(info.text)
    df = pd.DataFrame()
    for x in range(10):
        teamID = 0 if info["participants"][x]["teamId"] == 100 else 1
        if info["teams"][teamID]["win"] == "Win":
            SummonerID = info["participantIdentities"][x]["player"]["summonerId"]
            kills = info["participants"][x]["stats"]["kills"]
            deaths = info["participants"][x]["stats"]["deaths"]
            assists = info["participants"][x]["stats"]["assists"]
            goldEarned = info["participants"][x]["stats"]["goldEarned"]
            wardsPlaced = info["participants"][x]["stats"]["wardsPlaced"]
            wardskilled = info["participants"][x]["stats"]["wardsKilled"]
            creepsPerMin = info["participants"][x]["timeline"]["creepsPerMinDeltas"]["0-10"]
            goldPerMin = info["participants"][x]["timeline"]["goldPerMinDeltas"]["0-10"]
            lane = info["participants"][x]["timeline"]["lane"]
            tier,rank = getRankedPosition(SummonerID)
            data = pd.Series({"lane": lane,
                                "tier": tier,
                                "rank": rank,
                                "creepsPerMin": creepsPerMin,
                                "goldPerMin": goldPerMin,
                                "kills": kills,
                                "deaths": deaths,
                                "assists":assists,
                                "goldEarned":goldEarned,
                                "wardsPlaced":wardsPlaced,
                                "wardsKilled":wardskilled})
            df = df.append(data,ignore_index=True)
    return df

#print(getMatchID(matchesData))
#print(getInfoWithMatchID(3504621987))
#print(len(matchesID))
#print(matchesData.info())

