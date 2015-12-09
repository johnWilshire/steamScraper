#!/bin/usr/python

# class that implents a bounded queue with sqlite
# might not actually be a queue (it doesnt really matter for my purpose)

class Queue:
    def __init__(self, connection):
        self.connection = connection
        c = self.connection.cursor()
        c.execute("SELECT Count (*) FROM toScrape;")
        self.count = c.fetchone()[0]
        self.wait = 0
        if self.count > 1000:
            self.wait = 300
    
    # checks if the player is in the to scrape list
    def inQueue(self, pid):
        c = self.connection.cursor()
        q = (str(pid),)
        c.execute("SELECT EXISTS(SELECT 1 FROM toScrape WHERE steamid=?);",q)
        return 1 == c.fetchone()[0]

    # removes the player from the to be scraped db
    def free(self, pid):
        c = self.connection.cursor()
        q = (str(pid),)
        c.execute("DELETE FROM toScrape WHERE steamid=?;",q)
        self.count -= 1
        
    # gets the next player to be scraped
    def next(self):
        c = self.connection.cursor()
        c.execute("SELECT steamid FROM toScrape;")
        return c.fetchone()[0]

    # adds a value to the queue thing
    def push(self, friend):
        if self.wait > 0:
            self.wait -= 1
        else:
            self.count += 1
            if self.count > 1000:
                self.wait = 300
            c = self.connection.cursor()
            q = (friend,)
            c.execute("INSERT INTO toScrape (steamid) VALUES (?)", q);
            self.connection.commit()
