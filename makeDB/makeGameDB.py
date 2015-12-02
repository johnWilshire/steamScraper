import sqlite3 as lite

# makes the to be scraped database 
con = lite.connect('gameInfo.db')
c = con.cursor()
c.execute("""CREATE TABLE Games (
    appid TEXT,
    title TEXT,
    advice TEXT,
    genre TEXT
);""")
con.commit()
con.close()