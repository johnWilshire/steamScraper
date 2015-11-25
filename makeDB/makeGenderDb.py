import sqlite3 as lite
import sys

# makes the to be scraped database 
con = lite.connect('gender.db')
c = con.cursor()
c.execute("CREATE TABLE Gender (name TEXT, gender TEXT, prob REAL, count INTEGER);")
c.execute("""INSERT INTO Gender (name, gender, prob, count) VALUES ('', 'None', 1.00, 0);""")

con.commit()
con.close()