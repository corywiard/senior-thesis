#!/usr/bin/env python3

DATE = "21 November 2019"
VERSION = "i"
AUTHOR = "Cory Wiard"
AUTHORMAIL = "wiardc@allegheny.edu"


import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os


def variableNameCollector(year):
    url = "https://www.espn.com/mlb/team/stats/_/name/cin/season/{}/seasontype/2".format(year)
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    # collects variable names
    variables = []
    player_variables = soup.find('table', attrs={'class': 'Table Table--align-right'})
    for stats_variables in player_variables.find_all('th'):
        variables.append(stats_variables.get_text())

    return variables

def dataCollectorReds(year, variables):
    # pull in web's source code

    url = "https://www.espn.com/mlb/team/stats/_/name/cin/season/{}/seasontype/2".format(year)
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    # collects player's name from Table
    names = ['Name']
    name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
    for data in name_variable.find_all('td'):
        names.append(data.get_text())

    # Turns list into dictionary
    names_dict_reds = dict.fromkeys(names)

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
    for key in names_dict_reds:
        names_dict_reds[key] = stats[i]
        i = i + 1

    return names_dict_reds

def dataCollectorCardinals(year, variables):
        # pull in web's source code
    url = "https://www.espn.com/mlb/team/stats/_/name/cin/season/{}/seasontype/2".format(year)
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    # collects variable names
    # collects player's name from Table
    names = ['Name']
    name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
    for data in name_variable.find_all('td'):
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

def dataCollectorPirates(year, variables):
    #pull in web's source code
    url = "https://www.espn.com/mlb/team/stats/_/name/pit/season/{}/seasontype/2".format(year)
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    # collects player's name from Table
    names = ['Name']
    name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
    for data in name_variable.find_all('td'):
        names.append(data.get_text())

    # Turns list into dictionary
    names_dict_pit = dict.fromkeys(names)

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
    for key in names_dict_pit:
        names_dict_pit[key] = stats[i]
        i = i + 1

    return names_dict_pit
    #return stats_list

def dataCollectorCubs(year, variables):
        # pull in web's source code
    url = "https://www.espn.com/mlb/team/stats/_/name/chc/season/{}/seasontype/2".format(year)
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    # collects player's name from Table
    names = ['Name']
    name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
    for data in name_variable.find_all('td'):
        names.append(data.get_text())

    # Turns list into dictionary
    names_dict_cubs = dict.fromkeys(names)

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
    for key in names_dict_cubs:
        names_dict_cubs[key] = stats[i]
        i = i + 1

    return names_dict_cubs

def dataCollectorBrew(year, variables):
        # pull in web's source code
    url = "https://www.espn.com/mlb/team/stats/_/name/mil/season/{}/seasontype/2".format(year)
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    # collects player's name from Table
    names = ['Name']
    name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
    for data in name_variable.find_all('td'):
        names.append(data.get_text())

    # Turns list into dictionary
    names_dict_brew = dict.fromkeys(names)

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
    for key in names_dict_brew:
        names_dict_brew[key] = stats[i]
        i = i + 1

    return names_dict_brew

def dataCollectorBraves(year, variables):
        # pull in web's source code
    url = "https://www.espn.com/mlb/team/stats/_/name/atl/season/{}/seasontype/2".format(year)
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    # collects player's name from Table
    names = ['Name']
    name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
    for data in name_variable.find_all('td'):
        names.append(data.get_text())

    # Turns list into dictionary
    names_dict_braves = dict.fromkeys(names)

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
    for key in names_dict_braves:
        names_dict_braves[key] = stats[i]
        i = i + 1

    return names_dict_braves

def dataCollectorPhillies(year, variables):
        # pull in web's source code
    url = "https://www.espn.com/mlb/team/stats/_/name/phi/season/{}/seasontype/2".format(year)
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    # collects player's name from Table
    names = ['Name']
    name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
    for data in name_variable.find_all('td'):
        names.append(data.get_text())

    # Turns list into dictionary
    names_dict_phil = dict.fromkeys(names)

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
    for key in names_dict_phil:
        names_dict_phil[key] = stats[i]
        i = i + 1

    return names_dict_phil

