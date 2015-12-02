name=`date +%d-%0e-%g__%R`
echo $name
zip $name *.db *.json
mv $name.zip ~/datasets/steamScraperBackUps