import config

import json
import telebot
from telebot.types import Message

lst = []

msg = {
    'start' : 'Вы подписаны на рыссылку, также у Вас есть возможность общаться с администраторами, для этого просто отправьте мне сообщение, оно будет доставлено по адресу',
    'mailing' : 'Следующее Ваше сообщение будет отправлено всем пользователям, использующим бота'
}

print("Бот запущен. Нажмите Ctrl+C для завершения")

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def msg_start(message):
    bot.send_message(message.chat.id, msg['start'])
    lst.append(message.chat.id)

@bot.message_handler(commands=['delete'])
def msg_delete(message):
    for item in lst:
        if (item == message.chat.id):
            lst.remove(item)
            break

@bot.message_handler(commands=['mailing'])
def msg_mailing(message):
    if message.chat.id == config.chat_id:
        bot.send_message(message.chat.id, msg['mailing'])
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
