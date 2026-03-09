import queue
import threading
import time


class MyThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name


    def run(self):
        print(f'Iniciando thread {self.name}')
        processando_fila()


priority_queue = queue.PriorityQueue()

def fatoracao(x):
    name_thread = threading.current_thread().name
    resultado = f'Fatores positivos {x}: '

    for i in range(1,x+1):
        if x % i == 0:
            resultado += str(i) + ' '
    
    print(f'[{name_thread}] {resultado}')
    print('_' * 30)

def processando_fila():
    while True:
        try:
            prioridade,numero = priority_queue.get(block=False)
        except queue.Empty:
            return
        else:
            print(f'Processando numero {numero} (prioridade {prioridade})')
            fatoracao(numero)
        time.sleep(2)

tarefas = [
    (3, 532),
    (1, 947),
    (4, 55),
    (2, 632),
    (1, 437),
    (5, 123),
    (2, 822),
    (3, 794)
]

for tarefa in tarefas:
    priority_queue.put(tarefa)


thread_01 = MyThread('A')
thread_02 = MyThread('B')
thread_03 = MyThread('C')

thread_01.start()
thread_02.start()
thread_03.start()


thread_01.join()
thread_02.join()
thread_03.join()

print("Algoritmo finalizado!")
