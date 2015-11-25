library(RSQLite)

playerdb <- dbConnect(SQLite(), dbname="players.db")
players <- dbReadTable(playerdb, "Players")

playersdf$gender[df$gender == ""] <- "None"
