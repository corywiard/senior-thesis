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

            #variables_dict = dict.fromkeys(variables)


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

def main():
    year = 2002
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
        year = year + 1

if __name__ == '__main__':
    main()
