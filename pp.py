from translated import to_cyrillic, to_latin
import telebot
from telebot import types

TOKEN = "1842495387:AAE76kSagYHUAtS4jAU6qhDAVUXYKJ9xxUU"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    first_name = message.chat.first_name
    response = f"Assalamu alaykum {first_name}, \nPlease enter text only..."

    bot.reply_to(message, response)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text

    if msg.isdigit() or msg[0].isspace():
        response = "Numbers are not allowed!\nPlease enter alphabetical value."
    elif msg.isascii():
        response = to_cyrillic(msg)
    else:
        response = to_latin(msg)
    bot.reply_to(message, response)


bot.polling()

