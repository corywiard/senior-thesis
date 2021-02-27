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

def example():
    url = "https://www.espn.com/mlb/team/stats/_/name/cin/season/2002/seasontype/2"
    html = urlopen(url)

    #print(url)

    soup = BeautifulSoup(html, "lxml")
