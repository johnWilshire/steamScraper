#!/bin/usr/python

# holds information about a player 

# player class 
class Player:
    def __init__(self,playerJson):
        self.steamid = str(playerJson["steamid"])
        self.privacy = str(playerJson["communityvisibilitystate"])
        self.realname = ""
        self.loccountrycode = ""
        self.locstatecode = ""
        self.loccityid = ""

        if "realname" in playerJson:
            self.realname = str(playerJson["realname"])
        if "loccountrycode" in playerJson:
            self.loccountrycode = str(playerJson["loccountrycode"])
        if "locstatecode" in playerJson:
            self.locstatecode = str(playerJson["locstatecode"])
        if "loccityid" in playerJson:
            self.loccityid = str(playerJson["loccityid"])

    #returns a list, 0 is the insert statement, 1 is the parameter tuple
    def addPlayerInfoToDB(self,playersCon):
        statement = """INSERT INTO Players 
            (steamid, realname,loccountrycode,locstatecode,loccityid)
            VALUES (?,?,?,?,?);"""
        c = playersCon.cursor()
        c.execute(statement,(self.steamid, self.realname, self.loccountrycode, self.locstatecode, self.loccityid))
        playersCon.commit()

    def isPrivate(self):
        return self.privacy == 1