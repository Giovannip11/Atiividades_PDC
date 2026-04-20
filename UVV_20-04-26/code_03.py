import requests
import threading
import time

class MyThread(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url = url
        self.result = None

    
    def run(self):
        res = requests.get(self.url)
        self.result = f('{self.url}: {res.text}')

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

threads = [urls]

start = time.time()
thread = [MyThread(url) for url in urls]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

for thread in threads:
    print(thread.result)

print(f'Concurrent: {time.time() - start : .2f} seconds','/n')
print("Done!")