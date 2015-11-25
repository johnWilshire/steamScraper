import sqlite3 as lite
import sys

# makes the to be scraped database 
con = lite.connect('toScrape.db')
c = con.cursor()
c.execute("CREATE TABLE toScrape(steamid TEXT);")
c.execute("INSERT INTO toScrape (steamid) VALUES (76561197960435530);")
con.commit()
con.close()