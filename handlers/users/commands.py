from data.loader import bot, db
from telebot.types import Message
from keyboards.default import register
from keyboards.inline import translate

@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id

    db.insert_telegram_id(telegram_id=from_user_id)

    check = db.check_user(telegram_id=from_user_id)
    if None in check:
        text = "Translate botga xushkelibsiz.\n"
        "Bottan foydalanish ushun ro'xatdan uting.👇🏻"
        markup = register()


    else:
        text = "Batafsil malumot olish ushun /help komandasini bosing"
        markup = translate()

    bot.send_message(chat_id, text, reply_markup=markup)


