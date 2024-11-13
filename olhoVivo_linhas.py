#%%
##Importando bibliotecas
import requests
import os
import json
from dotenv import load_dotenv

# Carregar as variáveis de ambiente
load_dotenv()

token = os.getenv('MEU_TOKEN')
session = requests.Session()
url_base = "https://api.olhovivo.sptrans.com.br/v2.1/"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
endpoint_token = "Login/Autenticar?"
params = {
    'token': token
}

# Autenticação
r = session.post(f'{url_base}{endpoint_token}', params=params, headers=headers)

if r.json() == True:
    # Puxar os dados
    endpoint_linha = 'Linha/Buscar?'
    resultados_combinados = []

    for i in range(1, 100):
        params = {'termosBusca': str(i)}
        response = session.get(url_base + endpoint_linha, params=params, headers=headers)
        if response.status_code == 200:
            resultados_combinados.extend(response.json())
        else:
            print(f'Erro na requisição para termosBusca={i}: {response.status_code}')

    # Remoção de duplicatas
    resultados_unicos = {linha['cl']: linha for linha in resultados_combinados}.values()

    # Resultado
    j = json.dumps(list(resultados_unicos), ensure_ascii=True)
    data = json.loads(j)
    print(data)
else:
    print('Falha na autenticação')
