import requests

url = 'http://www.uvv.br'
res = requests.get(url)

#print(res.status_code)

#print(res.headers)

with open('uvv.br','w') as f:
    f.write(res.text)
    print('Done!')