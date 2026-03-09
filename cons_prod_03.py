import time
from threading import Thread , Event
import random

items = []

event = Event()

class consumidor(Thread):
    def __init__(self,items,event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        while True:
            time.sleep(2)
            self.event.wait()
            item = self.items.pop()
            print('Consumidor notificado: %d retirado da lista por %s' %(item,self.name))

    
class produtor(Thread):
    def __init__(self,items,event):
        Thread.__init__(self)
        self.items = items
        self.event = event
    def run(self):
        global item
        for i in range (100):
            time.sleep(2)
            item = random.randint(0,256)
            self.items.append(item)
            print('Produtor notificando: item N %d adicionando a lista por %s'%(item,self.name))
            print('Produtor notificando: evento definido por %s '% self.name)
            self.event.set()
            print('Produto notificando: evento apagado por %s \n')
            self.event.clear()

if __name__=='__main__':
    t1=produtor(items,event)
    t2=consumidor(items,event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()