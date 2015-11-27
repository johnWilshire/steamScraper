library(RSQLite)
gamesdb <- dbConnect(SQLite(), dbname="gameInfo.db")
gamesInfo <- dbReadTable(gamesdb, "Games")