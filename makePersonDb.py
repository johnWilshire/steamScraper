import sqlite3 as lite
import sys

# makes the to be scraped database 
con = lite.connect('toScrape.db')
c = con.cursor()
c.execute("""CREATE TABLE Player (
    steamid INTEGER,
    lastlogoff INTEGER,
    realname TEXT,
    firstname  TEXT,
    gender REAL,
    timecreated INTEGER,
    numFriends INTEGER,
    friendList BLOB,
    loccountrycode TEXT,
    locstatecode TEXT,
    loccityid INTEGER,
    CommunityBanned TEXT,
    VACBanned TEXT,
    NumberOfVACBans INTEGER,
    NumberOfGameBans INTEGER
    );""")

c.commit()
conn.close()