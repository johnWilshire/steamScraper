#!/bin/usr/python

# class that holds information about the player db
# and implents update functions

class Players:
    def __init__(self, connection):
        self.connection = connection
        
    # checks to see if we have record of the player
    def inPlayers(self, pid):
        c = self.connection.cursor()
        q = (str(pid),)
        c.execute("SELECT EXISTS(SELECT 1 FROM Players WHERE steamid=?);",q)
        return 1 == c.fetchone()[0]

    # returns a list of players with no ban information
    # these players are waiting to be scraped
    def getPBans(self):
        c = self.connection.cursor()
        c.execute("SELECT steamid FROM Players WHERE VACBanned IS NULL;")
        return c.fetchall()

    # returns a list of players which 
    # these players are waiting to be scraped
    def getNoGameInfo(self):
        c = self.connection.cursor()
        c.execute("SELECT steamid FROM Players WHERE numberOfGames IS NULL;")
        return c.fetchall()

    def getCols(self):
        c = self.connection.cursor()
        c.execute("PRAGMA table_info(Players);")
        return [str(col[1]) for col in c.fetchall()]

    # adds a text column into the playerdb corrosponding to a genre or classification category 
    def addCol(self, colName):
        c = self.connection.cursor()
        c.execute("PRAGMA table_info(Players);")
        return [str(col[1]) for col in c.fetchall()]