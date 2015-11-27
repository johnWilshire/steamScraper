genderdb <- dbConnect(SQLite(), dbname="gender.db")
gender <- dbReadTable(genderdb, "Genders")