import requests

#QUERY STRINGS - Way of passing a data to a server as a part of GET request
url5 = "https://icanhazdadjoke.com/search"

rsp = requests.get(
    url5,
    headers={"Accept": "application/json"},
    params={"term": "cat", "limit": 2}
)
d = rsp.json()
#print(d)
print(d["results"])