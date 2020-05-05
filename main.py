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
MEM = False


@bot.message_handler(commands=['start'])
def start(message):
    stik = open('стикеры/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, stik)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Поднять настроение :)")
    item2 = types.KeyboardButton("Дельный совет")

    markup.add(item1, item2)

    send_message = f"<b>Привет, {message.from_user.first_name}!</b>\n Я <b>Серёжа</b> - бот и подопытный кролик своих" \
                   f"создателей.\n Моей главной задачей является делиться основными новостями о Covid19 из разных стран"

    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def mess(message):
    global mem
    mem = False
    final_message = ""
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
            mem = True

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

    if flag:
        if final_message == "":
            date = location[0]['last_updated'].split("T")
            time = date[1].split(".")
            final_message = f"<u>Country Data:</u>\nPopulation: {location[0]['country_population']:,}\n" \
                            f"Last updated: {date[0]} {time[0]}\nLatest data:\n<b>" \
                            f"Sick: </b>{location[0]['latest']['confirmed']:,}\n<b>Died: </b>" \
                            f"{location[0]['latest']['deaths']:,}"

        bot.send_message(message.chat.id, final_message, parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global mem
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')

            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Как так то? 😢')

            if mem:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Как тебе?",
                    reply_markup=None)
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Как тебе?",
                    reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="СПАСИБО ЗА КОММЕНТАРИЙ")

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