def dataCollectorMets(year, variables):
        # pull in web's source code
    url = "https://www.espn.com/mlb/team/stats/_/name/nym/season/{}/seasontype/2".format(year)
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    # collects player's name from Table
    names = ['Name']
    name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
    for data in name_variable.find_all('td'):
        names.append(data.get_text())

    # Turns list into dictionary
    names_dict_mets = dict.fromkeys(names)

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
    for key in names_dict_mets:
        names_dict_mets[key] = stats[i]
        i = i + 1

    return names_dict_mets

def dataCollectorDBacks(year, variables):
        # pull in web's source code
    url = "https://www.espn.com/mlb/team/stats/_/name/ari/season/{}/seasontype/2".format(year)
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    # collects player's name from Table
    names = ['Name']
    name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
    for data in name_variable.find_all('td'):
        names.append(data.get_text())

    # Turns list into dictionary
    names_dict_dbacks = dict.fromkeys(names)

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
    for key in names_dict_dbacks:
        names_dict_dbacks[key] = stats[i]
        i = i + 1

    return names_dict_dbacks

def dataCollectorGiants(year, variables):
    # pull in web's source code
    url = "https://www.espn.com/mlb/team/stats/_/name/sf/season/{}/seasontype/2".format(year)
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    # collects player's name from Table
    names = ['Name']
    name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
    for data in name_variable.find_all('td'):
        names.append(data.get_text())

    # Turns list into dictionary
    names_dict_giants = dict.fromkeys(names)

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
    for key in names_dict_giants:
        names_dict_giants[key] = stats[i]
        i = i + 1

    return names_dict_giants

def dataCollectorRockies(year, variables):
        # pull in web's source code
    url = "https://www.espn.com/mlb/team/stats/_/name/col/season/{}/seasontype/2".format(year)
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    # collects player's name from Table
    names = ['Name']
    name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
    for data in name_variable.find_all('td'):
        names.append(data.get_text())

    # Turns list into dictionary
    names_dict_rockies = dict.fromkeys(names)

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
    for key in names_dict_rockies:
        names_dict_rockies[key] = stats[i]
        i = i + 1

    return names_dict_rockies

def dataCollectorPadres(year, variables):
        # pull in web's source code
    url = "https://www.espn.com/mlb/team/stats/_/name/sd/season/{}/seasontype/2".format(year)
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

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
    for key in names_dict_padres:
        names_dict_padres[key] = stats[i]
        i = i + 1

    return names_dict_padres

def data_store_csv_Reds(year, names_dict_reds, path):
    # transfering data to CSV
    df = pd.DataFrame.from_dict(names_dict_reds, orient="index")
    path = path + "/upload/Reds/cincyReds{}.csv".format(year)
    if os.path.isfile("upload/Reds/cincyReds{}.csv".format(year)):
        print(path, "already exist")
    else:
    # uploads csv file
        df.to_csv("upload/Reds/cincyReds{}.csv".format(year), header = 0)
        print("Successfully uploaded to:", path)

def data_store_csv_Cards(year, names_dict_cards, path):
    # transfering data to CSV
    df = pd.DataFrame.from_dict(names_dict_cards, orient="index")
    path = path + "/upload/Cardinals/StlCards{}.csv".format(year)
    # checks if file exist already
    if os.path.isfile("upload/Cardinals/StlCards{}.csv".format(year)):
        print(path, "already exist")
    else:
    # uploads csv file
        df.to_csv("upload/Cardinals/StlCards{}.csv".format(year), header = 0)
        print("Successfully uploaded to:", path)

def data_store_csv_Pit(year, names_dict_pit, path):
    # transfering data to CSV
    df = pd.DataFrame.from_dict(names_dict_pit, orient="index")
    path = path + "/upload/Pirates/PitPirate{}.csv".format(year)
    # checks if file exist already
    if os.path.isfile("upload/Pirates/PitPirate{}.csv".format(year)):
        print(path, "already exist")
    else:
    # uploads csv file
        df.to_csv("upload/Pirates/PitPirate{}.csv".format(year), header = 0)
        print("Successfully uploaded to:", path)

def data_store_csv_Cubs(year, names_dict_cubs, path):
    # transfering data to CSV
    df = pd.DataFrame.from_dict(names_dict_cubs, orient="index")
    path = path + "/upload/Cubs/ChicCubs{}.csv".format(year)
    # checks if file exist already
    if os.path.isfile("upload/Cubs/ChicCubs{}.csv".format(year)):
        print(path, "already exist")
    else:
    # uploads csv file
        df.to_csv("upload/Cubs/ChicCubs{}.csv".format(year), header = 0)
        print("Successfully uploaded to:", path)

