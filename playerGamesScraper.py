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
    # get a list of user ids to scrape
    f = open("confidentCountry.csv")
    h = f.readline()
    print "filtering"
    toDo = [re.sub('"', '', line).rstrip() for line in f.readlines()]
    i = 0
    players = list()
    # loop through the steam ids
    for steamid in toDo:
        print "processing", i, "out of", len(toDo),'remaining:',len(toDo) - i
        response = getGamesList(games, urlGen, steamid)
        updates = dict() # updates to the player info are placed in this dict
        updates['steamid'] = steamid
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
                    cols = description[1]+ ", " + description[2]
                    cols = re.sub('-|\'|\.','',cols)
                    cols = re.sub('&','and',cols)
                    cols = re.split(', ', cols)
                    for col in cols: # update minutes
                        if col in updates:
                            updates[col] += playtime
                        else:
                            updates[col] = playtime
        i += 1
        players.append(updates)

    f = open('players_games.json','w')
    f.write(json.dumps(players))

# checks if a col exists in players db
def addCols(players, cols):
    existing = players.getCols()
    for col in cols:
        if not col in existing:
            print "adding col", col
            players.addCol(col)

#  checks the gamesList db for an entry with steamid
# parses and returns the json stored there
# else squerys the steam api and inserts the json into the db
def getGamesList(games, urlGen, steamid):
    gamesList =  games.getGames(steamid)
    if gamesList == None: 
        # query the api and insert the result
        r = urllib2.urlopen(urlGen.getOwnedGames(steamid))
        response = json.loads(r.read())["response"]
        games.addGames(steamid, json.dumps(response))
    else:
        response = json.loads(gamesList[1])
    return response

if __name__ == '__main__':
    main() 