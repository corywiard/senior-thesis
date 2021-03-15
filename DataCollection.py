#!/usr/bin/env python3

DATE = "21 November 2019"
VERSION = "i"
AUTHOR = "Cory Wiard"
AUTHORMAIL = "wiardc@allegheny.edu"


import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
#import re


def dataCollectorReds(year):
        # pull in web's source code
            url = "https://www.espn.com/mlb/team/stats/_/name/cin/season/{}/seasontype/2".format(year)
            html = urlopen(url)

            #print(url)

            soup = BeautifulSoup(html, "lxml")

            # collects variable names
            variables = []
            player_variables = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for stats_variables in player_variables.find_all('th'):
                variables.append(stats_variables.get_text())

            # collects player's name from Table
            names = ['Name']
            name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
            for data in name_variable.find_all('tr'):
                names.append(data.get_text())

            # Turns list into dictionary
            names_dict_reds = dict.fromkeys(names)

            # collects player's data into list
            data_row = []
            row_stats = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for info in row_stats.find_all('td'):
                data_row.append(info.get_text())

            # multi-dimensional list to hold player stats
            multi_list_of_stats = []
            # list adds variable names to it
            multi_list_of_stats.append(variables[0:17])
            x = 0
            # while loop to add row of player stats to new list and delete from old list
            while x < len(names):
                multi_list_of_stats.append(data_row[0:17])
                del data_row[0:17]
                x = x + 1
            # for loop to iterate through dictionary adding list index
            i = 0
            for key in names_dict_reds:
                names_dict_reds[key] = multi_list_of_stats[i]
                i = i + 1

            return names_dict_reds
            #return stats_list

def dataCollectorCardinals(year):
        # pull in web's source code
            url = "https://www.espn.com/mlb/team/stats/_/name/cin/season/{}/seasontype/2".format(year)
            html = urlopen(url)

            #print(url)

            soup = BeautifulSoup(html, "lxml")

            # collects variable names
            variables = []
            player_variables = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for stats_variables in player_variables.find_all('th'):
                variables.append(stats_variables.get_text())

            #variables_dict = dict.fromkeys(variables)


            # collects player's name from Table
            names = ['Name']
            name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
            for data in name_variable.find_all('tr'):
                names.append(data.get_text())

            # Turns list into dictionary
            names_dict_cards = dict.fromkeys(names)

            # collects player's data into list
            data_row = []
            row_stats = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for info in row_stats.find_all('td'):
                data_row.append(info.get_text())

            # multi-dimensional list to hold player stats
            stats = []
            # list adds variable names to it
            stats.append(variables[0:17])
            x = 0
            # while loop to add row of player stats to new list and delete from old list
            while x < len(names):
                stats.append(data_row[0:17])
                del data_row[0:17]
                x = x + 1
            # for loop to iterate through dictionary adding list index
            i = 0
            for key in names_dict_cards:
                names_dict_cards[key] = stats[i]
                i = i + 1

            return names_dict_cards

def dataCollectorPirates(year):
        # pull in web's source code
            url = "https://www.espn.com/mlb/team/stats/_/name/pit/season/{}/seasontype/2".format(year)
            html = urlopen(url)

            #print(url)

            soup = BeautifulSoup(html, "lxml")

            # collects variable names
            variables = []
            player_variables = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for stats_variables in player_variables.find_all('th'):
                variables.append(stats_variables.get_text())

            #variables_dict = dict.fromkeys(variables)


            # collects player's name from Table
            names = ['Name']
            name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
            for data in name_variable.find_all('tr'):
                names.append(data.get_text())

            # Turns list into dictionary
            names_dict_pit = dict.fromkeys(names)

            # collects player's data into list
            data_row = []
            row_stats = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for info in row_stats.find_all('td'):
                data_row.append(info.get_text())

            # multi-dimensional list to hold player stats
            multi_list_of_stats = []
            # list adds variable names to it
            multi_list_of_stats.append(variables[0:17])
            x = 0
            # while loop to add row of player stats to new list and delete from old list
            while x < len(names):
                multi_list_of_stats.append(data_row[0:17])
                del data_row[0:17]
                x = x + 1
            # for loop to iterate through dictionary adding list index
            i = 0
            for key in names_dict_pit:
                names_dict_pit[key] = multi_list_of_stats[i]
                i = i + 1

            return names_dict_pit
            #return stats_list

