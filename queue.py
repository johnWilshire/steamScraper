#!/bin/usr/python

# class that implents a queue with sqlite

class Queue:
    def __init__(self, connection):
        self.connection = connection
        c = self.connection.cursor()
        c.execute("SELECT Count (*) FROM toScrape;")
        count = c.fetchone()[0]

        # checks if the player is in the to scrape list
    def inQueue(pid):
        c = self.connection.cursor()
        q = (str(pid),)
        c.execute("SELECT EXISTS(SELECT 1 FROM toScrape WHERE steamid=?);",q)
        return 1 == c.fetchone()[0]

    # removes the player from the to be scraped db
    def free(pid):
        c = self.connection.cursor()
        q = (str(pid),)
        c.execute("DELETE FROM toScrape WHERE steamid=?;",q)
        
    # gets the next player to be scraped
    def next():
        c = self.connection.cursor()
        c.execute("SELECT steamid FROM toScrape;")
        return c.fetchone()[0]

    # adds a 
    def push(friend):
        c = toScrapeCon.cursor()
        q = (friend,)
        c.execute("INSERT INTO toScrape (steamid) VALUES (?)", q);
        self.connection.commit()
