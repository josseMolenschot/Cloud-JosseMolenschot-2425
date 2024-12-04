APIKEY=$(curl -X POST "http://library.demo.local/api/v1/loginViaJSON" \
-H  "accept: application/json" \
-H  "Content-Type: application/json" \
-d "{  \"username\": \"cisco\",  \"password\": \"Cisco123!\"}")
echo $APIKEY
APIKEY=$(echo $APIKEY | cut -b 13-61)
echo $APIKEY