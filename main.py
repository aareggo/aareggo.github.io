import json
import requests
import telebot

bot = telebot.TeleBot('1584283406:AAHolV6-eANqsIHCx2zYVPGCOYZbWR_8NxM')


QIWI_TOKEN = ''
QIWI_ACCOUNT = ''

s = requests.Session()
s.headers['authorization'] = 'Bearer ' + QIWI_TOKEN
parameters = {'rows': '50'}
h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' +
          QIWI_ACCOUNT + '/payments', params=parameters)
req = json.loads(h.text)
