#!/bin/usr/python

import sys
import re
import requests
import sqlite3 as lite
from bs4 import BeautifulSoup

class GameScraper:
    def __init__(self):
        self.connection = lite.connect("gameInfo.db")
    
    # gets teh 

    def getDescription(self,appid): 
        des = self.get(appid)
        if des != None:
            return des
        des = self.scrapeDescription(appid)
        self.insertIntoDB(appid, des[0], des[1], des[2])
        return des

    # returns the record if it exists
    def get(self, appid):
        c = self.connection.cursor()
        q = (str(appid),)
        c.execute("SELECT * FROM Games WHERE appid=?;",q)
        return c.fetchone()
    
    def insertIntoDB(self, appid, title, genre, advice):
        c = self.connection.cursor()
        q = (appid, title, genre, advice,)
        c.execute("INSERT INTO Games (appid,title,genre,advice) VALUES (?,?,?,?);",q)
        self.connection.commit()

    def scrapeDescription(self, appid):
        appid = str(appid)
        url = 'http://store.steampowered.com/app/' + appid
        print "scraping", url
        r = requests.get(url, cookies = {'birthtime': '568022401'})
        soup = BeautifulSoup(r.text,'lxml')
        parentalText  = soup.find( id = 'descriptorText').text
        advice = [ c.lower() for c in re.split(", | and |\n\r\n", parentalText)] 
        infoText = soup.find('div',{'class':'details_block'}).text
        title = ""
        genre = ""
        for info in re.split('\n+',infoText):
            if re.search('^Title: ',info):
                title = info[7:].lower()
            elif re.search('^Genre: ',info):
                genre = re.split(', ', info[7:].lower())
        return [advice,title,genre]

