import threading
import time

class MyThread(threading.Thread):
    def __init__(self,name,delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def thread_count_down(self,name,delay):
        counter = 5 
        while counter:
            time.sleep(delay)
            print('Thread %s counting down: %i...'%(name,counter))
            counter -=1

    def run(self):
        print('Iniciando thread %s.' %self.name)
        self.thread_count_down(self.name,self.delay)
        print('Finalizando thread %s'% self.name)

    
