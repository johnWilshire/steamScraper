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
from lib.friends import Friends
from lib.players import Players


def main():
    # load the key
    keyFile = open("keyfile.txt")
    keys = keyFile.readlines()
    steamKey = keys[0].rstrip()
    genderKey = keys[1].rstrip()
    keyFile.close()

    # setup objects
    urlGen = SteamUrl(steamKey)
    queue = Queue(lite.connect("toScrape.db"))
    players = Players(lite.connect("players.db"))
    gender = Gender(lite.connect("gender.db"), genderKey)
    friends = Friends(lite.connect("friendsList.db"))
    #print getPlayersGames(urlGen, queue.next())
    addSummaries(urlGen, queue, players, gender, friends)

#TODO things



# scrapes player summaries getting players from the queue.db and adding them to players.db
def addSummaries(urlGen, queue, players, gender,friends):    
    # read number of records to pull
    numScrape = 10 
    if len(sys.argv) == 2:
        numScrape = int(sys.argv[1])

    while (numScrape > 0):
        pid = queue.next()
        player = Player(getPlayerInfo(urlGen, pid), players.connection)
        if not player.isPrivate():
            player.addPlayerInfoToDB()
            player.addGender(gender)
            friendsList = getFriendIds(urlGen, pid)
            if friendsList != "none": 
                player.addNumFriends(friendsList)
                friends.addFriends(pid, friendsList)
            print "player name: ", player.firstName, player.gender, player.genderConf, "friends",player.numFriends, " remaining: ", numScrape
            for friend in friendsList:
                if not (queue.inQueue(friend) or players.inPlayers(friend)):
                    queue.push(friend)
        queue.free(player.steamid)
        numScrape -= 1

# gets player info 
def getPlayerInfo (urlGen, pid):
    pid = str(pid)
    url =  urlGen.playerSummary(pid)
    response = urllib2.urlopen(url)
    jsons = json.loads(response.read())
    if "response" in jsons:
        response = jsons["response"] 
        return response["players"][0]
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
            friends.append(str(friend["steamid"]))
        return friends
    else:
        return "none"

## returns a list of game ids  and playtimes playtime for the give player
def getPlayersGames(urlGen,player):
    pid = str(player)
    url =  urlGen.getOwnedGames(pid)
    response = urllib2.urlopen(url)
    jsons = json.loads(response.read())
    if "response" in jsons:
        response = jsons["response"]
        if response != {}: 
            games = response["games"]
            gameCount = "game_count"
            return games
    else: return "none" 


# TODO Games db update games db

if __name__ == '__main__':
    main()