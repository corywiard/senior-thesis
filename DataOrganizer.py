#!/usr/bin/env python3

DATE = "21 November 2019"
VERSION = "i"
AUTHOR = "Cory Wiard"
AUTHORMAIL = "wiardc@allegheny.edu"


#import numpy as np
#import matplotlib.pyplot as plt


import pandas as pd
from itertools import chain

def dataCollectRedsWins():
    file = open("Wins/RedsWins.txt", "r")
    RedsWins = []
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        RedsWins.append(line_list)

    return RedsWins

def dataOrganizerReds(year, RedsWins):

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

def dataStoreReds(RedsTotalData, year):
    df = pd.DataFrame.from_dict(RedsTotalData, orient="index")
    df.to_csv("upload/RedsData{}.csv".format(year))

def dataCollectCardsWins():
    file = open("Wins/CardsWins.txt", "r")
    CardsWins = []
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        CardsWins.append(line_list)

    return CardsWins

def dataOrganizerCards(year, CardsWins):

    i = 0
    df = pd.read_csv("upload/Cardinals/StlCards{}.csv".format(year), header=None)
    row = df.tail(1)
    CardsData = row.values.tolist()
    NewList = list(chain.from_iterable(CardsData))
    NewList.extend(CardsWins[i])
    CardsWins.remove(CardsWins[i])
    NewList.pop(0)
    NewList.pop(16)
    CardsDict = {year: NewList}

    return CardsDict

def dataStoreCards(CardsTotalData, year):
    df = pd.DataFrame.from_dict(CardsTotalData, orient="index")
    df.to_csv("upload/CardsData{}.csv".format(year))

def dataCollectBravesWins():
    file = open("Wins/BravesWins.txt", "r")
    BravesWins = []
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        BravesWins.append(line_list)

    return BravesWins

def dataOrganizerBraves(year, BravesWins):

    i = 0
    df = pd.read_csv("upload/Braves/AtlBraves{}.csv".format(year), header=None)
    row = df.tail(1)
    BravesData = row.values.tolist()
    NewList = list(chain.from_iterable(BravesData))
    NewList.extend(BravesWins[i])
    BravesWins.remove(BravesWins[i])
    NewList.pop(0)
    NewList.pop(16)
    BravesDict = {year: NewList}

    return BravesDict

def dataStoreBraves(BravesTotalData, year):
    df = pd.DataFrame.from_dict(BravesTotalData, orient="index")
    df.to_csv("upload/BravesData{}.csv".format(year))

def dataCollectBrewersWins():
    file = open("Wins/BrewersWins.txt", "r")
    BrewersWin = []
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        BrewersWin.append(line_list)

    return BrewersWin

def dataOrganizerBrewers(year, BrewersWin):

    i = 0
    df = pd.read_csv("upload/Brewers/MilBrew{}.csv".format(year), header=None)
    row = df.tail(1)
    BrewersData = row.values.tolist()
    NewList = list(chain.from_iterable(BrewersData))
    NewList.extend(BrewersWin[i])
    BrewersWin.remove(BrewersWin[i])
    NewList.pop(0)
    NewList.pop(16)
    BrewersDict = {year: NewList}

    return BrewersDict

def dataStoreBrewers(BrewersTotalData, year):
    df = pd.DataFrame.from_dict(BrewersTotalData, orient="index")
    df.to_csv("upload/BrewersData{}.csv".format(year))

def dataCollectCubsWins():
    file = open("Wins/CubsWins.txt", "r")
    CubsWins = []
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        CubsWins.append(line_list)

    return CubsWins

def dataOrganizerCubs(year, CubsWins):

    i = 0
    df = pd.read_csv("upload/Cubs/ChicCubs{}.csv".format(year), header=None)
    row = df.tail(1)
    CubsData = row.values.tolist()
    NewList = list(chain.from_iterable(CubsData))
    NewList.extend(CubsWins[i])
    CubsWins.remove(CubsWins[i])
    NewList.pop(0)
    NewList.pop(16)
    CubsDict = {year: NewList}

    return CubsDict

def dataStoreCubs(CubsTotalData, year):
    df = pd.DataFrame.from_dict(CubsTotalData, orient="index")
    df.to_csv("upload/CubsData{}.csv".format(year))

def dataCollectDBacksWins():
    file = open("Wins/DBacksWins.txt", "r")
    DBacksWins = []
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        DBacksWins.append(line_list)

    return DBacksWins

