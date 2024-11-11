# %%
import requests
import json
import time

# %%
session = requests.Session()
headers = {
    "Content_Type":"application/json",
    "Accept":"application/json"
}

# %%
#AUTENTICAR

token = '47255cb8c8fc03bfdc7e7289afa121f8141d05e03036bf4826ef5358e97c6d90'
url_base='https://api.olhovivo.sptrans.com.br/v2.1/'

r = session.post(url_base+'Login/Autenticar?token='+token,headers=headers)

# %%
## GET

def _get(path):
    response = session.get(url_base+path)
    data = response.json()
    return data

# %%
## PEGAR LINHA

line = _get("Linha/Buscar?termosBusca=8000")
j = json.dumps(line,ensure_ascii=True)
data = json.loads(j)
print(data)