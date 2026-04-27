import asyncio
import threading
import time

import aiohttp


def tarefa_pesada(id):
    print(f"Iniciando tarefa pesada {id}")
    time.sleep(2)
    print(f"Tarefa pesada {id} concluida.")


async def baixar_pagina(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resposta:
            conteudo = await resposta.text()
            print(f"Conteudo da {url}: {conteudo[:100]}...")


def run_asyncio_loop(urls):
    asyncio.run(main(urls))


async def main(urls):
    start_time = time.time()
    tarefas = [baixar_pagina(url) for url in urls]
    await asyncio.gather(*tarefas)

    elapsed_time = time.time() - start_time
    print(f"Tempo total com coroutines: {elapsed_time:.2f} segundos")


def main_threaded():
    urls = [
        "http://viacep.com.br/ws/01001000/json/",
        "http://viacep.com.br/ws/01001000/json/",
        "http://viacep.com.br/ws/01001000/json/",
    ]
    start_time = time.time()

    threads = []
    for i in range(3):
        thread = threading.Thread(target=tarefa_pesada, args=(i,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
        asyncio_thread = threading.Thread(target=run_asyncio_loop, args=(urls,))
        asyncio_thread.start()
        asyncio_thread.join()

        elapsed_time = time.time() - start_time
        print(f"Tempo total com threads e tarefas pesadas: {elapsed_time:.2f}segundos")


print("Iniciando execucao com threads...")
main_threaded()
