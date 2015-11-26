import sqlite3 as lite

# makes the to be scraped database 
con = lite.connect('playersGames.db')
c = con.cursor()
c.execute("""CREATE TABLE Games (
    appid TEXT,
    name TEXT,
    genres TEXT,
    score INTEGER,
    rating TEXT,
    consumerAdvice TEXT
);""")
con.commit()
con.close()