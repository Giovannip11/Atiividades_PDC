import threading
import time

import requests


class MyThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

        self.result = None

    def run(self):
        res = requests.get(self.url)
        self.result = f"{self.url}: {res.text}"


urls = [
    "http://httpstat.us/200",
    "http://httpstat.us/200?sleep=20000",
    "http://httpstat.us/400",
    "http://httpstat.us/404",
    "http://httpstat.us/408?sleep=5000",
    "http://httpstat.us/418",
    "http://httpstat.us/500?sleep=2000",
    "http://httpstat.us/524",
]

start = time.time()


threads = [MyThread(url) for url in urls]


for thread in threads:
    thread.start()


for thread in threads:
    thread.join()


for thread in threads:
    print(thread.result)

print(f"Threading {time.time() - start: .2f} seconds")
print("Done")
