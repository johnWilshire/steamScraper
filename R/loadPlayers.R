library(RSQLite)

playerdb <- dbConnect(SQLite(), dbname="players.db")
players <- dbReadTable(playerdb, "Players")

players$gender[players$gender == ""] <- "None"
np <-nrow(players)

gendered <- players[players$gender != "None",]
ngend <- nrow(gendered)

confident <- gendered[gendered$genderConf > 0.9,]
confidentCountry <- confident[confident$loccountrycode != "" ,]
confidentAmericans <- confident[confident$loccountrycode == "US" ,]

states <- confidentAmericans[ confidentAmericans$loctsatecode != "",]

nr = nrow(states)
#write.csv(confidentCountry$steamid, "confidentCountry.csv", row.names = FALSE)
nr / np
