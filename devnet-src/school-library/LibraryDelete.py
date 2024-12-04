#!/usr/bin/env python3

import requests
import json


APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"
ID = input ("give id of book you want to delete: ")

def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth = authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")

def deleteBook(ID, apiKey):
    r = requests.delete(
        f"{APIHOST}/api/v1/books/{ID}", 
        headers = {
            "accept": "application/json",
            "X-API-Key": apiKey
            }
    )
    if r.status_code == 200:
        print(f"Book {r.json()} deleted.")
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}.")

# Get the Auth Token Key
apiKey = getAuthToken()

deleteBook(ID,apiKey=apiKey)
