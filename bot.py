import config

import json
import telebot
from telebot.types import Message

lst = []

print("Бот запущен. Нажмите Ctrl+C для завершения")

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def msg_start(message):
    bot.send_message(message.chat.id, 'Напиши мне')
    lst.append(message.chat.id)

@bot.message_handler(commands=['delete'])
def msg_delete(message):
    for index, item in enumerate(lst):
        if (item == message.chat.id):
            lst.remove(index)
            break

@bot.message_handler(commands=['mailing'])
def msg_mailing(message):
    if message.chat.id == config.chat_id:
        bot.register_next_step_handler(message, mailing)
    
def mailing(message):
    for item in lst:
        bot.send_message(item, message.text)

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
