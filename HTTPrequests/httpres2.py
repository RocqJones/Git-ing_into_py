import requests
url = "https://www.google.com/"
response = requests.get(url)

print(f"Your request to {url} come with status code {response.status_code}")
print(response.text)