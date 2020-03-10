#!/usr/bin/python3

import requests

astros = requests.get("http://api.open-notify.org/astros.json")
inspace = []

for x in astros.json()["people"]:
    inspace.append(x['name'])
print(inspace)
