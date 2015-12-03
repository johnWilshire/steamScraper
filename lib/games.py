#!/bin/usr/python

import sys
import re
import requests
import urllib
import sqlite3 as lite
from bs4 import BeautifulSoup

class GameScraper:
    def __init__(self):
        self.gamesDBCon = lite.connect("gameInfo.db")
        self.gamesListDBCon = lite.connect("gamesList.db")
    
    # gets the description from the games
    def getDescription(self,appid): 
        des = self.get(appid)
        if des != None:
            return des[1:]
        des = self.scrapeDescription(appid)
        self.insertIntoDB(appid, des[0], ", ".join(des[1]), ", ".join(des[2]))
        return self.get(appid)[1:]

    # returns the record if it exists
    def get(self, appid):
        c = self.gamesDBCon.cursor()
        q = (str(appid),)
        c.execute("SELECT * FROM Games WHERE appid=?;",q)
        return c.fetchone()
    
    # inserst a game into the db
    def insertIntoDB(self, appid, title, genre, advice):
        c = self.gamesDBCon.cursor()
        q = (appid, title, genre, advice,)
        c.execute("INSERT INTO Games (appid,title,genre,advice) VALUES (?,?,?,?);",q)
        self.gamesDBCon.commit()

    # scapes a description from store.steam frequently returns no advice which isnt really good enough
    def scrapeDescription(self, appid):
        appid = str(appid)
        url = 'http://store.steampowered.com/app/' + appid
        print ""
        print "scraping", url
        advice = [u'noAdvice']
        r = requests.get(url, cookies = {'birthtime': '568022401'})
        if len(r.history) == 1: # to handle redirected/moved games
            return ['moved',[u'noGenre'],advice]

        soup = BeautifulSoup(r.text,'lxml')
        adviceText = soup.find('p', {'id':'descriptorText'})
        if type(adviceText) != type(None):
            # filter regex clean magic
            advice = self.adviceCleaner(adviceText)
        if len(advice) == 0:
            advice = [u'noAdvice']
        
        tagText = soup.find('div',{'class':'glance_tags popular_tags'})
        if type(tagText) == type(None):
            title = u'regionLocked'
            genre = [u'noGenre']
        else:
            title = ''

            genre = [ 'genre_' + re.sub("\r|\t|\n","",link.string) for link in tagText.find_all('a')]
            genre = [ g.rstrip() for g in genre ]
            genre = [ re.sub(' +', '_', g).lower() for g in genre ]
            # take the first 4 genres 
            genre = genre[:10]

            # get the title
            infoText = soup.find('div',{'class':'details_block'})
            for info in re.split('\n+',infoText.text):
                if re.search('^Title: ',info):
                    title = info[7:].lower()
        
            # advice = self.scrapeClassification(title)
        return [title,genre, advice]

    # in general the parental ratings from steam were awful
    # so we are going to scrape the european pegi  website for a games classification    
    # I should have expected that 95% of the games on steam are indie tiles and are not classified lol
    def scrapeClassification (self, name):
        print "scraping classification for ", name
        s = urllib.urlencode({'searchString': name, 'platforms':'PC'})
        url = "http://www.pegi.info/en/index/global_id/505/?" + s
        print url
        r = requests.get(url)
        soup = BeautifulSoup(r.content)
        divs = soup.find_all('div', {'style':'width:425px;'})
        print ""
        if len(divs) == 0:
            print "no advice found"
            return [u'noAdvice']
        else: 
            # the first one should be the correct one
            ok = False
            for div in divs:
                if type(div.strong) != type(None):
                   print div.strong.text, name
                   if div.strong.text == name:
                        print name
                        ok = True
                if re.search('.*contains: ', div.text) and ok:
                    text = div.text
                    text = re.sub('.*contains: ','', text)
                    advice = re.split(' - ', text)
                    advice = [re.sub(' +', '_', a).lower() for a in advice]
                    advice = [re.sub('.*online.*', 'online', a) for a in advice]
                    return advice
        return [u'noAdvice']

    # given a players steamid returns the entry in the games list if there is one
    # can == with None to check if we have an entryjson
    def getGames(self, steamid):
        c = self.gamesListDBCon.cursor()
        q = (str(steamid),)
        c.execute("SELECT * FROM GamesList WHERE steamid=?;",q)
        return c.fetchone()

    # takes the json response of the from the steam api and adds it to the db
    def addGames(self, steamid, gamesList):
        tup = (str(steamid), gamesList,  )
        statement = """INSERT INTO GamesList (steamid, games) VALUES (?,?);"""
        c = self.gamesListDBCon.cursor()
        c.execute(statement, tup)
        self.gamesListDBCon.commit()

    # cleans the scraped advice
    def adviceCleaner(self, adviceText):
        adviceText = adviceText.text.lower().rstrip().lstrip()
        adviceText = re.sub('blood and gore', 'blood_and_gore', adviceText)
        adviceText = re.sub('gaming', '', adviceText)
        adviceText = re.sub('animdated', 'animated', adviceText)
        adviceText = re.sub('oflcdescriptors', 'noAdvice', adviceText)
        advice = re.split('[,;] | and |[\r\n\t]+', adviceText)
        advice = [re.sub('.*content is mild.*', 'mild_content', a) for a in advice ]
        advice = [re.sub('.*online.*', 'online_play', a) for a in advice ]
        advice = [re.sub(' ', '_', a) for a in advice ]
        advice = [re.sub('[^\w]', '', a) for a in advice ]
        advice = [re.sub('^\d+$', 'age_' + a + '_plus', a) for a in advice]
        advice = filter(None, advice) # remove empty entries
        return advice

def main():
    s = GameScraper()
    test = [6860]
    for t in test:
        print s.scrapeDescription(str(t))

if __name__ == '__main__':
    main()

