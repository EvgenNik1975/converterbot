
import telebot
import traceback
from Extensions import *


bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands = ['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Привет!\n Для конвертации введите запрос в формате:\n <исходная валюта> <требуемая валюта> <количество>\n Cписок доступных валют - /values '

    bot.send_message(message.chat.id, text)


@bot.message_handler(commands = ['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in dict.keys():
        text = "\n".join((text, i))

    bot.reply_to(message, text)


@bot.message_handler(content_types = ['text'])
def converter(message: telebot.types.Message):
    
    value = message.text.split(' ')
    try:
        if len(value) != 3:
            raise APIException(f'Неверное число параметров!')
            
        answer = Convertor.get_price(*value)
    except APIException as e:
        bot.reply_to(message, f'Ошибка в команде:\n{e}')
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f'Неизвестная ошибка:\n{e}')
    else:
        bot.reply_to(message, answer)


bot.polling()
