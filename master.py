import telebot
import requests
from bs4 import BeautifulSoup


def outInfo(data):
    for j in data:      #корочь тебе ндо чтоб эта хрень была в формате str чтоб
        print(data)     #её можно было find и надо както ввытащить из мультисписка

TOKEN = "2078855013:AAFNlYLFXKIBWftwwn3pn8B4lIOwdlQSGtk"
bot = telebot.TeleBot(token=TOKEN)
#токен взят у BotFather

url = "https://bitinfocharts.com/ru/crypto-kurs/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")


print(page.status_code)
data_bank = []
with open("currency") as file:
    lines = file.readline()
    for i in range(int(lines)):
        a = file.readline()
        data_bank.append(soup.findAll("tr", id=f"tr_{int(a)}"))

print(data_bank)