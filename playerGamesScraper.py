#!/bin/usr/python

# writes games and playtime to a json
# will need to seperate dataset into smaller chuncks if I run out of memeory

import sys
import json
import urllib2
import re
import sqlite3 as lite

from lib.steamUrl import SteamUrl

from lib.players import Players
from lib.games import GameScraper


def main():
    # read in the ids
    players = Players(lite.connect("players.db"))
    games = GameScraper()
    # read in the steam api key
    keyFile = open("keyfile.txt")
    keys = keyFile.readlines()
    steamKey = keys[0].rstrip()

    urlGen = SteamUrl(steamKey)
    # get a list of user ids without game information
    noInfo = [str(steamid[0]) for steamid in players.getNoGameInfo()]
    # read a list of ids to scrape game information from
    f = open("confidentCountry.csv")
    h = f.readline()
    needed = [re.sub('"', '', line).rstrip() for line in f.readlines()]
    # find the intersection of these lists
    toDo = list()
    for steamid in needed:
        if steamid in noInfo:
            toDo.append(steamid)
    i = 0
    for steamid in toDo:
        print "processing", i, "out of", len(toDo)
        r = urllib2.urlopen(urlGen.getOwnedGames(steamid))
        response = json.loads(response.read())["response"]
        gameCount = 0
        if "games" in response and "game_count" in response:
            gameCount = response["game_count"]
            for game in response["games"]:
                appid = str(game["appid"])
                playtime = game["playtime_forever"]
        else:
            print "\t", steamid, "has no games or gamecount"
            
        return

if __name__ == '__main__':
    main() 