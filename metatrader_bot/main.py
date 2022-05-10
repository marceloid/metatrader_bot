import os
import telebot
from telebot import apihelper

from dotenv import load_dotenv

from messages_re import convert_signal, get_match_dict

load_dotenv()

apihelper.ENABLE_MIDDLEWARE = True
bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))


@bot.middleware_handler(update_types=['channel_post'])
def print_channel_post_text(bot_instance, channel_post):
    message = channel_post.text
    bot.delete_message(channel_post.chat.id, channel_post.message_id)
    try:
        in_message = get_match_dict(message)
        if in_message:
            out_message = convert_signal(in_message)
        else:
            return message

        bot.send_message(chat_id=int(os.getenv('CHANNEL_ID')), text=out_message)

        return out_message
    except:
        pass


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Olá! Este Bot recebe mensagens de ordem de compra ou de venda do MetaTrader, formata a mensagem e encaminha para o canal MetaTrader Test Channel t.me/metatrader_test_channel",
    )


@bot.message_handler(commands=['ping'])
def ping(message):
    bot.send_message(
        chat_id=message.chat.id, text="Pong! O bot está funcionando normalmente!"
    )


@bot.message_handler()
def broadcast_signal(message):
    try:
        in_message = get_match_dict(message.text)
        if in_message:
            out_message = convert_signal(in_message)
        else:
            bot.reply_to(
                message,
                'A mensagem recebida não está no padrão definido para ser encaminhada ao canal!',
            )
            return message.text

        bot.send_message(chat_id=int(os.getenv('CHANNEL_ID')), text=out_message)
        bot.reply_to(
            message,
            'Sinal enviado com sucesso!',
        )
        return out_message
    except:
        bot.reply_to(
            message,
            'Ocorreu algum erro desconhecido e não foi possível enviar o sinal para o canal!',
        )


if __name__ == '__main__':
    bot.infinity_polling()
