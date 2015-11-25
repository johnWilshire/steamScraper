genderdb <- dbConnect(SQLite(), dbname="gender.db")
gender <- dbReadTable(playerdb, "Genders")