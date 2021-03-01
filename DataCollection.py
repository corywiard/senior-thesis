#!/usr/bin/env python3

DATE = "21 November 2019"
VERSION = "i"
AUTHOR = "Cory Wiard"
AUTHORMAIL = "wiardc@allegheny.edu"


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


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

            i = 0
            # for loop to iterate through dictionary adding list index to each key
            for key in names_dict_reds:
                names_dict_reds[key] = multi_list_of_stats[i]
                i = i + 1

            return names_dict_reds
            #return stats_list

def dataCollectorCardinals(year):
        # pull in web's source code
            url = "https://www.espn.com/mlb/team/stats/_/name/stl/season/{}/seasontype/2".format(year)
            html = urlopen(url)

            #print(url)

            soup = BeautifulSoup(html, "lxml")

            # collects variable names
            variables = []
            player_variables = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for stats_variables in player_variables.find_all('th'):
                variables.append(stats_variables.get_text())

            # turns list into dictionary
            #variables_dict = dict.fromkeys(variables)
            # collects all data from table
            #stats_list = []
            #player_stats = soup.find('div', attrs={'class': 'ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize'})
            #for stats in player_stats.find_all('td'):
                #stats_list.append(stats.get_text())

            # collects name from Table
            names = ['Name']
            name_variable = soup.find('tbody', attrs={'class': 'Table__TBODY'})
            for data in name_variable.find_all('tr'):
                names.append(data.get_text())

            names_dict_cards = dict.fromkeys(names)

            # collects data in new list
            data_row = []
            row_stats = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for info in row_stats.find_all('td'):
                data_row.append(info.get_text())

            multi_list_of_stats = []
            multi_list_of_stats.append(variables[0:17])
            x = 0
            while x < len(names):
                multi_list_of_stats.append(data_row[0:17])
                del data_row[0:17]
                x = x + 1

            i = 0
            for key in names_dict_cards:
                names_dict_cards[key] = multi_list_of_stats[i]
                i = i + 1

            return names_dict_cards


def data_store_csv_Reds(year, names_dict_reds):
    # transfering data to CSV
    df = pd.DataFrame(names_dict_reds)
    df.to_csv("upload/Reds/cincyReds{}.csv".format(year), index=False)

def data_store_csv_Cards(year, names_dict_cards):
    # transfering data to CSV
    df = pd.DataFrame(names_dict_cards)
    df.to_csv("upload/Cardinals/StlCards{}.csv".format(year), index=False)



def main():
    year = 2002
    while year <= 2018:
        names_dict_reds = dataCollectorReds(year)
        data_store_csv_Reds(year, names_dict_reds)
        names_dict_cards = dataCollectorCardinals(year)
        data_store_csv_Cards(year, names_dict_cards)
        year = year + 1

if __name__ == '__main__':
    main()
