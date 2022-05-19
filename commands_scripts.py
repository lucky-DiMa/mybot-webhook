from create_bot import bot
# import mail_sender
import json
from telebot import types
import sys
import os


def start(message):
    new = True
    n = 0
    with open('db.json', "r") as file:
        data = json.load(file)
    for i in range(0, len(data["users"])):
        if data["users"][i]["id"] == message.from_user.id:
            new = False
            n = i
    if new:
        data["users"].append({"id": message.from_user.id,
                              "username": message.from_user.username,
                              "first_name": message.from_user.first_name,
                              "last_name": message.from_user.last_name,
                              "old_email": None,
                              "email": None,
                              "mode": "calm",
                              "proc": {"message_id": 0,
                                       "stage": None}})
        n = len(data["users"]) - 1
    if data["users"][n]["proc"]["stage"] is None:
        bot.delete_message(message.chat.id, message.id)
        bot.send_message(message.chat.id, f'Hello, {data["users"][n]["first_name"]}!')
        bot.send_message(message.chat.id, f"""Меня зовут {data["users"][0]["first_name"]} !
Я интересный бот, умею отвечать на все приветствия,
также у меня есть комманды! Обязательно загляни в их список!""")
    else:
        bot.send_message(message.chat.id, 'Cначала заверши процесс!')
    with open('db.json', "w") as file:
        json.dump(data, file, indent=2)
    #os.execl(sys.executable, sys.executable, *sys.argv)


def changemydata(message, delmes=True):
    n = -1
    new = True
    with open('db.json', "r") as file:
        data = json.load(file)
    for i in range(0, len(data["users"])):
        if data["users"][i]["id"] == message.from_user.id:
            new = False
            n = i
    if not new:
        if data["users"][n]["proc"]["stage"] is None:
            markup = types.InlineKeyboardMarkup(row_width=2)
            change_first_name_button = types.InlineKeyboardButton('Изменить имя', callback_data="changefirstname")
            change_last_name_button = types.InlineKeyboardButton('Изменить фамилию', callback_data="changelastname")
            change_username_button = types.InlineKeyboardButton('Изменить имя пользователя', callback_data="changeusername")
            markup.add(change_first_name_button, change_last_name_button, change_username_button)
            if delmes:
                bot.send_message(message.chat.id, 'Что хотите изменить в моей базе данных?', reply_markup=markup)
                bot.delete_message(message.chat.id, message.id)
            else:
                bot.edit_message_text('Что хотите изменить в моей базе данных?', message.message.chat.id, message.message.id,
                                      reply_markup=markup)
        else:
            if delmes:
                bot.send_message(message.chat.id, 'Cначала заверши процесс!')
            else:
                bot.answer_callback_query(message.id, 'Сначала заверши процесс', show_alert=True)
    else:
        if delmes:
            bot.reply_to(message, 'Ты новичок, чтобы я понял как тебе отвечать напиши /start !')
        else:
            bot.reply_to(message.message, 'Ты новичок, чтобы я понял как тебе отвечать напиши /start !')


def get_user_info(message, delmes=True):
    n = 0
    with open('db.json', "r") as file:
        data = json.load(file)
    for i in range(0, len(data["users"])):
        if data["users"][i]["id"] == message.from_user.id:
            n = i
    if n > 0:
        if data["users"][n]["proc"]["stage"] is None:
            markup = types.InlineKeyboardMarkup(row_width=2)
            idbutton = types.InlineKeyboardButton('id', callback_data='id')
            usernamebutton = types.InlineKeyboardButton('Имя пользователя', callback_data='username')
            firstnamebutton = types.InlineKeyboardButton('Имя', callback_data='firstname')
            lastnamebutton = types.InlineKeyboardButton('Фамилия', callback_data='lastname')
            emailbutton = types.InlineKeyboardButton('Эл. почта', callback_data='email')
            markup.add(idbutton, usernamebutton, firstnamebutton, lastnamebutton, emailbutton)
            if delmes:
                bot.delete_message(message.chat.id, message.id)
                bot.send_message(message.chat.id,
                                 f'Что вы, {data["users"][n]["first_name"]}, хотите узнать о своём профиле в Telegram?',
                                 reply_markup=markup)
            else:
                bot.edit_message_text(
                    f'Что вы, {data["users"][n]["first_name"]}, хотите узнать о своём профиле в Telegram?', message.message.chat.id,
                    message.message.id, reply_markup=markup)
        else:
            if delmes:
                bot.send_message(message.chat.id, 'Cначала заверши процесс!')
            else:
                bot.answer_callback_query(message.id, 'Сначала заверши процесс', show_alert=True)
    else:
        if delmes:
            bot.reply_to(message, 'Ты новичок, чтобы я понял как тебе отвечать напиши /start !')
        else:
            bot.reply_to(message.message, 'Ты новичок, чтобы я понял как тебе отвечать напиши /start !')
    #os.execl(sys.executable, sys.executable, *sys.argv)


