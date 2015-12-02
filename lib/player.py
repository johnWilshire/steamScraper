#!/bin/usr/python

# holds information about a player 
import re
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
        self.firstName = ""
        self.gender = ""

        if "realname" in playerJson:
            try:
                self.realname = re.sub("[^\w ]","",str(playerJson["realname"]))
                self.realname = self.realname.lower()
                self.firstName = re.split(" ", self.realname)[0]
            except UnicodeEncodeError :
                self.realname = "unicode"
                self.privacy = 1
        if "loccountrycode" in playerJson:
            self.loccountrycode = str(playerJson["loccountrycode"])
        if "locstatecode" in playerJson:
            self.locstatecode = str(playerJson["locstatecode"])
        if "loccityid" in playerJson:
            self.loccityid = str(playerJson["loccityid"])

    def addPlayerInfoToDB(self):
        statement = """INSERT INTO Players 
            (steamid, realname, firstName, loccountrycode,locstatecode,loccityid)
            VALUES (?,?,?,?,?,?);"""
        c = self.connection.cursor()
        c.execute(statement,(self.steamid, self.realname, self.firstName, self.loccountrycode, self.locstatecode, self.loccityid))
        self.connection.commit()

    def addNumFriends(self, friends):
        self.numFriends = len(friends)
        tup = (self.numFriends , self.steamid, )
        statement = """UPDATE Players SET numFriends = ? WHERE steamid = ?;"""
        c = self.connection.cursor()
        c.execute(statement, tup)
        self.connection.commit()

    def isPrivate(self):
        return self.privacy == 1

    def addGender(self,gender):
        gen = gender.getGender(self.firstName)
        sex = str(gen[0])
        conf = str(gen[1])
        statement = """UPDATE Players SET gender = ?, genderConf = ? WHERE steamid = ?;""" 
        c = self.connection.cursor()
        c.execute(statement, (sex, conf, self.steamid,))
        self.gender = sex
        self.genderConf = conf
        self.connection.commit()