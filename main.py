import telebot
from telebot import types
import COVID19Py
import os
import random

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1137122161:AAHtp6Zr1FaLQxn9Yh0UcSWMpETF1Li0pck')


@bot.message_handler(commands=['start'])
def start(message):
    stik = open('static/welcome.webp', 'rb')
    send_message = f"<b>Привет, {message.from_user.first_name}!</b>\n Я Серёжа - бот и подопытный кролик своих" \
                   f"создателей.\n Моей главной задачей является делиться основными новостями о Covid19 из разных стран"

    bot.send_message(message.chat.id, send_message, stik, parse_mode='html')


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()

    if get_message_bot == 'россия':
        location = covid19.getLocationByCountryCode("RU")

    elif get_message_bot == 'сша' or get_message_bot == 'америка':
        location = covid19.getLocationByCountryCode("US")

    elif get_message_bot == 'китай':
        location = covid19.getLocationByCountryCode("CN")

    elif get_message_bot == 'италия':
        location = covid19.getLocationByCountryCode("IT")

    elif get_message_bot == 'испания':
        location = covid19.getLocationByCountryCode("ES")

    elif get_message_bot == 'великобритания' or get_message_bot == 'англия':
        location = covid19.getLocationByCountryCode("GB")

    elif get_message_bot == 'франция':
        location = covid19.getLocationByCountryCode("FR")

    elif get_message_bot == 'германия':
        location = covid19.getLocationByCountryCode("DE")

    elif get_message_bot == 'канада':
        location = covid19.getLocationByCountryCode("CA")

    elif get_message_bot == 'швеция':
        location = covid19.getLocationByCountryCode("SE")

    elif 'задача' in get_message_bot or 'ты' in get_message_bot:
        send_message = f"Я Серёжа - бот и подопытный кролик " \
                       f"своих создателей.\n" \
                       f"Моей главной задачей является сообщить тебе всё связанное с Covid19 происходящем в этом мире."

        bot.send_message(message.chat.id, send_message, parse_mode='html')
        final_message = "Повтори запрос правильно)"

    else:
        location = covid19.getLatest()
        final_message = f"<u>По всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n" \
                        f"<b>Смертей: </b>{location['deaths']:,}\n" \
                        f"<b>ыздоровевших: </b>{location['recovered']:,}"

    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Country Data:</u>\nPopulation: {location[0]['country_population']:,}\n" \
                        f"Last updated: {date[0]} {time[0]}\nLatest data:\n<b>" \
                        f"Sick: </b>{location[0]['latest']['confirmed']:,}\n<b>Died: </b>" \
                        f"{location[0]['latest']['deaths']:,}"

    bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)
