import queue
import threading
import time

class MyThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name

    def run(self):
        print("Iniciando thread %s." % self.name)
        processando_fila()
        print("Encerrando thread %s." % self.name)


def processando_fila():
    while True:
        try:
            x = my_queue.get(block=False)
        except queue.Empty:
            return
        else:
            fatoracao(x)
        time.sleep(1)

def fatoracao(x):
    resultado = 'Fatores positivos %i sao: ' %x

    for i in range(1,x+1):
        if x % i==0:
            resultado += str(i) + ' '
    resultado += '\n' + '-' * 30
    print(resultado)

my_queue = queue.Queue()

input_ = [1,10,4,3]

for x in input_:
    my_queue.put(x)

thread1 = MyThread('A')
thread2 = MyThread('B')
thread3 = MyThread('C')

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print('\n','Concluido')
