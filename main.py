from math import sqrt
import concurrent.futures
import multiprocessing
import matplotlib.pyplot as plt
import numpy as np
from timeit import default_timer as timer


def eh_primo(x):
    if x < 2:
        return False
    if x==2:
        return x
    if x%2==0:
        return False

    limit = int(sqrt(x)+1)
    for i in range(3,limit,2):
        if x % i == 0:
            return False
    return x


def solucao_concorrente(n_workers):
    print('Numero de processadores:  %i.'% n_workers)

    start = timer()
    result = []

    with concurrent.futures.ProcessPoolExecutor(max_workers=n_workers) as executor:
        futures = [executor.submit(eh_primo, i) for i in input_data]
        completed_futures= concurrent.futures.as_completed(futures)

        sub_start = timer()

        for i, future in enumerate(completed_futures):
            if future.result():
                result.append(future.result())
        sub_duration = timer() - sub_start

    duration = timer() - start
    print('Duracao intermediaria: %.4f seconds'  % sub_duration)
    print('Duracao total: %.4f seconds' % duration)
    return duration

def image_generator(x, y):
    plt.figure(figsize=(10, 5),facecolor='w', edgecolor='k')
    plt.plot(x, y)
    plt.xlabel('Número de Processadores')
    plt.ylabel('Tempo (s)')
    plt.title('Tempo de Execução vs Número de Processadores')
    plt.grid()
    plt.savefig('tempo_execucao.png')
    plt.show()



if __name__ == "__main__":
    input_data = [i for i in range(10 ** 13, 10 ** 13 + 100000)]
    processadores = []
    tempos = []

    for n_workers in range(1,multiprocessing.cpu_count()+1):
        duration = solucao_concorrente(n_workers)
        tempos.append(duration)
        processadores.append(n_workers)
        print('-'*30)
    
    image_generator(processadores, tempos)
