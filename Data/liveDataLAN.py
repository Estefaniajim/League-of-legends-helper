import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv

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
    df = pd.DataFrame()
    gameTime = info["gameLength"]



