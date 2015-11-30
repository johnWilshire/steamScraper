library(ggplot2)
# run this after runing loadPlayers.R 
qplot(gendered$numFriends, fill=as.factor(gendered$gender))
qplot(countried$loccountrycode, fill=as.factor(countried$gender))

females <- gendered[gendered$gender == "female",]
males <- gendered[gendered$gender == "male",]
