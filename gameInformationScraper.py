#!/bin/usr/python

import sys
import re
import requests
import sqlite3 as lite
from bs4 import BeautifulSoup
import lxml
import time

def main():
    # read games to be read
    f = open("gamesToScrape.csv")
    heading = f.readline()
    appids = [ re.split(",", line.rstrip())[1] for line in f.readlines()]
    appids = [re.sub('"','', appid) for appid in appids]
    connection = lite.connect("gameInfo.db")
    appids = appids[99:200]
    i = 0
    for appid in appids:
        if not exists(connection, appid):
            
            url =  getInfoUrl(appid)
            htmls = requests.get(url).text
            soup = BeautifulSoup(htmls, 'lxml')
            trs = soup.find_all('tr')
            name = ""
            appType = ""
            genres = ""
            metacriticScore = ""
            appType = ""
            for tr in trs:
                td = re.split("\n+",tr.text)
                td = filter(None, td)
                if td[0] == 'Name' and name == "":
                    name = td[1]
                if td[0] == 'Genres' and genres == "":
                    genres = td[1]
                if td[0] == 'App Type' and appType == "":
                    appType = td[1]
                if td[0] == 'metacritic_score' and metacriticScore == "":
                    metacriticScore = td[1]
            print i, appid, name, genres, appType

            insertIntoDB(connection, appid, name, genres, metacriticScore, appType)
            time.sleep(1)
        i += 1




def getInfoUrl(appid):
    return "https://steamdb.info/app/" + appid + "/info/"

def insertIntoDB(connection, appid, name, genres, metacriticScore, appType):
    print "Inseting ", name, appid
    c = connection.cursor()
    q = (appid,name, genres,metacriticScore,appType)
    c.execute("INSERT INTO Games (appid,name,genres,metacriticScore, appType) VALUES (?,?,?,?,?);",q)
    connection.commit()

def exists(connection, appid):
    c = connection.cursor()
    q = (str(appid),)
    c.execute("SELECT EXISTS(SELECT 1 FROM Games WHERE appid=?);",q)
    return 1 == c.fetchone()[0]

if __name__ == '__main__':
    main()