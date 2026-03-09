import threading
import time
import time

semaphoro = threading.Semaphore(0)

def produtor():
    global item
    time.sleep(10)
    item = random.randint(0,1000)
    print("Item produzido %s" %item)
    print("Produtor notificando: produzinoo item numero %s " %item)
    print("Chamando realese() para avisar que o item esta disponivel")
    semaphoro.realese()

def consumidor():
    print("Tentando consumir item...")
    print("Chamado acquire() e aguardando liberacao do produtor")
    semaphoro.acquire()
    print("Consumidor notificando: consumido item %s " % item)
    semaphoro.realese()
    print('\n')


if __name__ == '__main__':
    for i in range(0,5):
        t1 = threading.Thread(target=produtor)
        t2 = threading.Thread(target=consumidor)
        t1.start
        t2.start
        t1.join
        t2.join
    print("Programacao encerrado!")