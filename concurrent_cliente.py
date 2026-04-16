import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin
import time

BASE = "http://127.0.0.1:5000/"

def do_increment(session):
    # faz POST para /increment
    r = session.post(urljoin(BASE, "increment"), timeout=5)
    return r.status_code

def do_submit(session, payload):
    # faz POST para /submit com payload
    r = session.post(urljoin(BASE, "submit"), data={"q": payload}, timeout=5)
    return r.status_code

def run_increment_test(total_requests=200, workers=20):
    session = requests.Session()
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = [ex.submit(do_increment, session) for _ in range(total_requests)]
        for f in as_completed(futures):
            _ = f.result()
    # pegar valor final do contador
    r = session.get(urljoin(BASE, ""), timeout=5)
    print("Pa~gina final recebida (tamanho):", len(r.text))
    # extrair valor do contador simplificando: busca 'Valor do contador: <strong>X</strong>'
    start = r.text.find("Valor do contador:")
    if start != -1:
        snippet = r.text[start:start+200]
        print(snippet.split("<strong>")[-1].split("</strong>")[0].strip())

def run_submit_test(total_requests=50, workers=10, payload="<script>alert('XSS')</script>"):
    session = requests.Session()
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = [ex.submit(do_submit, session, payload) for _ in range(total_requests)]
        for f in as_completed(futures):
            _ = f.result()
    r = session.get(urljoin(BASE, ""), timeout=5)
    print("Numero de entradas mostradas (approx):", r.text.count("<li>"))

if __name__ == "__main__":
    print("Resetando servidor...")
    s = requests.Session()
    s.post(urljoin(BASE, "reset"))
    print("Executando teste de incrementos (200 requisicoes, 20 workers)...")
    t0 = time.time()
    run_increment_test(total_requests=200, workers=20)
    print("Tempo:", time.time()-t0)
    print("\nResetando e testando submissoes (stored XSS)...")
    s.post(urljoin(BASE, "reset"))
    run_submit_test(total_requests=50, workers=10)

