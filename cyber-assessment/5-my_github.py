#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    data = response.json()
    print(data.get("id"))
