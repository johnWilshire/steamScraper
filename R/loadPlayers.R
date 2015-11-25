library(RSQLite)

playerdb <- dbConnect(SQLite(), dbname="players.db")
players <- dbReadTable(playerdb, "Players")

players$gender[players$gender == ""] <- "None"
np <-nrow(players)

gendered <- players[players$gender != "None",]
ngend <- nrow(gendered)

confident <- gendered[gendered$genderConf > 0.9,]

confidentAmericans <- confident[confident$loccountrycode == "US" ,]

states <- confidentAmericans[ confidentAmericans$locstatecode != "",]

states <- confidentAmericans[ confidentAmericans$locstatecode != "",]
cities <- states[states$loccityid != 0]
nr = nrow(states)

# nr / np

qplot()