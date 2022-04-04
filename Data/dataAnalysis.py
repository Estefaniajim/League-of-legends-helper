import pickle
import math

def loadData():
    pickleFile = open("matchesData.p","rb")
    file = pickle.load(pickleFile)
    return file

def conditions(lane,tier,rank,file):
    con1 = file["lane"] == lane
    con2 = file["tier"] == tier
    con3 = file["rank"] == rank
    return con1,con2,con3

def getAvgCreepsPerMin(lane,tier,rank):
    file = loadData()
    con1,con2,con3 = conditions(lane,tier,rank,file)
    data = file[con1 & con2 & con3]
    avg = math.ceil(data["creepsPerMin"].describe()["mean"])
    return avg

def getAvgGoldPerMin(lane,tier,rank):
    file = loadData()
    con1, con2, con3 = conditions(lane, tier, rank, file)
    data = file[con1 & con2 & con3]
    avg = math.ceil(data["goldPerMin"].describe()["mean"])
    return avg

def getAvgKills(lane,tier,rank):
    file = loadData()
    con1, con2, con3 = conditions(lane, tier, rank, file)
    data = file[con1 & con2 & con3]
    avg = math.ceil(data["kills"].describe()["mean"])
    return avg

def getAvgDeaths(lane,tier,rank):
    file = loadData()
    con1, con2, con3 = conditions(lane, tier, rank, file)
    data = file[con1 & con2 & con3]
    avg = math.ceil(data["deaths"].describe()["mean"])
    return avg

def getAvgAssists(lane,tier,rank):
    file = loadData()
    con1, con2, con3 = conditions(lane, tier, rank, file)
    data = file[con1 & con2 & con3]
    avg = math.ceil(data["assists"].describe()["mean"])
    return avg

def getAvgGoldEarned(lane,tier,rank):
    file = loadData()
    con1, con2, con3 = conditions(lane, tier, rank, file)
    data = file[con1 & con2 & con3]
    avg = math.ceil(data["goldEarned"].describe()["mean"])
    return avg

def getAvgWardsPlaced(lane,tier,rank):
    file = loadData()
    con1, con2, con3 = conditions(lane, tier, rank, file)
    data = file[con1 & con2 & con3]
    avg = math.ceil(data["wardsPlaced"].describe()["mean"])
    return avg

def getAvgWardsKilled(lane,tier,rank):
    file = loadData()
    con1, con2, con3 = conditions(lane, tier, rank, file)
    data = file[con1 & con2 & con3]
    avg = math.ceil(data["wardsKilled"].describe()["mean"])
    return avg

def gettingAvgScores(gameTime,lane,tier,rank):
    gameTime = gameTime/60
    creepsPerMin = math.ceil(getAvgCreepsPerMin(lane,tier,rank)*gameTime)
    goldPerMin = math.ceil(getAvgGoldPerMin(lane,tier,rank)*gameTime)
    return creepsPerMin,goldPerMin

file = loadData()
print(file)