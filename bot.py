import config

import json
import telebot
from telebot.types import Message

print("Бот запущен. Нажмите Ctrl+C для завершения")

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def msg_start(message):
    bot.send_message(message.chat.id, 'Начало')

@bot.message_handler(content_types=['text'])
def msg_text(message):
    if message.chat.id != config.chat_id:
        bot.forward_message(config.chat_id, message.chat.id, message.message_id)
    else:
        try:
            bot.send_message(message.reply_to_message.forward_from.id, message.text)
        except:
            pass

bot.polling()
#if __name__ == '__main__':
#	bot.infinity_polling()
