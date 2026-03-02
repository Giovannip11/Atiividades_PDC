import threading
import time 


exitFlag = 0

class MyThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name=name
        self.counter = counter

    def print_time(self,threadName,counter,delay):
        while counter:
            if exitFlag:
                threadName.exit()
            time.sleep(delay)
            print('%s:%s' % (threadName,time.ctime(time.time())))
            counter -=1
    def run(self):
        print('Iniciando' + self.name)
        self.print_time(self.name,self.counter,5)
        print('Finalizando' + self.name)

thread_01=MyThread(1,' Thread_01',1)
thread_02=MyThread(1,' Thread_02',1)

thread_01.start()
thread_02.start()

print('Saindo do Thread principal.')
