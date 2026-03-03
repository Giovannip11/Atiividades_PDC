import threading
from math import sqrt
from timeit import default_timer as timer


def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(sqrt(n + 1))
    for i in range(3, limit, 2):
        if n % i == 0:
            return False

    return True


class MyThread(threading.Thread):
    def __init__(self, inicio, fim, resultados, lock):
        super().__init__()
        self.inicio = inicio
        self.fim = fim
        self.resultados = resultados
        self.lock = lock

    def run(self):
        print(f"Iniciando Thread: {self.name}")
        for n in range(self.inicio, self.fim + 1):
            if eh_primo(n):
                with self.lock:
                    self.resultados.append(n)


def threading_manipulation(n_threads):
    print("Número de threads: %i" % n_threads)

    start = timer()

    resultados = []
    lock = threading.Lock()

    chunk_size = len(input_data) // n_threads
    threads = []

    for i in range(n_threads):
        inicio = i * chunk_size
        fim = (i + 1) * chunk_size - 1 if i < n_threads - 1 else len(input_data) - 1

        n_inicio = input_data[inicio]
        n_fim = input_data[fim]

        t = MyThread(n_inicio, n_fim, resultados, lock)
        threads.append(t)

    sub_start = timer()

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    sub_duration = timer() - sub_start
    duration = timer() - start

    print("Duração intermediária: %.4f seconds" % sub_duration)
    print("Duração total: %.4f seconds" % duration)
    print(f"Total de primos: {len(resultados)}")


if __name__ == "__main__":
    input_data = [i for i in range(10**6, 10**6 + 50000)]

    for n in range(1, 9):
        threading_manipulation(n)
        print("-" * 30)
