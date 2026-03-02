import threading
import time
from math import sqrt


def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return n
    if n % 2 == 0:
        return False

    limit = int(sqrt(n + 1))
    for i in range(3, limit, 2):
        if n % i == 0:
            return False

    return n


class MyThread(threading.Thread):
    def __init__(self, inicio, fim, resultados):
        threading.Thread.__init__(self)
        self.inicio = inicio
        self.fim = fim
        self.resultados = resultados

    def run(self):
        print("Iniciando Thread: %s." % self.name)
        for n in range(self.inicio, self.fim + 1):
            if eh_primo(n):
                self.resultados.append(n)
