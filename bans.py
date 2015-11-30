#!/bin/usr/python

import urllib2
import json
import sqlite3 as lite
import sys

from lib.steamUrl import SteamUrl
from lib.players import Players

# this script reads the players in players.db and 
# for those that we do not have ban information about
# we query the steam api
def main():
    keyFile = open("keyfile.txt")
    keys = keyFile.readlines()
    steamKey = keys[0].rstrip()
    keyFile.close()

    urlGen = SteamUrl(steamKey)
    con = lite.connect("players.db")
    pcon = Players(con)
    players = [ str(p[0]) for p in pcon.getPBans()]
    num =  len(players)
    for i in range(len(players)/100 + 1):
        url = urlGen.getPlayersBans(players[i*100:(i+1)*100])
        response = urllib2.urlopen(url)
        banInfoList = json.loads(response.read())["players"]
        for info in banInfoList:
            steamid = info["SteamId"]
            cBanned = info["CommunityBanned"]
            vBanned = info["VACBanned"]
            nVBans = info["NumberOfVACBans"]
            nGBans = info["NumberOfGameBans"]
            eBan = info["EconomyBan"]
            insertBanInfo (con, steamid, cBanned, vBanned, nVBans, nGBans, eBan)
            print num
            num -= 1
        

def insertBanInfo (con, steamid, cBanned, vBanned, nVBans, nGBans, eBan):
    c = con.cursor()
    q = (cBanned, vBanned, nVBans, nGBans, eBan, steamid, )
    print "inserting", q
    c.execute("UPDATE Players SET CommunityBanned = ?, VACBanned = ?, NumberOfVACBans = ?, NumberOfGameBans = ?, economyBan = ? WHERE steamid = ?;",q)
    con.commit()

if __name__ == '__main__':
    main()