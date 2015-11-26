#!/bin/usr/python

import sys
import re
import urllib2

def main():
    # read games to be read
    f = open("statesPlayers.csv")
    heading = f.readline()
    ids = [ re.split(",", line.rstrip())[1] for line in f.readlines()]
    ids = [re.sub('"','', steamid) for steamid in ids]



if __name__ == '__main__':
    main()