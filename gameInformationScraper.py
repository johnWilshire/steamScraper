#!/bin/usr/python

import sys
import re
import requests
import sqlite3 as lite
from bs4 import BeautifulSoup
import lxml


def main():
    # read games to be read
    f = open("gamesToScrape.csv")
    heading = f.readline()
    appids = [ re.split(",", line.rstrip())[1] for line in f.readlines()]
    appids = [re.sub('"','', appid) for appid in appids]

    appids = ["730"]

    for appid in appids:
        i = 0
        url =  getInfoUrl(appid)
        htmls = requests.get(url).text
        soup = BeautifulSoup(htmls, 'lxml')
        trs = soup.find_all('tr')
        metaCriticScore = trs[49].children[1]
        print meta_critic_score
        for row in trs[:50]:
            print ""
            print "index = ", i
            print row
            i += 1


def getInfoUrl(appid):
    return "https://steamdb.info/app/" + appid + "/info/"

def exists(connection, appid):
    c = connection.cursor()
    q = (str(appid),)
    c.execute("SELECT EXISTS(SELECT 1 FROM Games WHERE appid=?);",q)
    return 1 == c.fetchone()[0]

if __name__ == '__main__':
    main()