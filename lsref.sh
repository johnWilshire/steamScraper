#!/bin/bash

while true; do 
    ls -Slh | head -5
    date | cut -d\  -f4
    echo
    sleep 1
done