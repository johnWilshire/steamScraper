#!/bin/bash
# remove on production server
rm players.db toScrape.db
python makeDB/makePlayerDb.py
python makeDB/makeToScrape.py
python scraper.py