def dataCollectorCubs(year):
        # pull in web's source code
            url = "https://www.espn.com/mlb/team/stats/_/name/chc/season/{}/seasontype/2".format(year)
            html = urlopen(url)

            #print(url)

            soup = BeautifulSoup(html, "lxml")

            # collects variable names
            variables = []
            player_variables = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for stats_variables in player_variables.find_all('th'):
                variables.append(stats_variables.get_text())

            #variables_dict = dict.fromkeys(variables)


            # collects player's name from Table
            names = ['Name']
            name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
            for data in name_variable.find_all('tr'):
                names.append(data.get_text())

            # Turns list into dictionary
            names_dict_cubs = dict.fromkeys(names)

            # collects player's data into list
            data_row = []
            row_stats = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for info in row_stats.find_all('td'):
                data_row.append(info.get_text())

            # multi-dimensional list to hold player stats
            multi_list_of_stats = []
            # list adds variable names to it
            multi_list_of_stats.append(variables[0:17])
            x = 0
            # while loop to add row of player stats to new list and delete from old list
            while x < len(names):
                multi_list_of_stats.append(data_row[0:17])
                del data_row[0:17]
                x = x + 1
            # for loop to iterate through dictionary adding list index
            i = 0
            for key in names_dict_cubs:
                names_dict_cubs[key] = multi_list_of_stats[i]
                i = i + 1

            return names_dict_cubs
            #return stats_list

def dataCollectorBrew(year):
        # pull in web's source code
            url = "https://www.espn.com/mlb/team/stats/_/name/mil/season/{}/seasontype/2".format(year)
            html = urlopen(url)

            #print(url)

            soup = BeautifulSoup(html, "lxml")

            # collects variable names
            variables = []
            player_variables = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for stats_variables in player_variables.find_all('th'):
                variables.append(stats_variables.get_text())

            # collects player's name from Table
            names = ['Name']
            name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
            for data in name_variable.find_all('tr'):
                names.append(data.get_text())

            # Turns list into dictionary
            names_dict_brew = dict.fromkeys(names)

            # collects player's data into list
            data_row = []
            row_stats = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for info in row_stats.find_all('td'):
                data_row.append(info.get_text())

            # multi-dimensional list to hold player stats
            multi_list_of_stats = []
            # list adds variable names to it
            multi_list_of_stats.append(variables[0:17])
            x = 0
            # while loop to add row of player stats to new list and delete from old list
            while x < len(names):
                multi_list_of_stats.append(data_row[0:17])
                del data_row[0:17]
                x = x + 1
            # for loop to iterate through dictionary adding list index
            i = 0
            for key in names_dict_brew:
                names_dict_brew[key] = multi_list_of_stats[i]
                i = i + 1

            return names_dict_brew
            #return stats_list

def dataCollectorBraves(year):
        # pull in web's source code
            url = "https://www.espn.com/mlb/team/stats/_/name/atl/season/{}/seasontype/2".format(year)
            html = urlopen(url)

            #print(url)

            soup = BeautifulSoup(html, "lxml")

            # collects variable names
            variables = []
            player_variables = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for stats_variables in player_variables.find_all('th'):
                variables.append(stats_variables.get_text())

            # collects player's name from Table
            names = ['Name']
            name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
            for data in name_variable.find_all('tr'):
                names.append(data.get_text())

            # Turns list into dictionary
            names_dict_braves = dict.fromkeys(names)

            # collects player's data into list
            data_row = []
            row_stats = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for info in row_stats.find_all('td'):
                data_row.append(info.get_text())

            # multi-dimensional list to hold player stats
            multi_list_of_stats = []
            # list adds variable names to it
            multi_list_of_stats.append(variables[0:17])
            x = 0
            # while loop to add row of player stats to new list and delete from old list
            while x < len(names):
                multi_list_of_stats.append(data_row[0:17])
                del data_row[0:17]
                x = x + 1
            # for loop to iterate through dictionary adding list index
            i = 0
            for key in names_dict_braves:
                names_dict_braves[key] = multi_list_of_stats[i]
                i = i + 1

            return names_dict_braves
            #return stats_list

