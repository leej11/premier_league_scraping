# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 16:39:46 2018

@author: Liam
"""
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import urllib.request
import os

print(os.getcwd())
os.chdir('C:/Users/Liam/Documents/Anki/Football/')
os.mkdir('Leicester')
os.chdir('Leicester')
print(os.getcwd())


# Get a list of all the premier league clubs and the href for their squads
page = requests.get('https://www.premierleague.com/clubs')
soup = BeautifulSoup(page.text, 'html.parser')
links = soup.find_all(href=re.compile("clubs/\d{1,2}"))

squads = []
for link in links:
    squads.append('https://www.premierleague.com' + link['href'].replace('overview', 'squad'))


for squad in squads:
    page = requests.get('https://www.premierleague.com/clubs/26/Leicester-City/squad')
    soup = BeautifulSoup(page.text, 'html.parser')

    # Player links list
players = []

for a in soup.find_all(class_="playerOverviewCard"):
    players.append('https://www.premierleague.com' + a.get('href'))
    

players_db = {}


for player in players:
    player_page = requests.get(player)
    soup = BeautifulSoup(player_page.text, 'html.parser')
    img = soup.select_one('.imgContainer img')
    img['src'] = img['src'].replace('Photo-Missing', img['data-player'])
    print('Adding {}'.format(img['alt']))
    players_db[img['alt']] = {}
    players_db[img['alt']]['link'] = player
    players_db[img['alt']]['source'] = img['src']
    
    try:
        urllib.request.urlretrieve('https:' + str(img['src']), str(img['alt']) + '.png')
    except:
        print("No image available for {}".format(img['alt']))


my_dictionary_pd = pd.DataFrame.from_dict(my_dictionary, orient='index')




# Downloading the image using urllib request

urllib.request.urlretrieve("https://platform-static-files.s3.amazonaws.com/premierleague/photos/players/250x250/p51940.png", "football_image.png")

