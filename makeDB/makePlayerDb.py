import sqlite3 as lite
import sys

# makes the to be scraped database 
con = lite.connect('players.db')
c = con.cursor()
c.execute("""CREATE TABLE Players (
    steamid INTEGER,
    lastlogoff INTEGER,
    realname TEXT,
    firstname  TEXT,
    gender REAL,
    timecreated INTEGER,
    numFriends INTEGER,
    friendList BLOB,
    numberOfGames INTEGER,
    numberOfPlayedGames INTEGER,
    games BLOB, 
    loccountrycode TEXT,
    locstatecode TEXT,
    loccityid INTEGER,
    CommunityBanned TEXT,
    VACBanned TEXT,
    NumberOfVACBans INTEGER,
    NumberOfGameBans INTEGER
    );""")

con.commit()
con.close()