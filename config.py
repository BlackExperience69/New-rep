import requests
import COVID19Py
import telebot
from telebot import types

covid = COVID19Py.COVID19()

bot = telebot.TeleBot('1137122161:AAHtp6Zr1FaLQxn9Yh0UcSWMpETF1Li0pck')
bot.set_webhook(url="https://telegg.ru/orig/bot")
bot.remove_webhook()


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f'<b>Hello {message.from_user.first_name}!</b>\nEnter the country:'
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ''
    get_message_bot = message.text.strip().lower()

    keyboard = types.InlineKeyboardMarkup()

    key_world = types.InlineKeyboardButton(text='Мир', callback_data='world')
    keyboard.add(key_world)

    key_rus = types.InlineKeyboardButton(text='Россия', callback_data='rus')
    keyboard.add(key_rus)

    key_us = types.InlineKeyboardButton(text='США', callback_data='us')
    keyboard.add(key_us)

    key_it = types.InlineKeyboardButton(text='Италия', callback_data='it')
    keyboard.add(key_it)

    key_es = types.InlineKeyboardButton(text='Испания', callback_data='res')
    keyboard.add(key_es)

    key_ca = types.InlineKeyboardButton(text='Канада', callback_data='ca')
    keyboard.add(key_ca)

    key_ch = types.InlineKeyboardButton(text='Китай', callback_data='ch')
    keyboard.add(key_ch)

    key_de = types.InlineKeyboardButton(text='Германия', callback_data='de')
    keyboard.add(key_de)

    key_fr = types.InlineKeyboardButton(text='Франция', callback_data='fr')
    keyboard.add(key_fr)

    key_se = types.InlineKeyboardButton(text='Швеция', callback_data='se')
    keyboard.add(key_se)

    key_gb = types.InlineKeyboardButton(text='Англия', callback_data='gb')
    keyboard.add(key_gb)

    bot.send_message(message.from_user.id, text='Актуальные новости по странам о Covid19:', reply_markup=keyboard)

    if get_message_bot == 'россия':
        location = covid.getLocationByCountryCode("RU")

    elif get_message_bot == 'сша' or get_message_bot == 'америка':
        location = covid.getLocationByCountryCode("US")

    elif get_message_bot == 'китай':
        location = covid.getLocationByCountryCode("CN")

    elif get_message_bot == 'италия':
        location = covid.getLocationByCountryCode("IT")

    elif get_message_bot == 'испания':
        location = covid.getLocationByCountryCode("ES")

    elif get_message_bot == 'великобритания' or get_message_bot == 'англия':
        location = covid.getLocationByCountryCode("GB")

    elif get_message_bot == 'франция':
        location = covid.getLocationByCountryCode("FR")

    elif get_message_bot == 'германия':
        location = covid.getLocationByCountryCode("DE")

    elif get_message_bot == 'канада':
        location = covid.getLocationByCountryCode("CA")

    elif get_message_bot == 'швеция':
        location = covid.getLocationByCountryCode("SE")

    else:
        location = covid.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n" \
                        f"<b>Заболевшие</b>{location[0]['latest']['confirmed']}\n"

    if final_message == '':
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по стране:</u>\n" \
                        f"Население: {location[0]['country_population']}\n" \
                        f"Последнее обновление: {date[0]}{time[0]}\n" \
                        f"<f1>Последние данные</f1>\n" \
                        f"Заболевших: <b>{location[0]['latest']['confirmed']}</b>\n" \
                        f"Смертей: <b>{location[0]['latest']['deaths']}</b>\n" \
                        f"Выздоровевших: <b>{location[0]['latest']['recovered']}</b>"

    bot.send_message(message.chat.id, final_message, parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    final_message = ''

    if call.data == "rus":
        location = covid.getLocationByCountryCode("RU")

    elif call.data == "us":
        location = covid.getLocationByCountryCode("US")

    elif call.data == "ch":
        location = covid.getLocationByCountryCode("CN")

    elif call.data == "it":
        location = covid.getLocationByCountryCode("IT")

    elif call.data == "es":
        location = covid.getLocationByCountryCode("ES")

    elif call.data == "gb":
        location = covid.getLocationByCountryCode("GB")

    elif call.data == "fr":
        location = covid.getLocationByCountryCode("FR")

    elif call.data == "de":
        location = covid.getLocationByCountryCode("DE")

    elif call.data == "ca":
        location = covid.getLocationByCountryCode("CA")

    elif call.data == "se":
        location = covid.getLocationByCountryCode("SE")

    elif call.data == "world":
        location = covid.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n" \
                        f"<b>Заболевшие</b>{location[0]['latest']['confirmed']}\n"

    if final_message == '':
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по стране:</u>\n" \
                        f"Население: {location[0]['country_population']}\n" \
                        f"Последнее обновление: {date[0]}{time[0]}\n" \
                        f"<f1>Последние данные</f1>\n" \
                        f"Заболевших: <b>{location[0]['latest']['confirmed']}</b>\n" \
                        f"Смертей: <b>{location[0]['latest']['deaths']}</b>\n" \
                        f"Выздоровевших: <b>{location[0]['latest']['recovered']}</b>"

    bot.send_message(call.message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)
