#!/usr/bin/env python3

DATE = "21 November 2019"
VERSION = "i"
AUTHOR = "Cory Wiard"
AUTHORMAIL = "wiardc@allegheny.edu"


import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from itertools import chain
import os
import glob


def dataOrganizerReds(year, RedsWins):

    # checks to makre sure file exist
    if os.path.isfile("upload/Reds/cincyReds{}.csv".format(year)):
        i = 0
        # reads in csv files
        df = pd.read_csv("upload/Reds/cincyReds{}.csv".format(year), header=None)
        row = df.tail(1)
        RedsData = row.values.tolist()
        NewList = list(chain.from_iterable(RedsData))
        NewList.extend(RedsWins[i])
        # removes first location of list
        RedsWins.remove(RedsWins[i])
        NewList.pop(0)
        NewList.pop(16)
        # stores data into dictionary
        RedsDict = {year: NewList}

        return RedsDict
    else:
        print("The csv files you are trying to access for Reds", year, "do not exist. Please try something else.")
        main()

def dataStoreReds(RedsTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(RedsTotalData, orient="index")
    path = path + "/upload/Totals/RedsData{}.csv".format(year)
    # checks if file exist
    if os.path.isfile("upload/Totals/RedsData{}.csv".format(year)):
        print(path, "already exist")
    else:
    # stores csv file
        df.to_csv("upload/Totals/RedsData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

def dataOrganizerCards(year, CardsWins):

    # checks if file exist
    if os.path.isfile("upload/Cardinals/StlCards{}.csv".format(year)):
        i = 0
        # reads in csv files
        df = pd.read_csv("upload/Cardinals/StlCards{}.csv".format(year), header=None)
        row = df.tail(1)
        CardsData = row.values.tolist()
        NewList = list(chain.from_iterable(CardsData))
        NewList.extend(CardsWins[i])
        # removes first location
        CardsWins.remove(CardsWins[i])
        NewList.pop(0)
        NewList.pop(16)
        # stores data into dictionary
        CardsDict = {year: NewList}
        return CardsDict
    else:
        print("The csv files you are trying to access for Cardinals", year, "do not exist. Please try something else.")
        main()

def dataStoreCards(CardsTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(CardsTotalData, orient="index")
    path = path + "/upload/Totals/CardsData{}.csv".format(year)
    # checks if file exist
    if os.path.isfile("upload/Totals/CardsData{}.csv".format(year)):
        print(path, "already exist")
    else:
    # stores file as csv
        df.to_csv("upload/Totals/CardsData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

def dataOrganizerBraves(year, BravesWins):

    # checks if file exist
    if os.path.isfile("upload/Braves/AtlBraves{}.csv".format(year)):
        i = 0
    # reads in csv files
        df = pd.read_csv("upload/Braves/AtlBraves{}.csv".format(year), header=None)
        row = df.tail(1)
        BravesData = row.values.tolist()
        NewList = list(chain.from_iterable(BravesData))
        NewList.extend(BravesWins[i])
        # removes first location
        BravesWins.remove(BravesWins[i])
        NewList.pop(0)
        NewList.pop(16)
        # stores data in dictionary
        BravesDict = {year: NewList}
        return BravesDict
    else:
        print("The csv files you are trying to access for Braves", year, "do not exist. Please try something else.")
        main()

def dataStoreBraves(BravesTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(BravesTotalData, orient="index")
    path = path + "/upload/Totals/BravesData{}.csv".format(year)
    # checks if file exist
    if os.path.isfile("upload/Totals/BravesData{}.csv".format(year)):
        print(path, "already exist")
    else:
    # uploads file as csv
        df.to_csv("upload/Totals/BravesData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

def dataOrganizerBrewers(year, BrewersWin):

    # checks if file exist
    if os.path.isfile("upload/Brewers/MilBrew{}.csv".format(year)):
        i = 0
        # reads in csv files
        df = pd.read_csv("upload/Brewers/MilBrew{}.csv".format(year), header=None)
        row = df.tail(1)
        BrewersData = row.values.tolist()
        NewList = list(chain.from_iterable(BrewersData))
        NewList.extend(BrewersWin[i])
        # removes first location
        BrewersWin.remove(BrewersWin[i])
        NewList.pop(0)
        NewList.pop(16)
        # stores data in dictionary
        BrewersDict = {year: NewList}
        return BrewersDict
    else:
        print("The csv files you are trying to access for Brewers", year, "do not exist. Please try something else.")
        main()

def dataStoreBrewers(BrewersTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(BrewersTotalData, orient="index")
    path = path + "/upload/Totals/BrewersData{}.csv".format(year)
    # check if files exist
    if os.path.isfile("upload/Totals/BrewersData{}.csv".format(year)):
        print(path, "already exist")
    else:
    # stores data in csv
        df.to_csv("upload/Totals/BrewersData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

def dataOrganizerCubs(year, CubsWins):

    # check if file exist
    if os.path.isfile("upload/Cubs/ChicCubs{}.csv".format(year)):
        i = 0
        # read in csv file
        df = pd.read_csv("upload/Cubs/ChicCubs{}.csv".format(year), header=None)
        row = df.tail(1)
        CubsData = row.values.tolist()
        NewList = list(chain.from_iterable(CubsData))
        NewList.extend(CubsWins[i])
        # removes first location of wins
        CubsWins.remove(CubsWins[i])
        NewList.pop(0)
        NewList.pop(16)
        # stores data in dictionary
        CubsDict = {year: NewList}
        return CubsDict
    else:
        print("The csv files you are trying to access for Cubs", year, "do not exist. Please try something else.")
        main()

def dataStoreCubs(CubsTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(CubsTotalData, orient="index")
    path = path + "/upload/Totals/CubsData{}.csv".format(year)
    # checks if file exist
    if os.path.isfile("upload/Totals/CubsData{}.csv".format(year)):
        print(path, "already exist")
    else:
    # stores data in csv file
        df.to_csv("upload/Totals/CubsData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

def dataOrganizerDBacks(year, DBacksWins):

    # checks if file exist
    if os.path.isfile("upload/DBacks/AriDBacks{}.csv".format(year)):
        i = 0
        # reads in csv file
        df = pd.read_csv("upload/DBacks/AriDBacks{}.csv".format(year), header=None)
        row = df.tail(1)
        DBacksData = row.values.tolist()
        NewList = list(chain.from_iterable(DBacksData))
        NewList.extend(DBacksWins[i])
        # removes first location of wins
        DBacksWins.remove(DBacksWins[i])
        NewList.pop(0)
        NewList.pop(16)
        # stores data in dictionary
        DBacksDict = {year: NewList}
        return DBacksDict
    else:
        print("The csv files you are trying to access for DBacks", year, "do not exist. Please try something else.")
        main()

def dataStoreDBacks(DBacksTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(DBacksTotalData, orient="index")
    path = path + "/upload/Totals/DBacksData{}.csv".format(year)
    # checks if file exist
    if os.path.isfile("upload/Totals/DBacksData{}.csv".format(year)):
        print(path, "already exist")
    else:
    # stores file as csv
        df.to_csv("upload/Totals/DBacksData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

def dataOrganizerGiants(year, GiantsWins):

    # checks if file exist
    if os.path.isfile("upload/Giants/SfGiants{}.csv".format(year)):
        i = 0
        # reads in csv
        df = pd.read_csv("upload/Giants/SfGiants{}.csv".format(year), header=None)
        row = df.tail(1)
        GiantsData = row.values.tolist()
        NewList = list(chain.from_iterable(GiantsData))
        NewList.extend(GiantsWins[i])
        # removes first win
        GiantsWins.remove(GiantsWins[i])
        NewList.pop(0)
        NewList.pop(16)
        # stores data in dictionary
        GiantsDict = {year: NewList}
        return GiantsDict
    else:
        print("The csv files you are trying to access for Giants", year, "do not exist. Please try something else.")
        main()

def dataStoreGiants(GiantsTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(GiantsTotalData, orient="index")
    path = path + "/upload/Totals/GiantsData{}.csv".format(year)
    # checks if file exist
    if os.path.isfile("upload/Totals/GiantsData{}.csv".format(year)):
        print(path, "already exist")
    else:
    # stores data as a csv
        df.to_csv("upload/Totals/GiantsData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

def dataOrganizerMets(year, MetsWins):

    # checks if file exist
    if os.path.isfile("upload/Mets/NYMets{}.csv".format(year)):
        i = 0
        # reads in csv
        df = pd.read_csv("upload/Mets/NYMets{}.csv".format(year), header=None)
        row = df.tail(1)
        MetsData = row.values.tolist()
        NewList = list(chain.from_iterable(MetsData))
        NewList.extend(MetsWins[i])
        # removes mets first win location
        MetsWins.remove(MetsWins[i])
        NewList.pop(0)
        NewList.pop(16)
        # stores data in dictionary
        MetsDict = {year: NewList}
        return MetsDict
    else:
        print("The csv files you are trying to access for Mets", year, "do not exist. Please try something else.")
        main()

def dataStoreMets(MetsTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(MetsTotalData, orient="index")
    path = path + "/upload/Totals/MetsData{}.csv".format(year)
    # check if file exist
    if os.path.isfile("upload/Totals/MetsData{}.csv".format(year)):
        print(path, "already exist")
    else:
    # stores as a csv
        df.to_csv("upload/Totals/MetsData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

def dataOrganizerPadres(year, PadresWins):

    # checks if file exist
    if os.path.isfile("upload/Padres/SdPadres{}.csv".format(year)):
        i = 0
        # reads in csv
        df = pd.read_csv("upload/Padres/SdPadres{}.csv".format(year), header=None)
        row = df.tail(1)
        PadresData = row.values.tolist()
        NewList = list(chain.from_iterable(PadresData))
        NewList.extend(PadresWins[i])
        # team wins remove first location
        PadresWins.remove(PadresWins[i])
        NewList.pop(0)
        NewList.pop(16)
        # data stored in dictionary
        PadresDict = {year: NewList}
        return PadresDict
    else:
        print("The csv files you are trying to access for Padres", year, "do not exist. Please try something else.")
        main()

def dataStorePadres(PadresTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(PadresTotalData, orient="index")
    path = path + "/upload/Totals/PadresData{}.csv".format(year)
    # checks if file exist
    if os.path.isfile("upload/Totals/PadresData{}.csv".format(year)):
        print(path, "already exist")
    else:
    # stores file as csv
        df.to_csv("upload/Totals/PadresData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

def dataOrganizerPhillies(year, PhilliesWins):

    # check if file exist
    if os.path.isfile("upload/Phillies/PhiPhil{}.csv".format(year)):
        i = 0
        # reads in csv
        df = pd.read_csv("upload/Phillies/PhiPhil{}.csv".format(year), header=None)
        row = df.tail(1)
        PhilliesData = row.values.tolist()
        NewList = list(chain.from_iterable(PhilliesData))
        NewList.extend(PhilliesWins[i])
        # removes first location of list
        PhilliesWins.remove(PhilliesWins[i])
        NewList.pop(0)
        NewList.pop(16)
        # stores data into dictionary
        PhilliesDict = {year: NewList}
        return PhilliesDict
    else:
        print("The csv files you are trying to access for Phillies", year, "do not exist. Please try something else.")
        main()

def dataStorePhillies(PhilliesTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(PhilliesTotalData, orient="index")
    path = path + "/upload/Totals/PhilliesData{}.csv".format(year)
    # checks if file exist
    if os.path.isfile("upload/Totals/PhilliesData{}.csv".format(year)):
        print(path, "already exist")
    else:
    # store data as csv
        df.to_csv("upload/Totals/PhilliesData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

def dataOrganizerPirates(year, PiratesWins):

    # checks if file exist
    if os.path.isfile("upload/Pirates/PitPirate{}.csv".format(year)):
        i = 0
        # reads csv in
        df = pd.read_csv("upload/Pirates/PitPirate{}.csv".format(year), header=None)
        row = df.tail(1)
        PiratesData = row.values.tolist()
        NewList = list(chain.from_iterable(PiratesData))
        NewList.extend(PiratesWins[i])
        # removes first location of list
        PiratesWins.remove(PiratesWins[i])
        NewList.pop(0)
        NewList.pop(16)
        # stores data in dictionary
        PiratesDict = {year: NewList}
        return PiratesDict
    else:
        print("The csv files you are trying to access for Pirates", year, "do not exist. Please try something else.")
        main()

def dataStorePirates(PiratesTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(PiratesTotalData, orient="index")
    path = path + "/upload/Totals/PiratesData{}.csv".format(year)
    # checks if file exist
    if os.path.isfile("upload/Totals/PiratesData{}.csv".format(year)):
        print(path, "already exist")
    else:
    # stores file as csv
        df.to_csv("upload/Totals/PiratesData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

def dataOrganizerRockies(year, RockiesWins):

    # checks if file exist
    if os.path.isfile("upload/Rockies/ColRockies{}.csv".format(year)):
        i = 0
        # reads in csv
        df = pd.read_csv("upload/Rockies/ColRockies{}.csv".format(year), header=None)
        row = df.tail(1)
        RockiesData = row.values.tolist()
        NewList = list(chain.from_iterable(RockiesData))
        NewList.extend(RockiesWins[i])
        # removes fist location of list
        RockiesWins.remove(RockiesWins[i])
        NewList.pop(0)
        NewList.pop(16)
        # stores data in dictionary
        RockiesDict = {year: NewList}
        return RockiesDict
    else:
        print("The csv files you are trying to access for Rockies", year, "do not exist. Please try something else.")
        main()

def dataStoreRockies(RockiesTotalData, year, variables, path):
    df = pd.DataFrame.from_dict(RockiesTotalData, orient="index")
    path = path + "/upload/Totals/RockiesData{}.csv".format(year)
    # checks if file exist
    if os.path.isfile("upload/Totals/RockiesData{}.csv".format(year)):
        print(path, "already exist")
    else:
    # stores data as csv
        df.to_csv("upload/Totals/RockiesData{}.csv".format(year), header = variables)
        print("Successfully uploaded to:", path)

def totalData(path):
    # finds a path
    path = path + "/upload/Totals/"
    # reads in file stored in path
    all_files = glob.glob(path + "/*.csv")
    li = []
    i = 0
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        # stores new files
        li.append(df)
    frame = pd.concat(li, axis=0, ignore_index=True)
    # sends file as csv
    frame.to_csv("upload/TotalData.csv")

def main():
    # gets path
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

    # stores team regular season wins from 2002-2019
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

    # collects user starting and ending year
    while True:
        while True:
            try:
                year = int(input("Enter a year to start organizing data from 2002-2019:"))
                yearEnd = int(input("Enter a year to stop organizing data from that is later than the previous year selected:"))
                if year <= yearEnd:
                    break
                else:
                    print("The year to stop organizing data is not later than the year to start, Please reselect years.")
            except ValueError:
                print('You entered a non integer value, try again.')
                continue
        if year >= 2002 and year <= 2019:
            if yearEnd >= 2002 and yearEnd <= 2019:
                break
            else:
                print("Invalid ending year, try again.")
        else:
            print("Invalid starting year, try again.")

    # creates empty dictionary to be used later
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

    # organizes data for selected teams
    while True:
        user_choice = input("Would you like to organize data for every team, Yes or No:")
        selection = user_choice.lower()
        if selection == "yes":
            while year <= yearEnd:
                # organizes data for all teams
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

            # function to store the data
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
            break

        # gives user option to select one single team
        elif selection == "no":
            user_selection = input("Select a team data to collect from the following: Braves, Brewers, Cardinals, Cubs, DBacks, Giants, Mets, Padres, Phillies, Pirates, Reds, or Rockies:")
            team_selection = user_selection.lower()
            if team_selection == "braves":
                while year <= yearEnd:
                    BravesDict = dataOrganizerBraves(year, BravesWins)
                    BravesTotalData.update(BravesDict)
                    year = year + 1
                dataStoreBraves(BravesTotalData, year, variables, path)
                break
            elif team_selection == "brewers":
                while year <= yearEnd:
                    BrewersDict = dataOrganizerBrewers(year, BrewersWin)
                    BrewersTotalData.update(BrewersDict)
                    year = year + 1
                dataStoreBrewers(BrewersTotalData, year, variables, path)
                break
            elif team_selection == "cardinals":
                while year <= yearEnd:
                    CardsDict = dataOrganizerCards(year, CardsWins)
                    CardsTotalData.update(CardsDict)
                    year = year + 1
                dataStoreCards(CardsTotalData, year, variables, path)
                break
            elif team_selection == "cubs":
                while year <= yearEnd:
                    CubsDict = dataOrganizerCubs(year, CubsWins)
                    CubsTotalData.update(CubsDict)
                    year = year + 1
                dataStoreCubs(CubsTotalData, year, variables, path)
                break
            elif team_selection == "dbacks":
                while year <= yearEnd:
                    DBacksDict = dataOrganizerDBacks(year, DBacksWins)
                    DBacksTotalData.update(DBacksDict)
                    year = year + 1
                dataStoreDBacks(DBacksTotalData, year, variables, path)
                break
            elif team_selection == "giants":
                while year <= yearEnd:
                    GiantsDict = dataOrganizerGiants(year, GiantsWins)
                    GiantsTotalData.update(GiantsDict)
                    year = year + 1
                dataStoreGiants(GiantsTotalData, year, variables, path)
                break
            elif team_selection == "mets":
                while year <= yearEnd:
                    MetsDict = dataOrganizerMets(year, MetsWins)
                    MetsTotalData.update(MetsDict)
                    year = year + 1
                dataStoreMets(MetsTotalData, year, variables, path)
                break
            elif team_selection == "padres":
                while year <= yearEnd:
                    PadresDict = dataOrganizerPadres(year, PadresWins)
                    PadresTotalData.update(PadresDict)
                    year = year + 1
                dataStorePadres(PadresTotalData, year, variables, path)
                break
            elif team_selection == "phillies":
                while year <= yearEnd:
                    PhilliesDict = dataOrganizerPhillies(year, PhilliesWins)
                    PhilliesTotalData.update(PhilliesDict)
                    year = year + 1
                dataStorePhillies(PhilliesTotalData, year, variables, path)
                break
            elif team_selection == "pirates":
                while year <= yearEnd:
                    PiratesDict = dataOrganizerPirates(year, PiratesWins)
                    PiratesTotalData.update(PiratesDict)
                    year = year + 1
                dataStorePirates(PiratesTotalData, year, variables, path)
                break
            elif team_selection == "reds":
                while year <= yearEnd:
                    RedsDict = dataOrganizerReds(year, RedsWins)
                    RedsTotalData.update(RedsDict)
                    year = year + 1
                dataStoreReds(RedsTotalData, year, variables, path)
                break
            elif team_selection == "rockies":
                while year <= yearEnd:
                    RockiesDict = dataOrganizerRockies(year, RockiesWins)
                    RockiesTotalData.update(RockiesDict)
                    year = year + 1
                dataStoreRockies(RockiesTotalData, year, variables, path)
                break
            else:
                print("Invalid team selected, rerun and try again.")
                continue
        else:
            print("Please run again as an inproper selection was made.")
            continue

    # gives user option to organize all data combined
    while True:
        user_choice = input("Would you like to combine data for every team, Yes or No:")
        selection = user_choice.lower()
        if selection == "yes":
            totalData(path)
            break
        elif selection == "no":
            print("The tool is completed.")
            break
        else:
            print("Wrong input, please try again.")
            continue

if __name__ == '__main__':
    main()
