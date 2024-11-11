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

#Armazenar letreiros
letreiros_encontrados = []

#iterar sobre os numeros 1 a 89
for i in range(1,99):
    linhas_url = f"{url_base}/Linha/Buscar?termoBusca={i}"
    linhas_response = requests.get(linhas_url)
    linhas = linhas_response.json()

    #adicionar letreiros encontrados à lista
    if isinstance(linhas, list):
        for linha in linhas:
            letreiro = linha['lt']
            if letreiro not in letreiros_encontrados:
                letreiros_encontrados.append(letreiro)
    else:
        print(f"Resposta inesperada para o termo de busca {i}: {linhas}")
    
for letreiro in letreiros_encontrados:
    print(letreiro)