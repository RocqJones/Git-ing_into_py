import requests
url3 = "https://icanhazdadjoke.com/"

#resp = requests.get(url3)
#to get a plain text do
resp = requests.get(url3, headers={"Accept": "text/plain"}) #this is pretty amazing
#NOTE most websites doesn't use APIs which can make it display plain text but this does use APIs
print(resp.text)