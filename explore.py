import asyncio
import concurrent.futures
import requests
import string

chars = string.ascii_lowercase

def wrapper(path):
    return requests.get("https://goteborgsvarvet.propublik.se/"+path, allow_redirects=False)

async def main():
    paths = []
    paths.extend([c for c in string.ascii_lowercase])
    while True:
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            loop = asyncio.get_event_loop()
            futures = [
                loop.run_in_executor(
                    executor,
                    wrapper,
                    path)
                for path in paths
            ]
        for response in await asyncio.gather(*futures):
            if response.status_code == 200:
                print (response.url)

        extension = []
        for path in paths:
            extension.extend([ c + path for c in chars ])
        paths = extension

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
