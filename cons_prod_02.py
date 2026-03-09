from threading import Thread , Condition
import time

items = []

condition = Condition()

class consumidor(Thread):
    def __init__(self):
        Thread.__init__(self)
    def consume(self):
        global condition
        global items

        condition.acquire()

        if len (items) == 0:
            condition.wait()
            print("Consumidor notificando: nenhum item a consumir")
        
        items.pop()
        print("Consumidor notificando: consumindo 1 item")
        print("Consumidor notificado: itens a consumir sao "+ str(len(items)))
        condition.notify()
        condition.release()

    def run(self):
        for i in range(0, 20):
            time.sleep(10)
            self.consume()
class produtor(Thread):
    def __init__(self):
        Thread.__init__(self)

    def produce(self):
        global condition
        global items
        condition.acquire()

        if len (items) == 10:
            condition.wait()
            print("Produtor notificado: itens produzidos sao "+ str(len(items)))
            print("Produtor notificado: producao interrompida!!")
        items.append(1)
        print("Produtor  notificado: total de items produzidos "+str(len(items)))
        condition.notify()
        condition.release()
    def run(self):
        for i in range (0,20):
            time.sleep(5)
            self.produce()

if __name__ == "__main__":
    producer=produtor()
    consumer=consumidor()
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