def dataCollectorPhillies(year):
        # pull in web's source code
            url = "https://www.espn.com/mlb/team/stats/_/name/phi/season/{}/seasontype/2".format(year)
            html = urlopen(url)

            #print(url)

            soup = BeautifulSoup(html, "lxml")

            # collects variable names
            variables = []
            player_variables = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for stats_variables in player_variables.find_all('th'):
                variables.append(stats_variables.get_text())

            # collects player's name from Table
            names = ['Name']
            name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
            for data in name_variable.find_all('tr'):
                names.append(data.get_text())

            # Turns list into dictionary
            names_dict_phil = dict.fromkeys(names)

            # collects player's data into list
            data_row = []
            row_stats = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for info in row_stats.find_all('td'):
                data_row.append(info.get_text())

            # multi-dimensional list to hold player stats
            multi_list_of_stats = []
            # list adds variable names to it
            multi_list_of_stats.append(variables[0:17])
            x = 0
            # while loop to add row of player stats to new list and delete from old list
            while x < len(names):
                multi_list_of_stats.append(data_row[0:17])
                del data_row[0:17]
                x = x + 1
            # for loop to iterate through dictionary adding list index
            i = 0
            for key in names_dict_phil:
                names_dict_phil[key] = multi_list_of_stats[i]
                i = i + 1

            return names_dict_phil
            #return stats_list

def dataCollectorMets(year):
        # pull in web's source code
            url = "https://www.espn.com/mlb/team/stats/_/name/nym/season/{}/seasontype/2".format(year)
            html = urlopen(url)

            #print(url)

            soup = BeautifulSoup(html, "lxml")

            # collects variable names
            variables = []
            player_variables = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for stats_variables in player_variables.find_all('th'):
                variables.append(stats_variables.get_text())

            # collects player's name from Table
            names = ['Name']
            name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
            for data in name_variable.find_all('tr'):
                names.append(data.get_text())

            # Turns list into dictionary
            names_dict_mets = dict.fromkeys(names)

            # collects player's data into list
            data_row = []
            row_stats = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for info in row_stats.find_all('td'):
                data_row.append(info.get_text())

            # multi-dimensional list to hold player stats
            multi_list_of_stats = []
            # list adds variable names to it
            multi_list_of_stats.append(variables[0:17])
            x = 0
            # while loop to add row of player stats to new list and delete from old list
            while x < len(names):
                multi_list_of_stats.append(data_row[0:17])
                del data_row[0:17]
                x = x + 1
            # for loop to iterate through dictionary adding list index
            i = 0
            for key in names_dict_mets:
                names_dict_mets[key] = multi_list_of_stats[i]
                i = i + 1

            return names_dict_mets
            #return stats_list

def dataCollectorDBacks(year):
        # pull in web's source code
            url = "https://www.espn.com/mlb/team/stats/_/name/ari/season/{}/seasontype/2".format(year)
            html = urlopen(url)

            #print(url)

            soup = BeautifulSoup(html, "lxml")

            # collects variable names
            variables = []
            player_variables = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for stats_variables in player_variables.find_all('th'):
                variables.append(stats_variables.get_text())

            # collects player's name from Table
            names = ['Name']
            name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
            for data in name_variable.find_all('tr'):
                names.append(data.get_text())

            # Turns list into dictionary
            names_dict_dbacks = dict.fromkeys(names)

            # collects player's data into list
            data_row = []
            row_stats = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for info in row_stats.find_all('td'):
                data_row.append(info.get_text())

            # multi-dimensional list to hold player stats
            multi_list_of_stats = []
            # list adds variable names to it
            multi_list_of_stats.append(variables[0:17])
            x = 0
            # while loop to add row of player stats to new list and delete from old list
            while x < len(names):
                multi_list_of_stats.append(data_row[0:17])
                del data_row[0:17]
                x = x + 1
            # for loop to iterate through dictionary adding list index
            i = 0
            for key in names_dict_dbacks:
                names_dict_dbacks[key] = multi_list_of_stats[i]
                i = i + 1

            return names_dict_dbacks
            #return stats_list

