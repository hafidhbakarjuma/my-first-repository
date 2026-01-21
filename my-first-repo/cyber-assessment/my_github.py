#!/usr/bin/python3
import sys
import requests

url = "https://api.github.com/user"
r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))

if r.status_code == 200:
    print(r.json().get("id"))
else:
    print(None)
