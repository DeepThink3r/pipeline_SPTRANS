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
## Função GET

def _get(path):
    response = session.get(url_base+path)
    data = response.json()
    return data

# %%
## PEGAR LINHA

termos_de_busca = [str(i) for i in range(1,100)]
resultados_combinados = []

for termo in termos_de_busca:
    line = _get(f"Linha/Buscar?termosBusca={termo}")
    resultados_combinados.extend(line)

## REMOÇÃO DE DUPLICATAS
resultados_unicos = {linha['cl']: linha for linha in resultados_combinados}.values()

##RESULTADO
j = json.dumps(list(resultados_unicos),ensure_ascii=True)
data = json.loads(j)
print(data)
# %%
