import urllib2
import json
import sqlite3 as lite
import sys
import re

from steamUrl import SteamUrl

def main():
    keyFile = open("keyfile.txt")
    key = keyFile.readlines()[0].rstrip()
    urlGen = SteamUrl(key)

    #toScrapeCon = lite.connect("toScrape.db")
    friends =  getFriendIds(urlGen, "76561198052601146")
    print friends

def getFriendIds(urlGen,pid):
    url =  urlGen.friendsList(pid)
    response = urllib2.urlopen(url)
    data = response.read()
    friendsRaw = json.loads(data)["friendslist"]["friends"]
    friends  = list()
    for friend in friendsRaw:
        friends.append(int(friend["steamid"]))

    return friends

## returns a list of game ids and play times for that player
def getPlayersGames(urlGen,pid):
    url =  urlGen.friendsList(pid)
    response = urllib2.urlopen(url)
    data = response.read()
    friendsRaw = json.loads(data)["friendslist"]["friends"]
    friends  = list()
    for friend in friendsRaw:
        friends.append(int(friend["steamid"]))

    return friends
if __name__ == '__main__':

  main()