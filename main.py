import requests
import telebot
from telebot import types

<<<<<<< HEAD
bot = telebot.TeleBot('1584283406:AAEZXQF10SIK2gjXNUkwetaqPDXHG9v1gdU')
=======
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
api_access_token = 'a9868427418df870351f1c3832092de3'
>>>>>>> 000344aa687f596a7ac18377e1941711fedb950b


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


@bot.message_handler(commands=["start"])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    markup.row("💼 Инвестиции", "💳 Кошелёк")
    markup.row("👔 Партнерам", "📠 Калькулятор")
    bot.send_message(message.chat.id, "Добрый день", reply_markup=markup)


@bot.message_handler(regexp="Инвестиции")
def invest(message):
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(
        text="NumberOne", callback_data="NumberOne")
    but_2 = types.InlineKeyboardButton(
        text="NumberTwo", callback_data="NumberTwo")
    key.add(but_1, but_2)
    bot.send_message(
        message.chat.id, "⁠▪️ Открывай инвестиции и получай стабильную прибыль в данном разделе, после собирай доход: \n\n💎 Процент прибыли: 3.2 %\n⏱ Время доходности: 24 часа\n📆 Срок вклада: 30 дней\n\n💳 Ваш вклад: 0.0₽\n💵 Накопление: 0.0₽\n\n🧭 Время до сбора: 0: 00: 00", reply_markup=key)


photo = 'https://medialeaks.ru/wp-content/uploads/2017/10/catbread-03-600x400.jpg'


@bot.message_handler(regexp="Кошелёк")
def wallet(message):
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(
        text="Пополнить", callback_data="enter")
    but_2 = types.InlineKeyboardButton(
        text="Вывести", callback_data="exit")
    key.add(but_1, but_2)
    bot.send_message(message.chat.id, "⁠⚙️ Ваш ID: 1455842970\n\n💰 Ваш баланс: 0.0₽\n👥 Партнеров: 0 чел." + '[⠀]' +
                     '(' + photo + ')', parse_mode='markdown', reply_markup=key)


@bot.message_handler(regexp="Калькулятор")
def start_calc(message):
    markup = types.ForceReply(selective=False)
    bot.send_message(message.chat.id, 'Введите сумму', reply_markup=markup)
    print(message.text)
    bot.register_next_step_handler(message, check)


def check(message):
    check = message.text
    print('enter is ' + check)

    if not isint(check):
        print('do a check')
        start_calc(message)
    else:
        print(check)
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row(check)
        bot.send_message(
            message.chat.id, "Подтвердите введенную сумму", reply_markup=markup)
        print('pass')
        bot.register_next_step_handler(message, calc)


def calc(message):
    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    markup.row("💼 Инвестиции", "💳 Кошелёк")
    markup.row("👔 Партнерам", "📠 Калькулятор")
    amount = message.text
    print(amount)
    bot.send_message(message.chat.id, f"⁠В данном разделе вы сумеете рассчитать вашу прибыль, от суммы инвестиции: \n\n💵 Ваша инвестиция: {amount}₽\n\n▪️ Прибыль в сутки: 32.0₽\n▪️ Прибыль в месяц: 973.33₽\n▪️ Прибыль в год: 11679.96₽" + '[⠀]' +
                     '(' + photo + ')', parse_mode='markdown', reply_markup=markup)


bot.polling()
