name=`date +%d-%e-%g__%R`
echo $name
zip $name *.db *.json
mv $name.zip ~/datasets/steamScraperBackUps