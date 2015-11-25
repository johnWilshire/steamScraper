#!/bin/usr/python
import urllib2
import json
import sqlite3 as lite
import sys
import re

from lib.steamUrl import SteamUrl
from lib.player import Player
from lib.queue import Queue
from lib.gender import Gender
from players import Players


def main():
    # load the key
    keyFile = open("keyfile.txt")
    key = keyFile.readlines()[0].rstrip()
    keyFile.close()

    # setup objects
    urlGen = SteamUrl(key)
    queue = Queue(lite.connect("toScrape.db"))
    players = Players(lite.connect("players.db"))
    gender = Gender(lite.connect("gender.db"))
    addSummaries(key, urlGen, queue, players, gender)



# scrapes player summaries getting players from the queue.db and adding them to players.db
def addSummaries(key, urlGen, queue, players, gender):    
    # read number of records to pull
    numScrape = 10 
    if len(sys.argv) == 2:
        numScrape = int(sys.argv[1])

    while (numScrape > 0):
        pid = queue.next()
        player = Player(getPlayerInfo(urlGen, pid), players.connection)
        print "player", player.steamid, numScrape
        if not player.isPrivate():
            player.addPlayerInfoToDB()
            player.addGender(gender)
            friends = getFriendIds(urlGen, pid)
            player.addNumFriends(len(friends))
            for friend in friends:
                if not (queue.inQueue(friend) or players.inPlayers(friend)):
                    queue.push(friend)
        queue.free(pid)
        numScrape -= 1

# gets player info 
def getPlayerInfo(urlGen, pid):
    pid = str(pid)
    url =  urlGen.playerSummary(pid)
    response = urllib2.urlopen(url)
    jsons = json.loads(response.read())
    if "response" in jsons:
        response = jsons["response"] 
        info = response["players"][0]
        return info
    else: 
        return "none" 

# returns a list of friends that the users has
def getFriendIds(urlGen, pid):
    pid = str(pid)
    url =  urlGen.friendsList(pid)
    response = urllib2.urlopen(url)
    jsons = json.loads(response.read())
    if "friendslist" in jsons:
        friendsRaw = jsons["friendslist"]["friends"]
        friends  = list()
        for friend in friendsRaw:
            friends.append(int(friend["steamid"]))
        return friends
    else:
        return "none"

## returns a list of game ids that have non zero playtime for the give player
def getPlayersGames(urlGen, pid):
    pid = str(pid)
    url =  urlGen.getOwnedGames(pid)
    response = urllib2.urlopen(url)
    jsons = json.loads(response.read())
    if "response" in jsons:
        response = ["response"]
        if response != {}: 
            games = response["games"]
            gameCount = "game_count"
            return games
    else: return "none" 

if __name__ == '__main__':
    main()