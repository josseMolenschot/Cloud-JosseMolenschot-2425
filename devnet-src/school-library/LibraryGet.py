import requests

url = "http://library.demo.local/api/v1/books"
headers = {
    "accept": "application/json"
}

response = requests.get(url, headers=headers)

# Check the response
if response.status_code == 200:
    # Print the response content (if it's in JSON format)
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")
