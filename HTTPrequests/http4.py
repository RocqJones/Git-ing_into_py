import requests
url4 = "https://icanhazdadjoke.com/"

response = requests.get(url4, headers={"Accept": "application/json"})

#converting JSON of JS to python
dt = response.json()
print(type(dt)) #inform of dict
#print(response.json()) #prints the JSON script

print(dt["joke"])
print(f"status {dt['status']}")