def changeanswermood(message):
    n = 0
    global new
    new = True
    with open('db.json', "r") as file:
        data = json.load(file)
    for i in range(0, len(data["users"])):
        if data["users"][i]["id"] == message.chat.id:
            new = False
            n = i
    if new == False:
        if data["users"][n]["proc"]["stage"] is None:
            bot.delete_message(message.chat.id, message.id)
            markup = types.InlineKeyboardMarkup(row_width=2)
            setcalmbutton = types.InlineKeyboardButton('Спокойные', callback_data='setcalm')
            setfunbutton = types.InlineKeyboardButton('Весёлые', callback_data='setfun')
            setagrbutton = types.InlineKeyboardButton('Агрессивныe', callback_data='setagr')
            markup.add(setfunbutton, setagrbutton, setcalmbutton)
            mood: str
            match data["users"][n]["mode"]:
                case "calm":
                    mood = 'спокойно'
                case "agr":
                    mood = 'агрессивно'
                case "fun":
                    mood = 'весело'
            bot.send_message(message.chat.id,
                             f'Сейчас я отвечаю вам {mood}! Какие ответы от меня вы хотите получать на свои сообщения?',
                             reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Cначала заверши процесс!')
    else:
        bot.reply_to(message, 'Ты новичок, чтобы я понял как тебе отвечать напиши /start !')

def test_pay(message):
    bot.send_invoice(message.chat.id, 'TEST', 'TEST', 'TEST', )

def email_func(message, delmes=True):
    n = 0
    with open('db.json', "r") as file:
        data = json.load(file)
    for i in range(0, len(data["users"])):
        if data["users"][i]["id"] == message.from_user.id:
            n = i
    if n > 0:
        if data["users"][n]["proc"]["stage"] is None:
            markup = types.InlineKeyboardMarkup(row_width=1)
            if data["users"][i]["email"] is None:
                addemailbutton = types.InlineKeyboardButton('Добавить почту', callback_data='addemail')
                markup.add(addemailbutton)
            else:
                editemailbutton = types.InlineKeyboardButton('Изменить почту', callback_data='addemail')
                delemailbutton = types.InlineKeyboardButton('Удалить почту', callback_data='delemail')
                markup.add(editemailbutton, delemailbutton)
            if delmes:
                bot.delete_message(message.chat.id, message.id)
                bot.send_message(message.chat.id,
                                 f' Сейчас ваша почта: {data["users"][n]["email"]}\nЧто вы, {data["users"][n]["first_name"]}, хотите сделать?',
                                 reply_markup=markup)
            else:
                bot.edit_message_text(
                    f'Что вы, {data["users"][n]["first_name"]}, хотите сделать?',
                    message.message.chat.id,
                    message.message.id,
                    reply_markup=markup)
        else:
            if delmes:
                bot.send_message(message.chat.id, 'Cначала заверши процесс!')
            else:
                bot.answer_callback_query(message.id, 'Сначала заверши процесс', show_alert=True)
    else:
        if delmes:
            bot.reply_to(message, 'Ты новичок, чтобы я понял как тебе отвечать напиши /start !')
        else:
            bot.reply_to(message.message, 'Ты новичок, чтобы я понял как тебе отвечать напиши /start !')
    #os.execl(sys.executable, sys.executable, *sys.argv)

def reg_handlers():
    bot.register_message_handler(start, commands=['start'])
    bot.register_message_handler(get_user_info, commands=['getmyinfo'])
    bot.register_message_handler(changeanswermood, commands=['changeanswermood'])
    bot.register_message_handler(changemydata, commands=['changemydata'])
    bot.register_message_handler(email_func, commands=['emailfunc'])
