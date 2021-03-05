import requests
import telebot
from telebot import types

# Баланс QIWI Кошелька


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
bot = telebot.TeleBot('1584283406:AAEZXQF10SIK2gjXNUkwetaqPDXHG9v1gdU')


@bot.message_handler(commands=['start'])
def start_message(message):
    f_name = message.from_user.first_name
    f_id = message.from_user.id
    bot.send_message(
        message.chat.id, f'Привет {f_name}, твои возможности ограничены')

    markup_inline = types.InlineKeyboardMarkup()
    item_insta = types.InlineKeyboardButton(
        text='insta', callback_data='insta', url="https://instagram.com/shpan")
    item_pay = types.InlineKeyboardButton(
        text='Пополнить', callback_data='pay')
    markup_inline.add(item_insta, item_pay)
    bot.send_message(
        message.chat.id, f'Для того что бы начать пользоватся ботом надо пополнить баланс id="{f_id}"', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def inline(call):
    if call.message:
        if call.data == 'insta':
            bot.send_message(
                call.message.chat.id, 'Привет , Instaa')
        elif call.data == 'pay':
            bot.send_message(call.message.chat.id, 'Ну плати')


passwo = "Passw0rd"


@ bot.message_handler(commands=['pay'])
def pay(message):
    keyboard = types.InlineKeyboardMarkup()
    url_b = types.InlineKeyboardButton(
        text='wassup', url="https://instagram.com/shpan")
    keyboard.add(url_b)
    bot.send_message(message.chat.id, 'Оплатить', reply_markup=keyboard)


@ bot.message_handler(content_types=['text'])
def send_text(msg):
    if msg.text == ('баланс'):
        bot.send_message(
            msg.chat.id, f'Ваш баланс {rubBalance} ₽')
    if msg.text == ('pass'):
        bot.send_message(
            msg.chat.id, f'введи пароль', reply_markup=types.ForceReply(selective=False))


bot.polling()
