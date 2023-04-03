import requests

uf = "SP"
cidade = "Campinas"
endereco = "Nelson Barbosa"

link = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'

requisicao = requests.get(link)
#print(requisicao)

dic_requisicao = requisicao.json()
#print(dic_requisicao)

import pprint
pprint.pprint(dic_requisicao)