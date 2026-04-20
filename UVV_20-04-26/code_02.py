import requests
import threading
import time

#site:httpstat.us


def ping(url):
    res = requests.get(url)
    print(f'{url}: {res.text}')


urls = [
    'https://tools-httpstatus.pickup-services.com/200',
    'https://tools-httpstatus.pickup-services.com/202',
    'https://tools-httpstatus.pickup-services.com/418',
    'https://tools-httpstatus.pickup-services.com/423',
    'https://tools-httpstatus.pickup-services.com/400',
    'https://tools-httpstatus.pickup-services.com/408',
    'https://tools-httpstatus.pickup-services.com/500',
    'https://tools-httpstatus.pickup-services.com/524',
    'https://tools-httpstatus.pickup-services.com/405',
    'https://tools-httpstatus.pickup-services.com/407',
    'https://tools-httpstatus.pickup-services.com/408',
    'https://tools-httpstatus.pickup-services.com/411'
]

start = time.time()

for url in urls:
    ping(url)
print(f'Sequential: {time.time() - start : .2f} seconds','/n')

start = time.time()

threads = []

for url in urls:
    thread = threading.Thread(target=ping, args=(url,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

print(f'Concurrent: {time.time() - start : .2f} seconds','/n')