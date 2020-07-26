import app
import Data.dataAnalysis as da
import Data.liveDataLAN as lan
import Data.liveDataNA as na
import time

#summonerName,server,lane = app.getUser()

def getDataServer(server,summonerName):
    if server == "LAN":
        summonerId = lan.gettingSummonerId(summonerName)
        tier, rank = lan.getRankedPosition(summonerId)
        return summonerId,tier,rank
    else:
        summonerId= na.gettingSummonerId(summonerName)
        tier,rank = na.getRankedPosition(summonerId)
        return summonerId,tier,rank

def refreshData(lane,server,summonerName,creepsPerMin,goldPerMin):
    while True:
        try:
            summonerId,tier,rank = getDataServer(server,summonerName)
            if server == "LAN":
                # gameTime = lan.gettingLiveScores(summonerId)
                gameTime = 120
            else:
                gameTime = na.gettingLiveScores(summonerId)
            creepsPerMin, goldPerMin = da.gettingAvgScores(gameTime,lane,tier,rank)
            time.sleep(60)
        except:
            print("Matched Ended")
            print("Your Score should look like")
            deaths = da.getAvgDeaths(lane,tier,rank)
            kills = da.getAvgKills(lane,tier,rank)
            assists = da.getAvgAssists(lane,tier,rank)
            wardsKilled = da.getAvgWardsKilled(lane,tier,rank)
            wardsPlaced = da.getAvgWardsPlaced(lane,tier,rank)
            print("Your KDA: "+ str(kills)+"/"+str(deaths)+"/"+str(assists))
            print("Your wards placed: "+ str(wardsPlaced)+ " yes, wards are important even if you are not a support")
            print("Your wads killed: "+ str(wardsKilled)+ "yes, even killing wards is important")
            return deaths,kills,assists,wardsKilled,wardsPlaced