#when you type something to search from web browser the first thing that happens is
#We will use a module calls 'request' ... install it via commandline as "python3 -m pip install requests"
import requests #you can still run this on commandline
res = requests.get("https://www.ycombinator.com/")
res
#<Response [200]>
#res.header
#will output an xml or json text will all metadata that come out
#res.ok
#True or False