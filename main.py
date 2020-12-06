import telebot
from pprint import pprint

token = "1302154546:AAFgAU5NdG3Hmb5gRwoAkfa5HsWCwRX3U4g"
bot = telebot.TeleBot(token)


# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"\
Привет, {message.from_user.first_name}! Это торговый бот. Пиши 'help' и он напишет, что он умеет\
")


# Handle '/help'
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, """\
Тут появится инфо\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, "Ну привет, " + message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling()
