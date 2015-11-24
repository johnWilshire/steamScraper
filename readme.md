#  A scraper to collect user data from steam

see: [This wiki](https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_.28v0002.29 )

Please abide by the [steam api](http://steamcommunity.com/dev) terms of use


# API Key

store your api key in a file called "keyfile.txt"

# Databases 

databases are in sqlite

### players.db

database of players and their information, games played, bans

Field | Type | Comment
--- | --- | --- 
steamid | INTEGER |
lastlogoff| INTEGER |
realname | TEXT |
firstname | TEXT |
gender | REAL| likelyhood of being male
timecreated | INTEGER |epoch time
numFriends | INTEGER |
friendList | BLOB | comma seperated friend ids of this player 
loccountrycode | TEXT | ex: "US"
locstatecode | TEXT | ex: "WA"
loccityid | INTEGER | ex: 3961
CommunityBanned | TEXT | true, false 
VACBanned | TEXT | true, false
NumberOfVACBans | INTEGER |
NumberOfGameBans | INTEGER |



### toScrape.db

database of player ids gained from friendslist

Field | Type | Comment
--- | --- | --- 
steamid  | INT | 


### games.db

games with non zero playtime are added 

Field | Type | Comment
--- | --- | --- 
appid | INT | 
name | TEXT |
releaseDate | INT |
genre | TEXT |
rating | TEXT |
Consumer Advice | TEXT
