import telebot
import requests
from bs4 import BeautifulSoup

TOKEN = "2078855013:AAFNlYLFXKIBWftwwn3pn8B4lIOwdlQSGtk"
bot = telebot.TeleBot(token=TOKEN) #токен взят у BotFather

url = "https://ru.investing.com/crypto/currencies"

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Вот что я могу: '/")

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
print(soup.findAll("tb", class_="left noWrap elp symb js-currency-symbol"))

