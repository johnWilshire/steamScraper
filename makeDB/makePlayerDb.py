import sqlite3 as lite
import sys

# makes the to be scraped database 
con = lite.connect('players.db')
c = con.cursor()
c.execute("""CREATE TABLE Players (
    steamid TEXT,
    realname TEXT,
    firstName TEXT,
    gender TEXT,
    numFriends INTEGER,
    friendList TEXT,
    numberOfGames INTEGER,
    numberOfPlayedGames INTEGER,
    games TEXT, 
    loccountrycode TEXT,
    locstatecode TEXT,
    loccityid INTEGER,
    CommunityBanned TEXT,
    VACBanned TEXT,
    NumberOfVACBans INTEGER,
    NumberOfGameBans INTEGER );""")

con.commit()
con.close()