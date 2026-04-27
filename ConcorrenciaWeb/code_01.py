import time

import requests


def baixar_pagina(url):
    resposta = requests.get(url)
    print(f"Conteuro da {url}: {resposta.text[:100]}...")


def main():
    urls = [
        "http://viacep.com.br/ws/01001000/json/",
        "http://viacep.com.br/ws/01001000/json/",
        "http://viacep.com.br/ws/01001000/json/",
    ]
    start_time = time.time()
    for url in urls:
        baixar_pagina(url)

    elapsed_time = time.time() - start_time
    print(f"Tempo total sem coroutines: {elapsed_time:.2f}segundos")


main()
