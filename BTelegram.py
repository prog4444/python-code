import telebot
from telebot import types

bot = telebot.TeleBot('5303515767:AAEh__TxII0le0bMa0_IufMAE64R869fJYE')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == "Hello":
#         bot.send_message(message.chat.id, "И тебе привет", parse_mode='html')
#     elif message.text == "photo":
#         photo = open('dop.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo, parse_mode='html')
#     else:
#         bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Ваауу крутое фото", parse_mode='html')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить себ сайт", url="https://prog90003.com"))
    bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website1 = types.InlineKeyboardButton("Веб сайт")
    start1 = types.InlineKeyboardButton("start")
    markup.add(website1, start1)
    bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)


bot.polling(non_stop=True)



