from math import sqrt
import concurrent.futures
import multiprocessing
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

if __name__ == "__main__":
    input_data = [i for i in range(10 ** 13, 10 ** 13 + 50000)]

    for n_workers in range(1,multiprocessing.cpu_count()+1):
        solucao_concorrente(n_workers)
        print('-'*30)