def data_store_csv_Brew(year, names_dict_brew, path):
    # transfering data to CSV
    df = pd.DataFrame.from_dict(names_dict_brew, orient="index")
    path = path + "/upload/Brewers/MilBrew{}.csv".format(year)
    # checks if file exist already
    if os.path.isfile("upload/Brewers/MilBrew{}.csv".format(year)):
        print(path, "already exist")
    else:
    # uploads csv file
        df.to_csv("upload/Brewers/MilBrew{}.csv".format(year), header = 0)
        print("Successfully uploaded to:", path)

def data_store_csv_Braves(year, names_dict_braves, path):
    # transfering data to CSV
    df = pd.DataFrame.from_dict(names_dict_braves, orient="index")
    path = path + "/upload/Braves/AtlBraves{}.csv".format(year)
    # checks if file exist already
    if os.path.isfile("upload/Braves/AtlBraves{}.csv".format(year)):
        print(path, "already exist")
    else:
    # uploads csv file
        df.to_csv("upload/Braves/AtlBraves{}.csv".format(year), header = 0)
        print("Successfully uploaded to:", path)

def data_store_csv_Phil(year, names_dict_phil, path):
    # transfering data to CSV
    df = pd.DataFrame.from_dict(names_dict_phil, orient="index")
    path = path + "/upload/Phillies/PhiPhil{}.csv".format(year)
    # checks if file exist already
    if os.path.isfile("upload/Phillies/PhiPhil{}.csv".format(year)):
        print(path, "already exist")
    else:
    # uploads csv file
        df.to_csv("upload/Phillies/PhiPhil{}.csv".format(year), header = 0)
        print("Successfully uploaded to:", path)

def data_store_csv_Mets(year, names_dict_mets, path):
    # transfering data to CSV
    df = pd.DataFrame.from_dict(names_dict_mets, orient="index")
    path = path + "/upload/Mets/NYMets{}.csv".format(year)
    # checks if file exist already
    if os.path.isfile("upload/Mets/NYMets{}.csv".format(year)):
        print(path, "already exist")
    else:
    # uploads csv file
        df.to_csv("upload/Mets/NYMets{}.csv".format(year), header = 0)
        print("Successfully uploaded to:", path)

def data_store_csv_DBacks(year, names_dict_dbacks, path):
    # transfering data to CSV
    df = pd.DataFrame.from_dict(names_dict_dbacks, orient="index")
    path = path + "/upload/DBacks/AriDBacks{}.csv".format(year)
    # checks if file exist already
    if os.path.isfile("upload/DBacks/AriDBacks{}.csv".format(year)):
        print(path, "already exist")
    else:
    # uploads csv file
        df.to_csv("upload/DBacks/AriDBacks{}.csv".format(year), header = 0)
        print("Successfully uploaded to:", path)

def data_store_csv_Giants(year, names_dict_giants, path):
    # transfering data to CSV
    df = pd.DataFrame.from_dict(names_dict_giants, orient="index")
    path = path + "/upload/Giants/SfGiants{}.csv".format(year)
    # checks if file exist already
    if os.path.isfile("upload/Giants/SfGiants{}.csv".format(year)):
        print(path, "already exist")
    else:
    # uploads csv file
        df.to_csv("upload/Giants/SfGiants{}.csv".format(year), header = 0)
        print("Successfully uploaded to:", path)

def data_store_csv_Rockies(year, names_dict_rockies, path):
    # transfering data to CSV
    df = pd.DataFrame.from_dict(names_dict_rockies, orient="index")
    path = path + "/upload/Rockies/ColRockies{}.csv".format(year)
    # checks if file exist already
    if os.path.isfile("upload/Rockies/ColRockies{}.csv".format(year)):
        print(path, "already exist")
    else:
    # uploads csv file
        df.to_csv("upload/Rockies/ColRockies{}.csv".format(year), header = 0)
        print("Successfully uploaded to:", path)

def data_store_csv_Padres(year, names_dict_padres, path):
    # transfering data to CSV
    df = pd.DataFrame.from_dict(names_dict_padres, orient="index")
    path = path + "/upload/Padres/SdPadres{}.csv".format(year)
    # checks if file exist already
    if os.path.isfile("upload/Padres/SdPadres{}.csv".format(year)):
        print(path, "already exist")
    else:
    # uploads csv file
        df.to_csv("upload/Padres/SdPadres{}.csv".format(year), header = 0)
        print("Successfully uploaded to:", path)

