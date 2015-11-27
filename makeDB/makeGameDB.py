import sqlite3 as lite

# makes the to be scraped database 
con = lite.connect('gameInfo.db')
c = con.cursor()
c.execute("""CREATE TABLE Games (
    appid TEXT,
    name TEXT,
    genres TEXT,
    appType TEXT,
    metacriticScore TEXT,
    rating TEXT,
    consumerAdvice TEXT
);""")
con.commit()
con.close()