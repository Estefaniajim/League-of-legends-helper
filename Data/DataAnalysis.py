import pandas as pd
import pickle

def loadData():
    pickleFile = open("matchesData.p","rb")
    file = pickle.load(pickleFile)
    return file



