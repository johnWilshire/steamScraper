library(RSQLite)
library(jsonlite)
playerdb <- dbConnect(SQLite(), dbname="old_players.db")
players <- dbReadTable(playerdb, "Players")
players$gender <- as.factor(players$gender)
players$gender[players$gender == ""] <- "None"
np <-nrow(players)

gendered <- players[players$gender != "None",]
ngend <- nrow(gendered)

confident <- gendered[gendered$genderConf > 0.9,]
confidentCountry <- confident[confident$loccountrycode != "" ,]
confidentAmericans <- confident[confident$loccountrycode == "US" ,]
#write.csv(confidentCountry$steamid, "confidentCountry.csv", row.names = FALSE)

# this takes a while
genres <- fromJSON('players_games.json')
genres[is.na(genres)] <- 0
playerGenres <- cbind(confidentCountry,genres)
# to makes sure that we have matched up players correctly
table(playerGenres[,113] == playerGenres$steamid)
