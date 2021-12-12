import telebot
import requests
import datetime

TOKEN = "2078855013:AAFNlYLFXKIBWftwwn3pn8B4lIOwdlQSGtk"
url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=N55KX025SPV41Z25'
bot = telebot.TeleBot(token=TOKEN) #токен взят у BotFather
dt_now = datetime.date.today()
cg = requests.get(url).json()

coins = ['BTC', 'LTC', 'ETH', 'XRP', 'BCH', 'ETC']

def date_high_low(json, symbol):
    date = f'{dt_now.year}-{dt_now.month}-{dt_now.day}'
    need = ['2b. high (USD)', '3b. low (USD)']
    if url[url.find('market=')+7:url.find('&apikey')] != 'USD':
        need.append(f'2a. high ({symbol})', f'3a. low ({symbol}')
    out_put = []
    for i in range(len(need)):
        a = json['Time Series (Digital Currency Daily)'][date][need[i]]
        out_put.append(int(a[:a.find('.')]))
    return out_put


@bot.message_handler()
def get_text_messages(message):
    if message.text == '/help':
        bot.send_message(message.from_user.id, "Вот что я могу:"
                                               "/high_low Показывает максимльную и минимальную цену на сегодня\n"
                                               "Функционал ещё будет обещаю")
    if message.text == '/high_low':
        bot.send_message(message.from_user.id, "Выберете криптовалюту /BTC , /LTC , /ETH , /XRP , /BCH , /ETC")
        bot.register_next_step_handler(message, Coin_name)


def Coin_name(message):
    for i in range(len(coins)):
        if message.text[1:] == coins[i]:
            data = date_high_low(cg,  message.text[-1:])
            bot.send_message(message.from_user.id, f'Пики цен {message.text[1:]} на сегодня: \n'
                                                   f'Наивысшая {data[0]} USD\nМинимальная {data[1]} USD')
            return
        else:
            print('Повторите пожалуйста')
            bot.send_message(message.from_user.id, 'Error')
            return

bot.infinity_polling()