#!/bin/usr/python
import urllib2
import json
import sqlite3 as lite
import sys
import re

from steamUrl import SteamUrl
from player import Player
from queue import Queue


def main():
    keyFile = open("keyfile.txt")
    key = keyFile.readlines()[0].rstrip()
    keyFile.close()
    urlGen = SteamUrl(key)

    queue = Queue(lite.connect("toScrape.db"))
    # todo players
    playersCon = lite.connect("players.db")
    
    numScrape = 10 
    if len(sys.argv) == 2:
        numScrape = int(sys.argv[1])
    #friends =  (urlGen, "76561198052601146")
    
    #pushFriendsToScrape(playersCon,toScrapeCon,friends + [76561197960435530])

    #print isWaitingToBeScraped(toScrapeCon,76561197960435530)
    while (numScrape > 0):
        pid = getNextToBeScraped(toScrapeCon)
        player = Player(getPlayerInfo(urlGen, pid))
        print "player", player.steamid
        if not player.isPrivate():
            player.addPlayerInfoToDB(playersCon)
            pushFriendsToScrape(playersCon, toScrapeCon, getFriendIds(urlGen, pid) )
        removeFromToBeScraped(toScrapeCon, pid)
        numScrape -= 1


# gets player info 
def getPlayerInfo(urlGen,pid):
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


# add friends that havent been scraped and are not in toBeScraped
# to the db toScrape
def pushFriendsToScrape(playersCon, toScrapeCon, friends):
    for friend in friends:
        if hasBeenScraped(playersCon, friend) or isWaitingToBeScraped(toScrapeCon, friend):
            print "\tnot adding ", friend
        else:
            print "\tadded ", friend, " to toScrape"
            queue.add(friend)


# returns a list of friends that the users has
def getFriendIds(urlGen,pid):
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
def getPlayersGames(urlGen,pid):
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

# checks to see if we have record of the player
def hasBeenScraped(playersCon, pid):
    c = playersCon.cursor()
    q = (str(pid),)
    c.execute("SELECT EXISTS(SELECT 1 FROM Players WHERE steamid=?);",q)
    return 1 == c.fetchone()[0]

# checks if the player is in the to scrape list
def isWaitingToBeScraped(toScrapeCon, pid):
    c = toScrapeCon.cursor()
    q = (str(pid),)
    c.execute("SELECT EXISTS(SELECT 1 FROM toScrape WHERE steamid=?);",q)
    return 1 == c.fetchone()[0]

# removes the player from the to be scraped db
def removeFromToBeScraped(toScrapeCon, pid):
    c = toScrapeCon.cursor()
    q = (str(pid),)
    c.execute("DELETE FROM toScrape WHERE steamid=?;",q)
    
# gets the next player to be scraped
def getNextToBeScraped(toScrapeCon):
    c = toScrapeCon.cursor()
    c.execute("SELECT steamid FROM toScrape;")
    return c.fetchone()[0]


def getSize
if __name__ == '__main__':

    main()