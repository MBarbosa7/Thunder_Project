#Busca de clima com a API da OpenWeather

import requests #importar biblioteca para buscar API's

API_KEY = 'dd770c9d0d8cf26630d523974a121c46' #Chave da API
linguagem = "pt_br" #Linguagem dos Resultados
cep = "13035-500" #CEP Buscado

cep = cep.replace("-", "").replace(".", "").replace(" ", "") #Filtro para sintaxe do "Busca CEP"

#Código Busca CEP
if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)
    dic_requisicao = requisicao.json()

    uf = dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    bairro = dic_requisicao['bairro']
    rua = dic_requisicao['logradouro']
    cep = dic_requisicao['cep']
    print(f"O CEP informado é da {rua}, {bairro}, {cidade} - {uf}. {cep} ")
else:
    print("CEP Inválido")

#CLima com OpenWeather
link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang={linguagem}'

#Filtros para pegar apenas os campos que serão usados
req = requests.get(link)
req.dic = req.json()
descricao = req.dic['weather'][0]['description']
temp_maxima = req.dic['main']['temp_max'] - 273.15
temp_minima = req.dic['main']['temp_min'] - 273.15
temperatura = req.dic['main']['temp'] - 273.15
sensacao = req.dic['main']['feels_like'] - 273.15
humidade = req.dic['main']['humidity']

#Mostragem dos dados na tela
print('')
print(f"CLima = {descricao}")
print(f"Temperatura Atual = {temperatura:,.1f}°C")
print(f"Temperatura Minima = {temp_minima:,.1f}°C")
print(f"Temperatura Maxima = {temp_maxima:,.1f}°C")
print(f"Sensação térmica = {sensacao:,.1f}°C")
print(f"Humidade do ar = {humidade}%")

#Imprimir todos os dados da API em Lista
#import pprint
#pprint.pprint(req.dic)

#Video que foi usado como base para a parte de clima{https://www.youtube.com/watch?v=W_AQ_50Njgo}