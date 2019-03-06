import asyncio
import concurrent.futures
import requests
import string

chars = string.ascii_lowercase

paths = []
paths.extend([c for c in string.ascii_lowercase])
while True:
    for path in paths:
        # print("Trying " + path)
        resp = requests.get("https://goteborgsvarvet.propublik.se/"+path, allow_redirects=False)
        if resp.status_code == 200:
            print(path)
    extension = []
    for path in paths:
        extension.extend([ c + path for c in chars ])
    paths = extension
