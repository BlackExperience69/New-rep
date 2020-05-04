from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram import Bot
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
import requests



TG_TOKEN = "1137122161:AAHtp6Zr1FaLQxn9Yh0UcSWMpETF1Li0pck"

reply_keyboard = [['ru_en', '/en_ru', '/ru_tr', '/ru_de']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

TRANS_DIRECTION_KEY = "trans-direction"


def start(bot, update):
    update.message.reply_text("Привет) Я бот-переводчик, Крипто. Ты мне не поверишь, но я перевожу слова"
                              " и предложения.", reply_markup=markup)


def translater(bot, updater, user_data):
    translator_uri = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    response = requests.get(translator_uri, params={
        "key": "trnsl.1.1.20170206T114843Z.150706f980933244.3131bc737246d8afe33e325ad0d875ed2d646f8b",
        "lang": user_data.get(TRANS_DIRECTION_KEY),
        "text": updater.message.text
    })
    updater.message.reply_text("\n\n".join([response.json()["text"][0]]))


def ru_en(bot, updater, user_data):
    user_data[TRANS_DIRECTION_KEY] = "ru-en"
    updater.message.reply_text("Используем направление перевода: Анийский" + user_data[TRANS_DIRECTION_KEY])


def en_ru(bot, updater, user_data):
    user_data[TRANS_DIRECTION_KEY] = "en-ru"
    updater.message.reply_text("Используем направление перевода: " + user_data[TRANS_DIRECTION_KEY])


def ru_tr(bot, updater, user_data):
    user_data[TRANS_DIRECTION_KEY] = "ru-tr"
    updater.message.reply_text("Используем направление перевода: " + user_data[TRANS_DIRECTION_KEY])


def ru_de(bot, updater, user_data):
    user_data[TRANS_DIRECTION_KEY] = "ru-de"
    updater.message.reply_text("Используем направление перевода: " + user_data[TRANS_DIRECTION_KEY])


def main():
    bot = Bot(token=TG_TOKEN, base_url="https://telegg.ru/orig/bot")
    updater = Updater(bot=bot)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ru_en", ru_en, pass_user_data=True))
    dp.add_handler(CommandHandler("en_ru", en_ru, pass_user_data=True))
    dp.add_handler(CommandHandler("ru_tr", ru_tr, pass_user_data=True))
    dp.add_handler(CommandHandler("ru_de", ru_de, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, translater, pass_user_data=True))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()