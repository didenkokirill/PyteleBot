import telebot
import requests
import datetime

TOKEN = "2078855013:AAFNlYLFXKIBWftwwn3pn8B4lIOwdlQSGtk"
url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=N55KX025SPV41Z25'
bot = telebot.TeleBot(token=TOKEN) #токен взят у BotFather
dt_now = datetime.date.today()
cg = requests.get(url).json()


def date_high_low(json):
    date = f'{dt_now.year}-{dt_now.month}-{dt_now.day}'
    need = ['2b. high (USD)','3b. low (USD)']
    out_put = []
    for i in range(len(need)):
        out_put.append(json['Time Series (Digital Currency Daily)'][date][need[i]])
    return out_put


@bot.message_handler()
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Вот что я могу: '/")
    bot.register_next_step_handler(message, Coin_name)


def Coin_name(message):
    pass

print(date_high_low(cg))

bot.infinity_polling()