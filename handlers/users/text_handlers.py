from data.loader import bot, db
from telebot.types import Message, ReplyKeyboardRemove
from keyboards.default import telefon_button
from keyboards.inline import translate

USER_DATA = {}

@bot.message_handler(func=lambda message: message.text == "Ro'yxatdan o'tish")
def registration(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    USER_DATA[from_user_id] = {}
    msg = bot.send_message(chat_id, "F.I.O ni kriting", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, get_name)

def get_name(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    full_name = message.text
    if full_name.isalpha():
        USER_DATA[from_user_id]["full_name"] = full_name
    else:
        bot.send_message(chat_id, "Ism va familya faqat harflardan iborat bulsin!!!")


    msg = bot.send_message(chat_id, "Telefon raqamni buttonini bosib kritimng.👇🏻", reply_markup=telefon_button())
    bot.register_next_step_handler(msg, get_contackt_and_save)

def get_contackt_and_save(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    full_name = USER_DATA[from_user_id]['full_name']
    if message.contact:
        phone_number = message.contact.phone_number
        if phone_number.startswith("+998"):
            phone_number = message.text
        else:
            bot.send_message(chat_id, "Telefon Raqamda xatolik!!!")

    else:
        phone_number = message.text


    db.update_user(full_name, phone_number, from_user_id)
    bot.send_message(chat_id, "Ro'yhatdan muvafqiyatli uttingiz.👍🏻", reply_markup=ReplyKeyboardRemove())

    bot.send_message(chat_id, "Translate uchun buttonni bosing", reply_markup=translate())