def dataCollectorGiants(year):
        # pull in web's source code
            url = "https://www.espn.com/mlb/team/stats/_/name/sf/season/{}/seasontype/2".format(year)
            html = urlopen(url)

            #print(url)

            soup = BeautifulSoup(html, "lxml")

            # collects variable names
            variables = []
            player_variables = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for stats_variables in player_variables.find_all('th'):
                variables.append(stats_variables.get_text())

            # collects player's name from Table
            names = ['Name']
            name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
            for data in name_variable.find_all('tr'):
                names.append(data.get_text())

            # Turns list into dictionary
            names_dict_giants = dict.fromkeys(names)

            # collects player's data into list
            data_row = []
            row_stats = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for info in row_stats.find_all('td'):
                data_row.append(info.get_text())

            # multi-dimensional list to hold player stats
            multi_list_of_stats = []
            # list adds variable names to it
            multi_list_of_stats.append(variables[0:17])
            x = 0
            # while loop to add row of player stats to new list and delete from old list
            while x < len(names):
                multi_list_of_stats.append(data_row[0:17])
                del data_row[0:17]
                x = x + 1
            # for loop to iterate through dictionary adding list index
            i = 0
            for key in names_dict_giants:
                names_dict_giants[key] = multi_list_of_stats[i]
                i = i + 1

            return names_dict_giants
            #return stats_list

def dataCollectorRockies(year):
        # pull in web's source code
            url = "https://www.espn.com/mlb/team/stats/_/name/col/season/{}/seasontype/2".format(year)
            html = urlopen(url)

            #print(url)

            soup = BeautifulSoup(html, "lxml")

            # collects variable names
            variables = []
            player_variables = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for stats_variables in player_variables.find_all('th'):
                variables.append(stats_variables.get_text())

            # collects player's name from Table
            names = ['Name']
            name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
            for data in name_variable.find_all('tr'):
                names.append(data.get_text())

            # Turns list into dictionary
            names_dict_rockies = dict.fromkeys(names)

            # collects player's data into list
            data_row = []
            row_stats = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for info in row_stats.find_all('td'):
                data_row.append(info.get_text())

            # multi-dimensional list to hold player stats
            multi_list_of_stats = []
            # list adds variable names to it
            multi_list_of_stats.append(variables[0:17])
            x = 0
            # while loop to add row of player stats to new list and delete from old list
            while x < len(names):
                multi_list_of_stats.append(data_row[0:17])
                del data_row[0:17]
                x = x + 1
            # for loop to iterate through dictionary adding list index
            i = 0
            for key in names_dict_rockies:
                names_dict_rockies[key] = multi_list_of_stats[i]
                i = i + 1

            return names_dict_rockies
            #return stats_list

def dataCollectorPadres(year):
        # pull in web's source code
            url = "https://www.espn.com/mlb/team/stats/_/name/sd/season/{}/seasontype/2".format(year)
            html = urlopen(url)

            #print(url)

            soup = BeautifulSoup(html, "lxml")

            # collects variable names
            variables = []
            player_variables = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for stats_variables in player_variables.find_all('th'):
                variables.append(stats_variables.get_text())

            # collects player's name from Table
            names = ['Name']
            name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
            for data in name_variable.find_all('tr'):
                names.append(data.get_text())

            # Turns list into dictionary
            names_dict_padres = dict.fromkeys(names)

            # collects player's data into list
            data_row = []
            row_stats = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for info in row_stats.find_all('td'):
                data_row.append(info.get_text())

            # multi-dimensional list to hold player stats
            multi_list_of_stats = []
            # list adds variable names to it
            multi_list_of_stats.append(variables[0:17])
            x = 0
            # while loop to add row of player stats to new list and delete from old list
            while x < len(names):
                multi_list_of_stats.append(data_row[0:17])
                del data_row[0:17]
                x = x + 1
            # for loop to iterate through dictionary adding list index
            i = 0
            for key in names_dict_padres:
                names_dict_padres[key] = multi_list_of_stats[i]
                i = i + 1

            return names_dict_padres
            #return stats_list

