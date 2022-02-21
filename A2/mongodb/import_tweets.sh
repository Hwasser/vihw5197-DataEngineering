# Import all text-tweets into the mongodb
for file in ~/tweets/*.txt; do
  echo "Start importing file: $file"
  mongoimport -d test -c tweets --file "$file"
done