def dataOrganizerDBacks(year, DBacksWins):

    i = 0
    df = pd.read_csv("upload/DBacks/AriDBacks{}.csv".format(year), header=None)
    row = df.tail(1)
    DBacksData = row.values.tolist()
    NewList = list(chain.from_iterable(DBacksData))
    NewList.extend(DBacksWins[i])
    DBacksWins.remove(DBacksWins[i])
    NewList.pop(0)
    NewList.pop(16)
    DBacksDict = {year: NewList}

    return DBacksDict

def dataStoreDBacks(DBacksTotalData, year):
    df = pd.DataFrame.from_dict(DBacksTotalData, orient="index")
    df.to_csv("upload/DBacksData{}.csv".format(year))

def dataCollectGiantsWins():
    file = open("Wins/GiantsWins.txt", "r")
    GiantsWins = []
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        GiantsWins.append(line_list)

    return GiantsWins

def dataOrganizerGiants(year, GiantsWins):

    i = 0
    df = pd.read_csv("upload/Giants/SfGiants{}.csv".format(year), header=None)
    row = df.tail(1)
    GiantsData = row.values.tolist()
    NewList = list(chain.from_iterable(GiantsData))
    NewList.extend(GiantsWins[i])
    GiantsWins.remove(GiantsWins[i])
    NewList.pop(0)
    NewList.pop(16)
    GiantsDict = {year: NewList}

    return GiantsDict

def dataStoreGiants(GiantsTotalData, year):
    df = pd.DataFrame.from_dict(GiantsTotalData, orient="index")
    df.to_csv("upload/GiantsData{}.csv".format(year))

def dataCollectMetsWins():
    file = open("Wins/MetsWins.txt", "r")
    MetsWins = []
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        MetsWins.append(line_list)

    return MetsWins

def dataOrganizerMets(year, MetsWins):

    i = 0
    df = pd.read_csv("upload/Mets/NYMets{}.csv".format(year), header=None)
    row = df.tail(1)
    MetsData = row.values.tolist()
    NewList = list(chain.from_iterable(MetsData))
    NewList.extend(MetsWins[i])
    MetsWins.remove(MetsWins[i])
    NewList.pop(0)
    NewList.pop(16)
    MetsDict = {year: NewList}

    return MetsDict

def dataStoreMets(MetsTotalData, year):
    df = pd.DataFrame.from_dict(MetsTotalData, orient="index")
    df.to_csv("upload/MetsData{}.csv".format(year))

def dataCollectPadresWins():
    file = open("Wins/PadresWins.txt", "r")
    PadresWins = []
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        PadresWins.append(line_list)

    return PadresWins

def dataOrganizerPadres(year, PadresWins):

    i = 0
    df = pd.read_csv("upload/Padres/SdPadres{}.csv".format(year), header=None)
    row = df.tail(1)
    PadresData = row.values.tolist()
    NewList = list(chain.from_iterable(PadresData))
    NewList.extend(PadresWins[i])
    PadresWins.remove(PadresWins[i])
    NewList.pop(0)
    NewList.pop(16)
    PadresDict = {year: NewList}

    return PadresDict

def dataStorePadres(PadresTotalData, year):
    df = pd.DataFrame.from_dict(PadresTotalData, orient="index")
    df.to_csv("upload/PadresData{}.csv".format(year))

def dataCollectPhilliesWins():
    file = open("Wins/PhilliesWins.txt", "r")
    PhilliesWins = []
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        PhilliesWins.append(line_list)

    return PhilliesWins

def dataOrganizerPhillies(year, PhilliesWins):

    i = 0
    df = pd.read_csv("upload/Phillies/PhiPhil{}.csv".format(year), header=None)
    row = df.tail(1)
    PhilliesData = row.values.tolist()
    NewList = list(chain.from_iterable(PhilliesData))
    NewList.extend(PhilliesWins[i])
    PhilliesWins.remove(PhilliesWins[i])
    NewList.pop(0)
    NewList.pop(16)
    PhilliesDict = {year: NewList}

    return PhilliesDict

def dataStorePhillies(PhilliesTotalData, year):
    df = pd.DataFrame.from_dict(PhilliesTotalData, orient="index")
    df.to_csv("upload/PhilliesData{}.csv".format(year))

def dataCollectPiratesWins():
    file = open("Wins/PiratesWins.txt", "r")
    PiratesWins = []
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        PiratesWins.append(line_list)

    return PiratesWins

def dataOrganizerPirates(year, PiratesWins):

    i = 0
    df = pd.read_csv("upload/Pirates/PitPirate{}.csv".format(year), header=None)
    row = df.tail(1)
    PiratesData = row.values.tolist()
    NewList = list(chain.from_iterable(PiratesData))
    NewList.extend(PiratesWins[i])
    PiratesWins.remove(PiratesWins[i])
    NewList.pop(0)
    NewList.pop(16)
    PiratesDict = {year: NewList}

    return PiratesDict

