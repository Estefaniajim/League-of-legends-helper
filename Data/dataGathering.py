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
                print("\tGetting info for match " + str(matchID), end='')
                matchesData = matchesData.append(getInfoWithMatchID(matchID))
                print(".", end='')
                matchesID.remove(matchID)
                print(".", end='')
                pickle.dump(matchesID, open("matchesId.p", "wb"))
                print(".", end='')
                pickle.dump(matchesData, open("matchesData.p", "wb"))
                print("Done")
                break
            except:
                print(" ERROR - Waiting 120 segs")
                time.sleep(120)
                print("Trying again")


def getRankedPosition(summonerId):
    URL = "https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + str(summonerId) + "?api_key=" + str(
        API_KEY)
    info = requests.get(URL)
    info = json.loads(info.text)
    while True:
        try:
            tier = str(info[0]["tier"])
            rank = str(info[0]["rank"])
            return tier, rank
        except:
            tier = "Unranked"
            rank = 0
            return tier, rank


def getInfoWithMatchID(matchID):
    URL = "https://americas.api.riotgames.com/lol/match/v5/matches/NA1_" + str(matchID) + "?api_key=" + str(API_KEY)
    info = requests.get(URL)
    info = json.loads(info.text)
    df = pd.DataFrame()
    for x in range(10):
        teamID = 0 if info["info"]["participants"][x]["teamId"] == 100 else 1
        if info["info"]["teams"][teamID]["win"] == True:
            SummonerID = info["info"]["participants"][x]["summonerId"]
            kills = info["info"]["participants"][x]["kills"]
            killingSprees = info["info"]["participants"][x]["killingSprees"]
            largestCriticalStrike = info["info"]["participants"][x]["largestCriticalStrike"]
            largestKillingSpree = info["info"]["participants"][x]["largestKillingSpree"]
            largestMultiKill = info["info"]["participants"][x]["largestMultiKill"]
            deaths = info["info"]["participants"][x]["deaths"]
            assists = info["info"]["participants"][x]["assists"]
            goldEarned = info["info"]["participants"][x]["goldEarned"]
            goldSpent = info["info"]["participants"][x]["goldSpent"]
            wardsPlaced = info["info"]["participants"][x]["detectorWardsPlaced"]
            creepsKilled = info["info"]["participants"][x]["totalMinionsKilled"]
            damageDealtToBuildings = info["info"]["participants"][x]["damageDealtToBuildings"]
            damageDealtToObjectives = info["info"]["participants"][x]["damageDealtToObjectives"]
            damageDealtToTurrets = info["info"]["participants"][x]["damageDealtToTurrets"]
            magicDamageDealt = info["info"]["participants"][x]["magicDamageDealtToChampions"]
            physicalDamageDealt = info["info"]["participants"][x]["physicalDamageDealtToChampions"]
            lane = info["info"]["participants"][x]["lane"]
            tier, rank = getRankedPosition(SummonerID)
            data = pd.Series({"lane": lane,
                              "tier": tier,
                              "rank": rank,
                              "creepsKilled": creepsKilled,
                              "kills": kills,
                              "killingSprees": killingSprees,
                              "largestCriticalStrike": largestCriticalStrike,
                              "largestKillingSpree": largestKillingSpree,
                              "largestMultiKill": largestMultiKill,
                              "deaths": deaths,
                              "assists": assists,
                              "goldEarned": goldEarned,
                              "goldSpent" : goldSpent,
                              "wardsPlaced": wardsPlaced,
                              "damageDealtToBuildings": damageDealtToBuildings,
                              "damageDealtToObjectives": damageDealtToObjectives,
                              "damageDealtToTurrets": damageDealtToTurrets,
                              "magicDamageDealt": magicDamageDealt,
                              "physicalDamageDealt": physicalDamageDealt
                              })
            df = df.append(data, ignore_index=True)
    return df

print(getMatchID(matchesData))
#print(len(matchesID))
#print(matchesData.info())