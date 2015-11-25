#!/bin/bash

while true; do 
    ls -lh players.db toScrape.db gender.db friendsList.db
    echo 
    date | cut -d\  -f4
    sleep 3
done