def CreateDirectory(path):
    # creates folders for all teams
    path = path + "/upload"
    try:
        os.mkdir(path)
    except OSError:
        print ("The directory %s already exist" % path)
    else:
        print ("Successfully created the directory %s " % path)

    oldPath = path
    path = path + "/Braves"
    try:
        os.mkdir(path)
    except OSError:
        print ("The directory %s already exist" % path)
    else:
        print ("Successfully created the directory %s " % path)

    path = oldPath
    path = path + "/Cardinals"
    try:
        os.mkdir(path)
    except OSError:
        print ("The directory %s already exist" % path)
    else:
        print ("Successfully created the directory %s " % path)

    path = oldPath
    path = path + "/Pirates"
    try:
        os.mkdir(path)
    except OSError:
        print ("The directory %s already exist" % path)
    else:
        print ("Successfully created the directory %s " % path)

    path = oldPath
    path = path + "/Cubs"
    try:
        os.mkdir(path)
    except OSError:
        print ("The directory %s already exist" % path)
    else:
        print ("Successfully created the directory %s " % path)

    path = oldPath
    path = path + "/Brewers"
    try:
        os.mkdir(path)
    except OSError:
        print ("The directory %s already exist" % path)
    else:
        print ("Successfully created the directory %s " % path)

    path = oldPath
    path = path + "/Reds"
    try:
        os.mkdir(path)
    except OSError:
        print ("The directory %s already exist" % path)
    else:
        print ("Successfully created the directory %s " % path)

    path = oldPath
    path = path + "/Phillies"
    try:
        os.mkdir(path)
    except OSError:
        print ("The directory %s already exist" % path)
    else:
        print ("Successfully created the directory %s " % path)

    path = oldPath
    path = path + "/Mets"
    try:
        os.mkdir(path)
    except OSError:
        print ("The directory %s already exist" % path)
    else:
        print ("Successfully created the directory %s " % path)

    path = oldPath
    path = path + "/DBacks"
    try:
        os.mkdir(path)
    except OSError:
        print ("The directory %s already exist" % path)
    else:
        print ("Successfully created the directory %s " % path)

    path = oldPath
    path = path + "/Giants"
    try:
        os.mkdir(path)
    except OSError:
        print ("The directory %s already exist" % path)
    else:
        print ("Successfully created the directory %s " % path)

    path = oldPath
    path = path + "/Rockies"
    try:
        os.mkdir(path)
    except OSError:
        print ("The directory %s already exist" % path)
    else:
        print ("Successfully created the directory %s " % path)

    path = oldPath
    path = path + "/Padres"
    try:
        os.mkdir(path)
    except OSError:
        print ("The directory %s already exist" % path)
    else:
        print ("Successfully created the directory %s " % path)

    path = oldPath
    path = path + "/Totals"
    try:
        os.mkdir(path)
    except OSError:
        print ("The directory %s already exist" % path)
    else:
        print ("Successfully created the directory %s " % path)

