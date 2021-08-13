import config

import telebot

print("Бот запущен. Нажмите Ctrl+C для завершения")

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def msg_start(message):
    pass

@bot.message_hanler(content_types=['text'])
def msg_text(message):
    pass
    
bot.polling()
#if __name__ == '__main__':
#	bot.infinity_polling()
