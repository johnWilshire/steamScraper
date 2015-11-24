import sqlite3 as lite
import sys

# makes the to be scraped database 
con = lite.connect('toScrape.db')
c = con.cursor()
c.execute("CREATE TABLE toScrape(id INTEGER);")
c.execute("INSERT INTO toScrape (steamid) VALUES (76561197960435530);")
c.commit()
conn.close()