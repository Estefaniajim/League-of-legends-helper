import app
import Data.dataAnalysis as da
import Data.liveDataLAN as lan
import Data.liveDataNA as na

summonerName,server,lane = app.getUser()

def getDataServer():
    if server == "LAN":
        summonerId = lan.gettingSummonerId(summonerName)
        tier, rank = lan.getRankedPosition(summonerId)
        return summonerId,tier,rank
    else:
        summonerId, tier, rank = na.gettingSummonerData()
        return summonerId,tier,rank

def refreshData():
    summonerId,tier,rank = getDataServer()
    while True:
        try:
            if server == "LAN":
                gameTime = lan.gettingLiveScores(summonerId)
            else:
                gameTime = na.gettingLiveScores(summonerId)
            creepsPerMin, goldPerMin = da.gettingAvgScores(gameTime,lane,tier,rank)
            return creepsPerMin,goldPerMin
        except:
            break