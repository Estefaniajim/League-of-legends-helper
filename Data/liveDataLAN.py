import requests
import json
import os
from dotenv import load_dotenv
import math
import Data.dataAnalysis as analysis

# Getting the api key from .env
load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")

def gettingSummonerId(summonerName):
    URL = "https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+ str(summonerName) + "?api_key=" + str(
        API_KEY)
    info = requests.get(URL)
    info = json.loads(info.text)
    return info["id"]

def gettingLiveScores(summonerId):
    URL = "https://la1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/"+ str(summonerId) + "?api_key=" + str(
        API_KEY)
    info = requests.get(URL)
    info = json.loads(info.text)
    gameTime = info["gameLength"]
    #for x in range(10):
        #if info["teams"][x]["summonerId"] == str(summonerId):
    return gameTime

def getRankedPosition(summonerId):
    URL = "https://la1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + str(summonerId) + "?api_key=" + str(
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

def gettingAvgScores(gameTime,lane,tier,rank):
    gameTime = gameTime/60
    creepsPerMin = math.ceil((analysis.getAvgCreepsPerMin(lane,tier,rank))*gameTime)
    goldPerMin = math.ceil(analysis.getAvgGoldPerMin(lane,tier,rank)*gameTime)
    return creepsPerMin,goldPerMin