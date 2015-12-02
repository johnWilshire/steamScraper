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
    print "reading noInfo"
    noInfo = [str(steamid[0]) for steamid in players.getNoGameInfo()]
    # read a list of ids to scrape game information from
    print "reading country Codes"
    f = open("confidentCountry.csv")
    h = f.readline()
    print "filtering"
    #toDo = [re.sub('"', '', line).rstrip() for line in f.readlines() if re.sub('"', '', line).rstrip() in noInfo]
    toDo = ['76561197960265731']
    i = 0
    for steamid in toDo:
        print "processing", i, "out of", len(toDo)
        r = urllib2.urlopen(urlGen.getOwnedGames(steamid))
        response = json.loads(r.read())["response"]
        updates = dict()
        updates['numberOfGames'] = 0
        updates['totalTimePlayed'] = 0
        if "games" in response and "game_count" in response:
            updates['numberOfGames'] = response["game_count"]
            for app in response["games"]:
                appid = str(app["appid"])
                playtime = app["playtime_forever"]
                updates['totalTimePlayed'] += playtime
                if playtime != 0:
                    description = games.getDescription(appid)
                    if description == "moved":
                        continue
                    cols = description[1]+ ", " + description[2]
                    cols = re.split(', ', cols)
                    addCols(players,cols)
                    for col in cols: # update minutes
                        if col in updates:
                            updates[col] += playtime
                        else:
                            updates[col] = playtime
        
        for key in updates:
            players.updatePlayer(steamid, key, updates[key])
                    
        return

# hecks if a col exists
def addCols(players, cols):
    existing = players.getCols()
    for col in cols:
        if not col in existing:
            players.addCol(col)

if __name__ == '__main__':
    main() 