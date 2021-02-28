import requests
import telebot

bot = telebot.TeleBot('1584283406:AAEZXQF10SIK2gjXNUkwetaqPDXHG9v1gdU')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id, 'Привет, ты написал мне /start')


# Баланс QIWI Кошелька
password = "Passw0rd"


def balance(login, api_access_token):
    s = requests.Session()
    s.headers['Accept'] = 'application/json'
    s.headers['authorization'] = 'Bearer ' + api_access_token
    b = s.get('https://edge.qiwi.com/funding-sources/v2/persons/' +
              login + '/accounts')
    return b.json()


# номер кошелька в формате 79992223344
mylogin = '998946449696'
api_access_token = 'ee125ea7e8fdad4e442e28e09a8661d1'

# все балансы
balances = balance(mylogin, api_access_token)['accounts']

# рублевый баланс
rubAlias = [x for x in balances if x['alias'] == 'qw_wallet_rub']
rubBalance = rubAlias[0]['balance']['amount']


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == ('баланс'):
        bot.send_message(message.chat.id, f'Ваш баланс {rubBalance} ₽')
    if message.text == ('pass'):
        bot.send_message(message.chat.id, f'davay {password}')


bot.polling()
