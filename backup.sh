name=`date +%d-%e-%g__%R`
echo $name
zip $name *.db
mv $name.zip ~/datasets/steamScraperBackUps