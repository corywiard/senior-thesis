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
            variables = ['Name']
            player_variables = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for stats_variables in player_variables.find_all('th'):
                variables.append(stats_variables.get_text())

            # turns list into dictionary
            variables_dict = dict.fromkeys(variables)

            # collects all data from table
            stats_list = []
            player_stats = soup.find('div', attrs={'class': 'ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize'})
            for stats in player_stats.find_all('td'):
                stats_list.append(stats.get_text())


            # Organize the data
            # stores name in new list

            return stats_list
            #print(names)
            #print(variables)
            #with open('team', 'w') as f:

                # using csv.writer method from CSV package
                #write = csv.writer(f)

                #write.writerow(variables)
                #write.writerow(names)

def dataCollectorCardinals(year):
        # pull in web's source code
            url = "https://www.espn.com/mlb/team/stats/_/name/stl/season/{}/seasontype/2".format(year)
            html = urlopen(url)

            #print(url)

            soup = BeautifulSoup(html, "lxml")

            # collects variable names
            variables = ['Name']
            player_variables = soup.find('table', attrs={'class': 'Table Table--align-right'})
            for stats_variables in player_variables.find_all('th'):
                variables.append(stats_variables.get_text())

            # turns list into dictionary
            variables_dict = dict.fromkeys(variables)

            # collects all data from table
            stats_list_Cards = []
            player_stats = soup.find('div', attrs={'class': 'ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize'})
            for stats in player_stats.find_all('td'):
                stats_list_Cards.append(stats.get_text())


            # Organize the data
            # stores name in new list

            return stats_list_Cards


def data_store_csv_Reds(year, stats_list):
    # transfering data to CSV
    df = pd.DataFrame(stats_list)
    df.to_csv("upload/Reds/cincyReds{}.csv".format(year), index=False)

def data_store_csv_Cards(year, stats_list_Cards):
    # transfering data to CSV
    df = pd.DataFrame(stats_list_Cards)
    df.to_csv("upload/Cardinals/StlCards{}.csv".format(year), index=False)



def main():
    year = 2002
    while year <= 2018:
        stats_list = dataCollectorReds(year)
        data_store_csv_Reds(year, stats_list)
        stats_list_Cards = dataCollectorCardinals(year)
        data_store_csv_Cards(year, stats_list_Cards)
        year = year + 1

if __name__ == '__main__':
    main()
