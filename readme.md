##  A scraper to collect user data from steam

Please see: [This wiki](https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_.28v0002.29 ).

Please abide by the [steam api](http://steamcommunity.com/dev) terms of use.


### API Key

store your api key in a file called "keyfile.txt"

# Databases 

databases are in sqlite

### players.db

database of players and their information, games played, bans

Field | Type | Comment
--- | --- | --- 
steamid | INTEGER |
realName | TEXT |
gender | REAL| likelyhood of being male
timeCreated | INTEGER |epoch time
numFriends | INTEGER |
friendList | TEXT | json of friend steamids of thisplayer 
numberOfGames |INTEGER |
numberOfPlayedGames | INTEGER |
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


### games.db

games with non zero playtime are added 

Field | Type | Comment
--- | --- | --- 
appid | INTEGER | 
name | TEXT |
releaseDate | INTEGER |
genre | TEXT |
rating | TEXT |
consumerAdvice | TEXT
