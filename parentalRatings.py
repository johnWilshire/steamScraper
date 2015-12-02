#!/bin/urs/python

import requests
from bs4 import BeautifulSoup
import re

def main():
    baseurl = 'http://store.steampowered.com/app/'
    appid = '22300'

    r = requests.get(baseurl + appid)
    soup = BeautifulSoup(r.text,'lxml')

    tables = soup.find( id = 'descriptorText')
    description =  tables.text
    categories = [ c.lower() for c in re.split(", | and ", description)]
    print categories 


if __name__  == '__main__':
    main()