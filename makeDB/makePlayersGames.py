import sqlite3 as lite

# makes the to be scraped database 
con = lite.connect('playersGames.db')
c = con.cursor()
c.execute("""CREATE TABLE PlayersGames (
    steamid TEXT
);""")

con.commit()
con.close()