def data_store_csv_Reds(year, names_dict_reds):
    # transfering data to CSV
    df = pd.DataFrame.from_dict(names_dict_reds, orient="index")
    df.to_csv("upload/Reds/cincyReds{}.csv".format(year), header = 0)

def data_store_csv_Cards(year, names_dict_cards):
    # transfering data to CSV
    df = pd.DataFrame.from_dict(names_dict_cards, orient="index")
    df.to_csv("upload/Cardinals/StlCards{}.csv".format(year), header = 0)

def data_store_csv_Pit(year, names_dict_pit):
    df = pd.DataFrame.from_dict(names_dict_pit, orient="index")
    df.to_csv("upload/Pirates/PitPirate{}.csv".format(year), header = 0)

def data_store_csv_Cubs(year, names_dict_cubs):
    df = pd.DataFrame.from_dict(names_dict_cubs, orient="index")
    df.to_csv("upload/Cubs/ChicCubs{}.csv".format(year), header = 0)

def data_store_csv_Brew(year, names_dict_brew):
    df = pd.DataFrame.from_dict(names_dict_brew, orient="index")
    df.to_csv("upload/Brewers/MilBrew{}.csv".format(year), header = 0)

def data_store_csv_Braves(year, names_dict_braves):
    df = pd.DataFrame.from_dict(names_dict_braves, orient="index")
    df.to_csv("upload/Braves/AtlBraves{}.csv".format(year), header = 0)

def data_store_csv_Phil(year, names_dict_phil):
    df = pd.DataFrame.from_dict(names_dict_phil, orient="index")
    df.to_csv("upload/Phillies/PhiPhil{}.csv".format(year), header = 0)

def data_store_csv_Mets(year, names_dict_mets):
    df = pd.DataFrame.from_dict(names_dict_mets, orient="index")
    df.to_csv("upload/Mets/NYMets{}.csv".format(year), header = 0)

def data_store_csv_DBacks(year, names_dict_dbacks):
    df = pd.DataFrame.from_dict(names_dict_dbacks, orient="index")
    df.to_csv("upload/DBacks/AriDBacks{}.csv".format(year), header = 0)

def data_store_csv_Giants(year, names_dict_giants):
    df = pd.DataFrame.from_dict(names_dict_giants, orient="index")
    df.to_csv("upload/Giants/SfGiants{}.csv".format(year), header = 0)

def data_store_csv_Rockies(year, names_dict_rockies):
    df = pd.DataFrame.from_dict(names_dict_rockies, orient="index")
    df.to_csv("upload/Rockies/ColRockies{}.csv".format(year), header = 0)

def data_store_csv_Padres(year, names_dict_padres):
    df = pd.DataFrame.from_dict(names_dict_padres, orient="index")
    df.to_csv("upload/Padres/SdPadres{}.csv".format(year), header = 0)

