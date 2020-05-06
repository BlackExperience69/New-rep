import telebot
from telebot import types
import COVID19Py
import os
import random

AUTORS = ['Николай Д.', 'Максиков М.']
SOVIET = ['мойте попу пацаны, лишь бы целы бы штаны', 'корень смотри внутрь', 'писко-витса']

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1137122161:AAHtp6Zr1FaLQxn9Yh0UcSWMpETF1Li0pck')

DIR = 'мемы'
STICK = 'стикеры'


@bot.message_handler(commands=['start'])
def start(message):
    stik = open((os.path.join(STICK, random.choice(os.listdir(STICK)))), 'rb')
    bot.send_sticker(message.chat.id, stik)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Поднять настроение :)")
    item2 = types.KeyboardButton("Дельный совет")

    markup.add(item1, item2)

    send_message = f"<b>Привет, {message.from_user.first_name}!</b>\n Я <b>Серёжа</b> - бот и подопытный кролик своих" \
                   f"создателей.\n Моей главной задачей является делиться основными новостями о Covid19 из разных стран"

    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

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



@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    country = ""
    flag = True
    get_message_bot = message.text.strip().lower()


    if message.chat.type == 'private':
        if message.text == 'Поднять настроение :)':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Like))", callback_data='good')
            item2 = types.InlineKeyboardButton("Dislike((", callback_data='bad')

            markup.add(item1, item2)

            photo = open((os.path.join(DIR, random.choice(os.listdir(DIR)))), 'rb')
            bot.send_photo(message.chat.id, photo)

            send_message = f"Как тебе?"
            bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

            flag = False

        elif message.text == 'Дельный совет':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            send_message = F"{random.choice(SOVIET)}\n<b>{random.choice(AUTORS)}</b>"
            bot.send_message(message.chat.id, send_message, parse_mode='html')

            send_message = f"Как тебе?"
            bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

            flag = False

    if get_message_bot == 'россия':
        location = covid19.getLocationByCountryCode("RU")
        country = 'Россия'

    elif get_message_bot == 'сша' or get_message_bot == 'америка':
        location = covid19.getLocationByCountryCode("US")
        country = 'США'

    elif get_message_bot == 'китай':
        location = covid19.getLocationByCountryCode("CN")
        country = 'Китай'

    elif get_message_bot == 'италия':
        location = covid19.getLocationByCountryCode("IT")
        country = 'Италия'

    elif get_message_bot == 'испания':
        location = covid19.getLocationByCountryCode("ES")
        country = 'Испания'

    elif get_message_bot == 'великобритания' or get_message_bot == 'англия':
        location = covid19.getLocationByCountryCode("GB")
        country = 'Великобритания'

    elif get_message_bot == 'франция':
        location = covid19.getLocationByCountryCode("FR")
        country = 'Франция'

    elif get_message_bot == 'германия':
        location = covid19.getLocationByCountryCode("DE")
        country = 'Гемания'

    elif get_message_bot == 'канада':
        location = covid19.getLocationByCountryCode("CA")
        country = 'Канада'

    elif get_message_bot == 'швеция':
        location = covid19.getLocationByCountryCode("SE")
        country = 'Швеция'

    elif 'задача' in get_message_bot or 'ты' in get_message_bot:
        send_message = f"Я Серёжа - бот и подопытный кролик " \
                       f"своих создателей.\n" \
                       f"Моей главной задачей является сообщить тебе всё связанное с Covid19 происходящем в этом мире."

        bot.send_message(message.chat.id, send_message, parse_mode='html')
        final_message = "Повтори запрос правильно)"

    elif 'прив' in get_message_bot or 'здравст' in get_message_bot:
        stik = open((os.path.join(STICK, random.choice(os.listdir(STICK)))), 'rb')
        bot.send_sticker(message.chat.id, stik)
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

    elif 'спасибо' in get_message_bot:
        final_message = f"Пожалуйста))\nЯ для этого и создан ;)"


    else:
        location = covid19.getLatest()
        final_message = f"<u>По всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n" \
                        f"<b>Смертей: </b>{location['deaths']:,}"

    if flag:
        if final_message == "":
            date = location[0]['last_updated'].split("T")
            time = date[1].split(".")
            final_message = f"<u>По стране: <b>{country}</b></u>\nНаселение: {location[0]['country_population']:,}\n" \
                            f"Последнее обновление: {date[0]} {time[0]}\n<u>Последние данные:</u>\n<b>" \
                            f"Больных: </b>{location[0]['latest']['confirmed']:,}\n<b>Смертей: </b>" \
                            f"{location[0]['latest']['deaths']:,}"

        bot.send_message(message.chat.id, final_message, parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:

        if call.data == 'good' or call.data == 'bad':
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')

            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Как так то? 😢')

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Как тебе?",
                                    reply_markup=None)

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="СПАСИБО ЗА КОММЕНТАРИЙ")

        else:
            print(1)
            final_message = ''
            country = ''

            if call.data == "rus":
                location = covid19.getLocationByCountryCode("RU")
                country = 'Россия'

            elif call.data == "us":
                location = covid19.getLocationByCountryCode("US")
                country = 'США'

            elif call.data == "ch":
                location = covid19.getLocationByCountryCode("CN")
                country = 'Китай'

            elif call.data == "it":
                location = covid19.getLocationByCountryCode("IT")
                country = 'Италия'

            elif call.data == "es":
                location = covid19.getLocationByCountryCode("ES")
                country = 'Испания'

            elif call.data == "gb":
                location = covid19.getLocationByCountryCode("GB")
                country = 'Великобритания'

            elif call.data == "fr":
                location = covid19.getLocationByCountryCode("FR")
                country = 'Франция'

            elif call.data == "de":
                location = covid19.getLocationByCountryCode("DE")
                country = 'Германия'

            elif call.data == "ca":
                location = covid19.getLocationByCountryCode("CA")
                country = 'Канада'

            elif call.data == "se":
                location = covid19.getLocationByCountryCode("SE")
                country = 'Швеция'

            elif call.data == "world":
                location = covid19.getLatest()
                final_message = f"<u>По всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n" \
                                f"<b>Смертей: </b>{location['deaths']:,}"

            if final_message == "":
                date = location[0]['last_updated'].split("T")
                time = date[1].split(".")
                final_message = f"<u>По стране: <b>{country}</b></u>\nНаселение: {location[0]['country_population']:,}\n" \
                            f"Последнее обновление: {date[0]} {time[0]}\n<u>Последние данные:</u>\n<b>" \
                            f"Больных: </b>{location[0]['latest']['confirmed']:,}\n<b>Смертей: </b>" \
                            f"{location[0]['latest']['deaths']:,}"

            bot.send_message(call.message.chat.id, final_message, parse_mode='html')


    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
