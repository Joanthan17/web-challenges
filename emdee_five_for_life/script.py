#!/usr/bin/python3

### attention: may need to run twice to get the flag (first sess drag a bit)


import hashlib
import requests
import re


def strip_html(html, pattern):
	return re.sub(pattern, "", html).strip("\n")



### getting the random string 

url = "http://178.128.160.242:31991"
pattern = re.compile('<.*?>') 
req = requests.session()
rget_html = req.get(url).text		
html_get = strip_html(rget_html, pattern)		# cleaning html tags
plain_txt = html_get.split("string")[1]
print("random string generated: " + plain_txt)


### md5 hash it

md_hash = hashlib.md5(plain_txt.encode()).hexdigest() # encode to bytes, then md5, then hex
print("md5 hash value: " + md_hash)


### sending hash via POST request

heads = {'User-Agent': 'Mozzila/5.0'}
payload = {'hash' : md_hash}

rpost = req.post(url, headers = heads, data = payload).text
html_post = strip_html(rpost, pattern)
flag = html_post.split("HTB")[1]
print("Flag: HTB" + flag)


