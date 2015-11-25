#!/bin/bash
# remove on production server
rm players.db toScrape.db playersGames.db friendsList.db
python makeDB/makePlayerDb.py
python makeDB/makeToScrape.py
python makeDB/makePlayersGames.py
python makeDB/makeFriendsList.py
python scraper.py