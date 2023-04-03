#Busca de clima com a API da OpenWeather
import requests

API_KEY = 'dd770c9d0d8cf26630d523974a121c46'
city = 'campinas'

link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br'

req = requests.get(link)
req.dic = req.json()
descricao = req.dic['weather'][0]['description']
temperatura = req.dic['main']['temp'] - 273.15
city_name = req.dic['name']
print(f"Informações em {city_name}")
print(f"CLima = {descricao}")
print(f"Temperatura = {temperatura}°C")

#print(req.json())
#Video que foi usado como base {https://www.youtube.com/watch?v=W_AQ_50Njgo}