#!/usr/bin/env python3

DATE = "21 November 2019"
VERSION = "i"
AUTHOR = "Cory Wiard"
AUTHORMAIL = "wiardc@allegheny.edu"

import pandas as pd
import re
import requests
from bs4 import BeautifulSoup



def dataCollector():
    url = 'https://www.espn.com/mlb/player/stats/_/id/28670/joey-votto'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    header = soup.find_all('tr', attrs={'class': 'Table__sub-header Table__TR Table__even'})

    print(header)
