import os
import telebot

from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['ping'])
def ping(message):
    bot.send_message(
        chat_id=message.chat.id, text="Pong! O bot está funcionando normalmente!"
    )


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    bot.send_message(chat_id=int(os.getenv('CHANNEL_ID')), text=message.text)


if __name__ == '__main__':
    bot.infinity_polling()
