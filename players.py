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

