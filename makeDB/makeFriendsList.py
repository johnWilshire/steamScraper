import sqlite3 as lite

# makes the to be scraped database 
con = lite.connect('friendsList.db')
c = con.cursor()
c.execute("""CREATE TABLE FriendsList (
    steamid TEXT,
    friends TEXT
);""")

con.commit()
con.close()