library(jsonlite)
games <- fromJSON("playerGames.json")
names <- colnames(games)
names <- names[-grep("_2",names)]
names <- names[-grep("steam",names)]

write.csv(names,"gamesToScrape.csv")
