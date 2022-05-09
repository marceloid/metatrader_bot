from email import message_from_string
import os
import telebot

from dotenv import load_dotenv

from messages_re import convert_signal, get_match_dict

load_dotenv()

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))


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


@bot.message_handler(func=lambda message: True)
def broadcast_signal(message):
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


if __name__ == '__main__':
    bot.infinity_polling()
