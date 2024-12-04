APIKEY=$(curl -X POST "http://library.demo.local/api/v1/loginViaJSON" \
-H  "accept: application/json" \
-H  "Content-Type: application/json" \
-d "{  \"username\": \"cisco\",  \"password\": \"Cisco123!\"}")
echo $APIKEY
APIKEY=$(echo $APIKEY | cut -b 13-61)
echo $APIKEY


curl -X POST "http://library.demo.local/api/v1/books" -H  "accept: application/json" -H  "X-API-KEY: $APIKEY" -H  "Content-Type: application/json" -d "{  \"id\": 0,  \"title\": \"Book1\",  \"author\": \"Author1\"}"