def dataStorePirates(PiratesTotalData, year):
    df = pd.DataFrame.from_dict(PiratesTotalData, orient="index")
    df.to_csv("upload/PiratesData{}.csv".format(year))

def dataCollectRockiesWins():
    file = open("Wins/RockiesWins.txt", "r")
    RockiesWins = []
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        RockiesWins.append(line_list)

    return RockiesWins

def dataOrganizerRockies(year, RockiesWins):

    i = 0
    df = pd.read_csv("upload/Rockies/ColRockies{}.csv".format(year), header=None)
    row = df.tail(1)
    RockiesData = row.values.tolist()
    NewList = list(chain.from_iterable(RockiesData))
    NewList.extend(RockiesWins[i])
    RockiesWins.remove(RockiesWins[i])
    NewList.pop(0)
    NewList.pop(16)
    RockiesDict = {year: NewList}

    return RockiesDict

def dataStoreRockies(RockiesTotalData, year):
    df = pd.DataFrame.from_dict(RockiesTotalData, orient="index")
    df.to_csv("upload/RockiesData{}.csv".format(year))

def dataStoreAllData(TotalData):
    df = pd.DataFrame.from_dict(TotalData, orient="index")
    df.to_csv("upload/TotalData.csv")

def main():
    RedsWins = dataCollectRedsWins()
    CardsWins = dataCollectCardsWins()
    BravesWins = dataCollectBravesWins()
    BrewersWins = dataCollectBrewersWins()
    CubsWins = dataCollectCubsWins()
    DBacksWins = dataCollectDBacksWins()
    GiantsWins = dataCollectGiantsWins()
    MetsWins = dataCollectMetsWins()
    PadresWins = dataCollectPadresWins()
    PhilliesWins = dataCollectPhilliesWins()
    PiratesWins = dataCollectPiratesWins()
    RockiesWins = dataCollectRockiesWins()

    year = 2002

    RedsTotalData = {}
    CardsTotalData = {}
    BravesTotalData = {}
    BrewersTotalData = {}
    CubsTotalData = {}
    DBacksTotalData = {}
    GiantsTotalData = {}
    MetsTotalData = {}
    PadresTotalData = {}
    PhilliesTotalData = {}
    PiratesTotalData = {}
    RockiesTotalData = {}
    TotalData = {}

    while year <= 2019:
        RedsDict = dataOrganizerReds(year, RedsWins)
        RedsTotalData.update(RedsDict)

        CardsDict = dataOrganizerCards(year, CardsWins)
        CardsTotalData.update(CardsDict)

        BravesDict = dataOrganizerBraves(year, BravesWins)
        BravesTotalData.update(BravesDict)

        BrewersDict = dataOrganizerBrewers(year, BrewersWins)
        BrewersTotalData.update(BrewersDict)

        CubsDict = dataOrganizerCubs(year, CubsWins)
        CubsTotalData.update(CubsDict)

        DBacksDict = dataOrganizerDBacks(year, DBacksWins)
        DBacksTotalData.update(DBacksDict)

        GiantsDict = dataOrganizerGiants(year, GiantsWins)
        GiantsTotalData.update(GiantsDict)

        MetsDict = dataOrganizerMets(year, MetsWins)
        MetsTotalData.update(MetsDict)

        PadresDict = dataOrganizerPadres(year, PadresWins)
        PadresTotalData.update(PadresDict)

        PhilliesDict = dataOrganizerPhillies(year, PhilliesWins)
        PhilliesTotalData.update(PhilliesDict)

        PiratesDict = dataOrganizerPirates(year, PiratesWins)
        PiratesTotalData.update(PiratesDict)

        RockiesDict = dataOrganizerRockies(year, RockiesWins)
        RockiesTotalData.update(RockiesDict)

        year = year + 1

    dataStoreReds(RedsTotalData, year)
    dataStoreCards(CardsTotalData, year)
    dataStoreBraves(BravesTotalData, year)
    dataStoreBrewers(BrewersTotalData, year)
    dataStoreCubs(CubsTotalData, year)
    dataStoreDBacks(DBacksTotalData, year)
    dataStoreGiants(GiantsTotalData, year)
    dataStoreMets(MetsTotalData, year)
    dataStorePadres(PadresTotalData, year)
    dataStorePhillies(PhilliesTotalData, year)
    dataStorePirates(PiratesTotalData, year)
    dataStoreRockies(RockiesTotalData, year)

    #dataStoreAllData(TotalData)

if __name__ == '__main__':
    main()
