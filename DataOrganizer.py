#!/usr/bin/env python3

DATE = "21 November 2019"
VERSION = "i"
AUTHOR = "Cory Wiard"
AUTHORMAIL = "wiardc@allegheny.edu"


#import numpy as np
#import matplotlib.pyplot as plt


import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from itertools import chain
import os



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

def dataStoreReds(RedsTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(RedsTotalData, orient="index")
    path = path + "/upload/RedsData{}.csv".format(year)
    if os.path.isfile("upload/RedsData{}.csv".format(year)):
        print(path, "already exist")
    else:
        df.to_csv("upload/RedsData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

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

def dataStoreCards(CardsTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(CardsTotalData, orient="index")
    path = path + "/upload/CardsData{}.csv".format(year)
    if os.path.isfile("upload/CardsData{}.csv".format(year)):
        print(path, "already exist")
    else:
        df.to_csv("upload/CardsData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

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

def dataStoreBraves(BravesTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(BravesTotalData, orient="index")
    path = path + "/upload/BravesData{}.csv".format(year)
    if os.path.isfile("upload/BravesData{}.csv".format(year)):
        print(path, "already exist")
    else:
        df.to_csv("upload/BravesData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

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

def dataStoreBrewers(BrewersTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(BrewersTotalData, orient="index")
    path = path + "/upload/BrewersData{}.csv".format(year)
    if os.path.isfile("upload/BrewersData{}.csv".format(year)):
        print(path, "already exist")
    else:
        df.to_csv("upload/BrewersData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

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

def dataStoreCubs(CubsTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(CubsTotalData, orient="index")
    path = path + "/upload/CubsData{}.csv".format(year)
    if os.path.isfile("upload/CubsData{}.csv".format(year)):
        print(path, "already exist")
    else:
        df.to_csv("upload/CubsData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

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

def dataStoreDBacks(DBacksTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(DBacksTotalData, orient="index")
    path = path + "/upload/DBacksData{}.csv".format(year)
    if os.path.isfile("upload/DBacksData{}.csv".format(year)):
        print(path, "already exist")
    else:
        df.to_csv("upload/DBacksData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

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

def dataStoreGiants(GiantsTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(GiantsTotalData, orient="index")
    path = path + "/upload/GiantsData{}.csv".format(year)
    if os.path.isfile("upload/GiantsData{}.csv".format(year)):
        print(path, "already exist")
    else:
        df.to_csv("upload/GiantsData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

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

def dataStoreMets(MetsTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(MetsTotalData, orient="index")
    path = path + "/upload/MetsData{}.csv".format(year)
    if os.path.isfile("upload/MetsData{}.csv".format(year)):
        print(path, "already exist")
    else:
        df.to_csv("upload/MetsData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

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

def dataStorePadres(PadresTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(PadresTotalData, orient="index")
    path = path + "/upload/PadresData{}.csv".format(year)
    if os.path.isfile("upload/PadresData{}.csv".format(year)):
        print(path, "already exist")
    else:
        df.to_csv("upload/PadresData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

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

def dataStorePhillies(PhilliesTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(PhilliesTotalData, orient="index")
    path = path + "/upload/PhilliesData{}.csv".format(year)
    if os.path.isfile("upload/PhilliesData{}.csv".format(year)):
        print(path, "already exist")
    else:
        df.to_csv("upload/PhilliesData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

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

def dataStorePirates(PiratesTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(PiratesTotalData, orient="index")
    path = path + "/upload/PiratesData{}.csv".format(year)
    if os.path.isfile("upload/PiratesData{}.csv".format(year)):
        print(path, "already exist")
    else:
        df.to_csv("upload/PiratesData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

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

def dataStoreRockies(RockiesTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(RockiesTotalData, orient="index")
    path = path + "/upload/RockiesData{}.csv".format(year)
    if os.path.isfile("upload/RockiesData{}.csv".format(year)):
        print(path, "already exist")
    else:
        df.to_csv("upload/RockiesData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)
#def dataStoreAllData(TotalData):
    #df = pd.DataFrame.from_dict(TotalData, orient="index")
    #df.to_csv("upload/TotalData.csv")

def main():

    path = os.getcwd()
    url = "https://www.espn.com/mlb/team/stats/_/name/phi/season/2002/seasontype/2"
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    # collects variable names
    variables = []
    player_variables = soup.find('table', attrs={'class': 'Table Table--align-right'})
    for stats_variables in player_variables.find_all('th'):
        variables.append(stats_variables.get_text())
    variables.pop(16)
    variables.append("Wins")

    RedsWins = [['78'],['69'],['76'],['73'],['80'],['72'],['74'],['78'],['91'],['79'],['97'],['90'],['76'],['64'],['68'],['68'],['67'],['75']]
    CardsWins = [['97'],['85'],['105'],['100'],['83'],['78'],['86'],['91'],['86'],['90'],['88'],['97'],['90'],['100'],['86'],['83'],['88'],['91']]
    BravesWins = [['101'],['101'],['96'],['90'],['79'],['84'],['72'],['86'],['91'],['89'],['94'],['96'],['79'],['67'],['68'],['72'],['90'],['97']]
    BrewersWin = [['56'],['68'],['67'],['81'],['75'],['83'],['90'],['80'],['77'],['96'],['83'],['74'],['82'],['68'],['73'],['86'],['96'],['89']]
    CubsWins = [['67'],['88'],['89'],['79'],['66'],['85'],['97'],['83'],['75'],['71'],['61'],['66'],['73'],['97'],['103'],['92'],['95'],['84']]
    DBacksWins = [['98'],['84'],['51'],['77'],['76'],['90'],['82'],['70'],['65'],['94'],['81'],['81'],['64'],['79'],['69'],['93'],['82'],['85']]
    GiantsWins = [['95'],['100'],['91'],['75'],['76'],['71'],['72'],['88'],['92'],['86'],['94'],['76'],['88'],['84'],['87'],['64'],['73'],['77']]
    MetsWins = [['75'],['66'],['71'],['83'],['97'],['88'],['89'],['70'],['79'],['77'],['74'],['74'],['79'],['90'],['87'],['70'],['77'],['86']]
    PadresWins = [['66'],['64'],['87'],['82'],['88'],['89'],['63'],['75'],['90'],['71'],['76'],['76'],['77'],['74'],['68'],['71'],['66'],['70']]
    PhilliesWins = [['80'],['86'],['86'],['88'],['85'],['89'],['92'],['93'],['97'],['102'],['81'],['73'],['73'],['63'],['71'],['66'],['80'],['81']]
    PiratesWins = [['72'],['75'],['72'],['67'],['67'],['68'],['67'],['62'],['57'],['72'],['79'],['94'],['88'],['98'],['78'],['75'],['82'],['69']]
    RockiesWins = [['73'],['74'],['68'],['67'],['76'],['90'],['74'],['92'],['83'],['73'],['64'],['74'],['66'],['68'],['75'],['87'],['91'],['71']]

    user_input = input("Enter a year to start collecting data from 2002-2019:")
    year = int(user_input)

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

        BrewersDict = dataOrganizerBrewers(year, BrewersWin)
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

    dataStoreReds(RedsTotalData, year, variables, path)
    dataStoreCards(CardsTotalData, year, variables, path)
    dataStoreBraves(BravesTotalData, year, variables, path)
    dataStoreBrewers(BrewersTotalData, year, variables, path)
    dataStoreCubs(CubsTotalData, year, variables, path)
    dataStoreDBacks(DBacksTotalData, year, variables, path)
    dataStoreGiants(GiantsTotalData, year, variables, path)
    dataStoreMets(MetsTotalData, year, variables, path)
    dataStorePadres(PadresTotalData, year, variables, path)
    dataStorePhillies(PhilliesTotalData, year, variables, path)
    dataStorePirates(PiratesTotalData, year, variables, path)
    dataStoreRockies(RockiesTotalData, year, variables, path)


if __name__ == '__main__':
    main()
