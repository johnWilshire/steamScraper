##  A scraper to collect user data from steam

Please see: [This wiki](https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_.28v0002.29 ).

Please abide by the [steam api](http://steamcommunity.com/dev) terms of use.


### API Key

store your api key in the first line of a file called "keyfile.txt"
store your genderize key in the second line of the keyfile

if you do not have a genderize key modify the url in lib/gender.py

# Databases 

databases are in sqlite

### players.db

database of players and their information, games played, bans

Field | Type | Comment
--- | --- | --- 
steamid | INTEGER |
realName | TEXT |
gender | TEXT
genderConf | REAL | confidence of gender
numFriends | INTEGER |
numberOfGames |INTEGER |
games | TEXT | name of game table
loccountrycode | TEXT | ex: "US"
locstatecode | TEXT | ex: "WA"
loccityid | INTEGER | ex: 3961
CommunityBanned | TEXT | true, false 
VACBanned | TEXT | true, false
numberOfVACBans | INTEGER |
NumberOfGameBans | INTEGER |

The change of case is in steams api it is easier if we use what keys they use.


### toScrape.db

database of player ids gained from friendslist

Field | Type | Comment
--- | --- | --- 
steamid  | INTEGER | 

### playerGames.db

column for each game, time, row for each player
we will convert NA's to 0 in R

Field | Type | Comment
--- | --- | --- 
steamid | TEXT | 
app1 | TEXT |
app2 | INTEGER |
...

### games.db

games with non zero playtime are added 

Field | Type | Comment
--- | --- | --- 
appid | TEXT | 
name | TEXT |
releaseDate | INTEGER |
genre | TEXT |
rating | TEXT |
consumerAdvice | TEXT |

### friendsList.db

games with non zero playtime are added 

Field | Type | Comment
--- | --- | --- 
steamid | TEXT | 
friends | TEXT |