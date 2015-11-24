#!/bin/usr/python

# holds information about a player 

# player class 
class Player:
    def __init__(self, playerJson, connection):
        self.connection = connection
        self.steamid = str(playerJson["steamid"])
        self.privacy = int(playerJson["communityvisibilitystate"])
        self.realname = ""
        self.loccountrycode = ""
        self.locstatecode = ""
        self.loccityid = ""

        if "realname" in playerJson:
            try:
                self.realname = str(playerJson["realname"])
            except UniCodeEncodeError:
                self.realname = "unicode"
        if "loccountrycode" in playerJson:
            self.loccountrycode = str(playerJson["loccountrycode"])
        if "locstatecode" in playerJson:
            self.locstatecode = str(playerJson["locstatecode"])
        if "loccityid" in playerJson:
            self.loccityid = str(playerJson["loccityid"])

    #returns a list, 0 is the insert statement, 1 is the parameter tuple
    def addPlayerInfoToDB(self):
        statement = """INSERT INTO Players 
            (steamid, realname,loccountrycode,locstatecode,loccityid)
            VALUES (?,?,?,?,?);"""
        c = self.connection.cursor()
        c.execute(statement,(self.steamid, self.realname, self.loccountrycode, self.locstatecode, self.loccityid))
        self.connection.commit()

    def addNumFriends(self, numFriends):
        numFriends = (numFriends , self.steamid, )
        statement = """UPDATE Players SET numFriends = ? WHERE steamid = ?;"""
        c = self.connection.cursor()
        c.execute(statement, numFriends)
        self.connection.commit()

    def isPrivate(self):
        return self.privacy == 1