import telebot

bot = telebot.TeleBot('1584283406:AAEZXQF10SIK2gjXNUkwetaqPDXHG9v1gdU')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(

        message.chat.id, 'Привет, ты написал мне /start )))')


bot.polling()
