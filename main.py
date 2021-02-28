import telebot

bot = telebot.TeleBot('1584283406:AAHolV6-eANqsIHCx2zYVPGCOYZbWR_8NxM')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


bot.polling()
