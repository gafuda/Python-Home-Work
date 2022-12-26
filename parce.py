from bs4 import BeautifulSoup # библиотеки
import requests

url = "https://scrapingclub.com/exercise/list_basic/?page=1" # пеерменная с ссылкой 


response = requests.get(url) # запрос
# print(response.status_code) - статус запроса
# print(response.text) - проеврить получаемую инфу с запроса 

soup = BeautifulSoup(response.text, "lxml") #передаем bs4 обработанный через lxml текст, получаемый запросом из ссылки
# вместо lxml можно юзать html.parser

data = soup.find("div", class_="col-lg-4 col-md-6 mb-4") # конкретный поиск по тегу и классу (ищем карточку)


name = data.find("h4", class_="card-title").text.replace('\n', '') #(ищем название карточки)
# .text - вырезает текст из всего контейнера
# .replace('\n', '') - замена (заменяет перенос строки пробелом)

price = data.find('h5').text.replace('\n', '') #(ищем стоимость айтема)

