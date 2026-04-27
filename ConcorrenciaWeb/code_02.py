import asyncio
import time

import aiohttp
from flask.sessions import SessionInterface


async def baixar_pagina(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resposta:
            conteudo = await resposta.text()
            print(f"Conteudo da {url}: {conteudo[:100]}...")


async def main():
    urls = [
        "http://viacep.com.br/ws/01001000/json/",
        "http://viacep.com.br/ws/01001000/json/",
        "http://viacep.com.br/ws/01001000/json/",
    ]
    start_time = time.time()

    tarefas = [baixar_pagina(url) for url in urls]
    await asyncio.gather(*tarefas)

    elapsed_time = time.time() - start_time
    print(f"Tempo total com coroutines: {elapsed_time:.2f}segundos")


asyncio.run(main())
