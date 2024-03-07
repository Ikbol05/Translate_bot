from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def translate():
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("Translate", callback_data="translate")
    markup.add(btn1)
    return markup