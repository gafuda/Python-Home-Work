# Урок https://www.youtube.com/watch?v=lOfm04oLD1U


from bs4 import BeautifulSoup # библиотеки
import requests
from time import sleep

list_card_url = []
headers = {'User Agent': # создается для того, чтобы "не выглядеть ботом" и не грузить сайт 
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36"}

for count in range(1, 8): #переход по страницам
    sleep (1)
    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}" # пеерменная с ссылкой 


    response = requests.get(url, headers = headers) # запрос
    # print(response.status_code) - статус запроса
    # print(response.text) - проеврить получаемую инфу с запроса 

    soup = BeautifulSoup(response.text, "lxml") #передаем bs4 обработанный через lxml текст, получаемый запросом из ссылки
    # вместо lxml можно юзать html.parser

    data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4") # конкретный поиск по тегу и классу (ищем карточку)
    # for i in data: # перебирает весь код страницы по параметрам, указанным выше
    #     name = i.find("h4", class_="card-title").text.replace('\n', '') #(ищем название карточки)
    #     # .text - вырезает текст из всего контейнера
    #     # .replace('\n', '') - замена (заменяет перенос строки пробелом)

    #     price = i.find('h5').text.replace('\n', '') #(ищем стоимость айтема)
    #     url_img = 'https://scrapingclub.com' + i.find("img", class_="card-img-top img-fluid").get("src")

    #     print(name + "\n" + price + "\n" + url_img + "\n\n")

    # блок кода выше - поиск по общему списку карточкек, не заходя внутрь карточки

    for i in data:
        card_url = 'https://scrapingclub.com' + i.find('a').get('href')
        list_card_url.append(card_url)
        # print(card_url)

for card_url in list_card_url:
    response = requests.get(card_url, headers = headers)

    soup = BeautifulSoup(response.text, "lxml") 

    data = soup.find("div", class_="card mt-4 my-4")
    name = data.find('h3', class_='card-title').text
    price = data.find('h4').text
    txt = data.find('p', class_='card-text').text
    print (name + "\n" + price + "\n" + txt + "\n\n")