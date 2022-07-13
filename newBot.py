import telebot

bot = telebot.TeleBot('5303515767:AAEh__TxII0le0bMa0_IufMAE64R869fJYE')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Салом, <b>{message.from_user.first_name}' \
           f' <u>{message.from_user.last_name}</u> хуш омадед, боти мо кинохои дилхохатонро ' \
           f'ёфта медихад, барои ин факат номи киноро нависед шуд</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


bot.polling(non_stop=True)