def CreateDirectory():
    path = os.getcwd()
    path = path + "/upload"
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

    path2 = os.getcwd()
    path2 = path2 + "/upload/Reds"
    try:
        os.mkdir(path2)
    except OSError:
        print ("Creation of the directory %s failed" % path2)
    else:
        print ("Successfully created the directory %s " % path2)

    path3 = os.getcwd()
    path3 = path3 + "/upload/Cardinals"
    try:
        os.mkdir(path3)
    except OSError:
        print ("Creation of the directory %s failed" % path3)
    else:
        print ("Successfully created the directory %s " % path3)

    path4 = os.getcwd()
    path4 = path4 + "/upload/Pirates"
    try:
        os.mkdir(path4)
    except OSError:
        print ("Creation of the directory %s failed" % path4)
    else:
        print ("Successfully created the directory %s " % path4)

    path5 = os.getcwd()
    path5 = path5 + "/upload/Cubs"
    try:
        os.mkdir(path5)
    except OSError:
        print ("Creation of the directory %s failed" % path5)
    else:
        print ("Successfully created the directory %s " % path5)

    path6 = os.getcwd()
    path6 = path6 + "/upload/Brewers"
    try:
        os.mkdir(path6)
    except OSError:
        print ("Creation of the directory %s failed" % path6)
    else:
        print ("Successfully created the directory %s " % path6)

    path7 = os.getcwd()
    path7 = path7 + "/upload/Braves"
    try:
        os.mkdir(path7)
    except OSError:
        print ("Creation of the directory %s failed" % path7)
    else:
        print ("Successfully created the directory %s " % path7)

    path8 = os.getcwd()
    path8 = path8 + "/upload/Phillies"
    try:
        os.mkdir(path8)
    except OSError:
        print ("Creation of the directory %s failed" % path8)
    else:
        print ("Successfully created the directory %s " % path8)

    path9 = os.getcwd()
    path9 = path9 + "/upload/Mets"
    try:
        os.mkdir(path9)
    except OSError:
        print ("Creation of the directory %s failed" % path9)
    else:
        print ("Successfully created the directory %s " % path9)

    path10 = os.getcwd()
    path10 = path10 + "/upload/DBacks"
    try:
        os.mkdir(path10)
    except OSError:
        print ("Creation of the directory %s failed" % path10)
    else:
        print ("Successfully created the directory %s " % path10)

    path11 = os.getcwd()
    path11 = path11 + "/upload/Giants"
    try:
        os.mkdir(path11)
    except OSError:
        print ("Creation of the directory %s failed" % path11)
    else:
        print ("Successfully created the directory %s " % path11)

    path12 = os.getcwd()
    path12 = path12 + "/upload/Rockies"
    try:
        os.mkdir(path12)
    except OSError:
        print ("Creation of the directory %s failed" % path12)
    else:
        print ("Successfully created the directory %s " % path12)

    path13 = os.getcwd()
    path13 = path13 + "/upload/Padres"
    try:
        os.mkdir(path13)
    except OSError:
        print ("Creation of the directory %s failed" % path13)
    else:
        print ("Successfully created the directory %s " % path13)

def main():
    year = 2002
    CreateDirectory()
    while year <= 2018:
        names_dict_reds = dataCollectorReds(year)
        data_store_csv_Reds(year, names_dict_reds)
        names_dict_cards = dataCollectorCardinals(year)
        data_store_csv_Cards(year, names_dict_cards)
        names_dict_pit = dataCollectorPirates(year)
        data_store_csv_Pit(year, names_dict_pit)
        names_dict_cubs = dataCollectorCubs(year)
        data_store_csv_Cubs(year, names_dict_cubs)
        names_dict_brew = dataCollectorBrew(year)
        data_store_csv_Brew(year, names_dict_brew)
        names_dict_braves = dataCollectorBraves(year)
        data_store_csv_Braves(year, names_dict_braves)
        names_dict_phil = dataCollectorPhillies(year)
        data_store_csv_Phil(year, names_dict_phil)
        names_dict_mets = dataCollectorMets(year)
        data_store_csv_Mets(year, names_dict_mets)
        names_dict_dbacks = dataCollectorDBacks(year)
        data_store_csv_DBacks(year, names_dict_dbacks)
        names_dict_giants = dataCollectorGiants(year)
        data_store_csv_Giants(year, names_dict_giants)
        names_dict_rockies = dataCollectorRockies(year)
        data_store_csv_Rockies(year, names_dict_rockies)
        names_dict_padres = dataCollectorPadres(year)
        data_store_csv_Padres(year, names_dict_padres)
        year = year + 1

if __name__ == '__main__':
    main()
