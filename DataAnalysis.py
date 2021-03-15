#!/usr/bin/env python3

DATE = "21 November 2019"
VERSION = "i"
AUTHOR = "Cory Wiard"
AUTHORMAIL = "wiardc@allegheny.edu"


#import numpy as np
#import matplotlib.pyplot as plt


import pandas as pd
from itertools import chain
import os

def dataCollectWins():
    file = open("RedsWins.txt", "r")
    RedsWins = []
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        RedsWins.append(line_list)

    return RedsWins

def dataOrganizer(year, RedsWins):

    i = 0
    df = pd.read_csv("upload/Reds/cincyReds{}.csv".format(year), header=None)
    row = df.tail(1)
    RedsData = row.values.tolist()
    NewList = list(chain.from_iterable(RedsData))
    NewList.extend(RedsWins[i])
    RedsWins.remove(RedsWins[i])
    NewList.pop(0)
    NewList.pop(16)
    RedsDict = {year: NewList}

    return RedsDict

def dataStore(RedsTotalData, year):
    df = pd.DataFrame.from_dict(RedsTotalData, orient="index")
    df.to_csv("upload/RedsData{}.csv".format(year))

def dataCorrelation(year):
    df = pd.read_csv("upload/Reds/Totals/RedsData{}.csv".format(year))
    WinsCorr = df.corr(method='pearson')
    #print(WinsCorr)
    #print()


def main():
    RedsWins = dataCollectWins()
    year = 2002
    RedsTotalData = {}
    while year <= 2018:
        RedsDict = dataOrganizer(year, RedsWins)
        RedsTotalData.update(RedsDict)
        dataStore(RedsTotalData, year)
        #RedsTotalData.clear()
        year = year + 1
    dataCorrelation(year)

if __name__ == '__main__':
    main()