def main():
    # collects user path
    path = os.getcwd()
    CreateDirectory(path)

    # get user input for starting and ending year
    while True:
        while True:
            try:
                year = int(input("Enter a year to start collecting data from 2002-2019:"))
                yearEnd = int(input("Enter a year to stop collecting data from that is later than the previous year selected:"))
                if year <= yearEnd:
                    break
                else:
                    print("The year to stop collecting data is not later than the year to start, Please reselect years.")
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

    # collects data variables
    variables = variableNameCollector(year)

    # runs functions for data collection
    while True:
        user_choice = input("Would you like to collect data for every team, Yes or No:")
        selection = user_choice.lower()
        if selection == "yes":
            while year <= yearEnd:
                names_dict_braves = dataCollectorBraves(year, variables)
                data_store_csv_Braves(year, names_dict_braves, path)

                names_dict_brew = dataCollectorBrew(year, variables)
                data_store_csv_Brew(year, names_dict_brew, path)

                names_dict_cards = dataCollectorCardinals(year, variables)
                data_store_csv_Cards(year, names_dict_cards, path)

                names_dict_cubs = dataCollectorCubs(year, variables)
                data_store_csv_Cubs(year, names_dict_cubs, path)

                names_dict_dbacks = dataCollectorDBacks(year, variables)
                data_store_csv_DBacks(year, names_dict_dbacks, path)

                names_dict_giants = dataCollectorGiants(year, variables)
                data_store_csv_Giants(year, names_dict_giants, path)

                names_dict_mets = dataCollectorMets(year, variables)
                data_store_csv_Mets(year, names_dict_mets, path)

                names_dict_padres = dataCollectorPadres(year, variables)
                data_store_csv_Padres(year, names_dict_padres, path)

                names_dict_phil = dataCollectorPhillies(year, variables)
                data_store_csv_Phil(year, names_dict_phil, path)

                names_dict_pit = dataCollectorPirates(year, variables)
                data_store_csv_Pit(year, names_dict_pit, path)

                names_dict_reds = dataCollectorReds(year, variables)
                data_store_csv_Reds(year, names_dict_reds, path)

                names_dict_rockies = dataCollectorRockies(year, variables)
                data_store_csv_Rockies(year, names_dict_rockies, path)
                year = year + 1
            break

        elif selection == "no":
            user_selection = input("Select a team data to collect from the following: Braves, Brewers, Cardinals, Cubs, DBacks, Giants, Mets, Padres, Phillies, Pirates, Reds, or Rockies:")
            team_selection = user_selection.lower()
            if team_selection == "braves":
                while year <= yearEnd:
                    names_dict_braves = dataCollectorBraves(year, variables)
                    data_store_csv_Braves(year, names_dict_braves, path)
                    year = year + 1
                break
            elif team_selection == "brewers":
                while year <= yearEnd:
                    names_dict_brew = dataCollectorBrew(year, variables)
                    data_store_csv_Brew(year, names_dict_brew, path)
                    year = year + 1
                break
            elif team_selection == "cardinals":
                while year <= yearEnd:
                    names_dict_cards = dataCollectorCardinals(year, variables)
                    data_store_csv_Cards(year, names_dict_cards, path)
                    year = year + 1
                break
            elif team_selection == "cubs":
                while year <= yearEnd:
                    names_dict_cubs = dataCollectorCubs(year, variables)
                    data_store_csv_Cubs(year, names_dict_cubs, path)
                    year = year + 1
                break
            elif team_selection == "dbacks":
                while year <= yearEnd:
                    names_dict_dbacks = dataCollectorDBacks(year, variables)
                    data_store_csv_DBacks(year, names_dict_dbacks, path)
                    year = year + 1
                break
            elif team_selection == "giants":
                while year <= yearEnd:
                    names_dict_giants = dataCollectorGiants(year, variables)
                    data_store_csv_Giants(year, names_dict_giants, path)
                    year = year + 1
                break
            elif team_selection == "mets":
                while year <= yearEnd:
                    names_dict_mets = dataCollectorMets(year, variables)
                    data_store_csv_Mets(year, names_dict_mets, path)
                    year = year + 1
                break
            elif team_selection == "padres":
                while year <= yearEnd:
                    names_dict_padres = dataCollectorPadres(year, variables)
                    data_store_csv_Padres(year, names_dict_padres, path)
                    year = year + 1
                break
            elif team_selection == "phillies":
                while year <= yearEnd:
                    names_dict_phil = dataCollectorPhillies(year, variables)
                    data_store_csv_Phil(year, names_dict_phil, path)
                    year = year + 1
                break
            elif team_selection == "pirates":
                while year <= yearEnd:
                    names_dict_pit = dataCollectorPirates(year, variables)
                    data_store_csv_Pit(year, names_dict_pit, path)
                    year = year + 1
                break
            elif team_selection == "reds":
                while year <= yearEnd:
                    names_dict_reds = dataCollectorReds(year, variables)
                    data_store_csv_Reds(year, names_dict_reds, path)
                    year = year + 1
                break
            elif team_selection == "rockies":
                while year <= yearEnd:
                    names_dict_rockies = dataCollectorRockies(year, variables)
                    data_store_csv_Rockies(year, names_dict_rockies, path)
                    year = year + 1
                break
            else:
                print("Invalid team selected, rerun and try again.")
                continue
        else:
            print("Please run again as an inproper selection was made.")
            continue

if __name__ == '__main__':
    main()
