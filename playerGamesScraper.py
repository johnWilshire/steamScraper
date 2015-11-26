#!/bin/usr/python

# writes games and playtime to a json
# will need to seperate dataset into smaller chuncks if I run out of memeory

import sys
import json
import urllib2
import re

from lib.steamUrl import SteamUrl

def main():
    # read in the ids
    f = open("statesPlayers.csv")
    heading = f.readline()
    ids = [ re.split(",", line.rstrip())[1] for line in f.readlines()]
    ids = [re.sub('"','', steamid) for steamid in ids]

    # read in the steam api key
    keyFile = open("keyfile.txt")
    keys = keyFile.readlines()
    steamKey = keys[0].rstrip()

    urlGen = SteamUrl(steamKey)
    i = 0
    ids = ids[:1000]
    players = list()
    log = open("errors.log", "w")
    #
    with open("playerGames.json", "w") as myFile:
        # check which users are in our db
        for steamid in ids:
            player = dict()
            player["steamid"] = steamid
            url = urlGen.getOwnedGames(steamid)
            response = urllib2.urlopen(url)
            response = json.loads(response.read())["response"]
            if "games" in response and "game_count" in response:
                player["ownedGames"] = response["game_count"]
                for game in response["games"]:
                    appid = str(game["appid"])
                    player[appid] = game["playtime_forever"]
                    if "playtime_2weeks" in game:
                        player[appid + "_2weeks"] = game["playtime_2weeks"]
                    player[appid] = game["playtime_forever"]
                players.append(player)
                print steamid, len (ids) - i
            else:
                print "\t", steamid, "has no games or gamecount"
                log.write("%s ,has no games or gamecount" % (steamid))
            i += 1

        myFile.write(json.dumps(players))

if __name__ == '__main__':
    main() 