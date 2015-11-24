#!/bin/usr/python


# player class 
class Player:
    def __init__(self,playerJson):
        self.steamid = int(playerJson["steamid"])
        self.privacy = int(playerJson["communityvisibilitystate"])
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
            self.loccityid = int(playerJson["loccityid"])

    #returns a list, 0 is the insert statement, 1 is the parameter tuple
    def getSqlSummaryInsert(self):
        return ["""INSERT INTO Players 
            (steamid, privacy,realname,loccountrycode,locstatecode,loccityid)
            VALUES (?,?,?,?,?,?,?);""", (self.steamid, self.privacy, self.realname, self.loccountrycode , self.locstatecode, self.loccityid )]