from create_bot import bot
from telebot import types
import commands_scripts
import random
import json
import os
import sys


def click(call):
    bot.send_message(call.message.chat.id, call)
    n = 0
    global new
    with open('db.json', "r") as file:
        data = json.load(file)
    for i in range(0, len(data["users"])):
        if data["users"][i]["id"] == call.message.chat.id:
            n = i
    if n > 0:
        if data["users"][n]["proc"]["stage"] is None:
            markup = types.InlineKeyboardMarkup(row_width=2)
            backtogetmyinfomenubutton = types.InlineKeyboardButton('<<Назад', callback_data='backtogetmyinfomenu')
            backtochangeanswermoodmenubutton = types.InlineKeyboardButton('<<Назад',
                                                                          callback_data='backtochangeanswermoodmenu')
            backtochoosewhattochangemenubutton = types.InlineKeyboardButton('<<Назад',
                                                                            callback_data='backtochoosewhattochangemenu')
            if call.data == "id":
                markup.add(backtogetmyinfomenubutton)
                bot.edit_message_text(f'Ваш id: {data["users"][n]["id"]}',
                                      data["users"][n]["id"],
                                      call.message.id,
                                      reply_markup=markup)
            if call.data == "lastname":
                markup.add(backtogetmyinfomenubutton)
                bot.edit_message_text(f'Ваша фамилия: {data["users"][n]["last_name"]}',
                                      data["users"][n]["id"],
                                      call.message.id,
                                      reply_markup=markup)
            if call.data == "firstname":
                markup.add(backtogetmyinfomenubutton)
                bot.edit_message_text(f'Ваше имя: {data["users"][n]["first_name"]}',
                                      data["users"][n]["id"],
                                      call.message.id,
                                      reply_markup=markup)
            if call.data == "username":
                markup.add(backtogetmyinfomenubutton)
                if data["users"][n]["username"] != None:
                    bot.edit_message_text(f'Ваше имя пользователя: @{data["users"][n]["username"]}',
                                          data["users"][n]["id"],
                                          call.message.id,
                                          reply_markup=markup)
                else:
                    bot.edit_message_text(f'Имя пользователя не задано',
                                          data["users"][n]["id"],
                                          call.message.id,
                                          reply_markup=markup)
            if call.data == 'email':
                markup.add(backtogetmyinfomenubutton)
                if data["users"][n]["email"] is not None:
                    bot.edit_message_text(f'В моей базе данных ваша почта: {data["users"][n]["email"]}',
                                          data["users"][n]["id"],
                                          call.message.id,
                                          reply_markup=markup)
                else:
                    bot.edit_message_text('В моей базе данных нет вашей почты чтобы её добавить напиши /emailfunc',
                                          data["users"][n]["id"],
                                          call.message.id,
                                          reply_markup=markup)
            if call.data == "backtogetmyinfomenu":
                commands_scripts.get_user_info(call.message, False)
            if call.data == "backtochangeanswermoodmenu":
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
                bot.edit_message_text(
                    f'Сейчас я отвечаю вам {mood}! Какие ответы от меня вы хотите получать на свои сообщения?',
                    data["users"][n]["id"],
                    call.message.id,
                    reply_markup=markup)
            if call.data == 'setagr':
                markup.add(backtochangeanswermoodmenubutton)
                bot.edit_message_text(
                    f'Сейчас я отвечаю вам агрессивно!',
                    data["users"][n]["id"],
                    call.message.id,
                    reply_markup=markup)
                data["users"][n]["mode"] = "agr"
            if call.data == 'setcalm':
                markup.add(backtochangeanswermoodmenubutton)
                bot.edit_message_text(
                    f'Сейчас я отвечаю вам спокойно!',
                    data["users"][n]["id"],
                    call.message.id,
                    reply_markup=markup)
                data["users"][n]["mode"] = "calm"
            if call.data == 'setfun':
                markup.add(backtochangeanswermoodmenubutton)
                bot.edit_message_text(
                    f'Сейчас я отвечаю вам весело!',
                    data["users"][n]["id"],
                    call.message.id,
                    reply_markup=markup)
                data["users"][n]["mode"] = "fun"
            if call.data == 'backtochoosewhattochangemenu':
                commands_scripts.changemydata(call.message, False)
            if call.data == "changefirstname" or call.data == "backtohowtogetfirstname":
                enterfirstnamefromkeyboardbutton = types.InlineKeyboardButton('Ввести вручную',
                                                                              callback_data="enterfirstnamefromkeyboard")
                getfirstnamefromaccauntbutton = types.InlineKeyboardButton('Взять из аккаунта Telegram',
                                                                           callback_data="getfirstnamefromaccaunt")
                markup.add(getfirstnamefromaccauntbutton, enterfirstnamefromkeyboardbutton,
                           backtochoosewhattochangemenubutton)
                bot.edit_message_text(
                    f'Сейчас ваше имя в моей базе данных: {data["users"][n]["first_name"]}. Откуда брать новое?',
                    data["users"][n]["id"],
                    call.message.id,
                    reply_markup=markup)
            if call.data == "getfirstnamefromaccaunt":
                backtohowtogetfirstnamebutton = types.InlineKeyboardButton('<<Назад',
                                                                           callback_data="backtohowtogetfirstname")
                markup.add(backtohowtogetfirstnamebutton)
                data["users"][n]["first_name"] = call.message.chat.first_name
                bot.edit_message_text(
                    f'Сейчас ваше имя в моей базе данных: {data["users"][n]["first_name"]}',
                    data["users"][n]["id"],
                    call.message.id,
                    reply_markup=markup)
            if call.data == "enterfirstnamefromkeyboard":
                bot.delete_message(call.message.chat.id, call.message.id)
                specmarkup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                specmarkup.add(types.KeyboardButton('Отмена'))
                bm = bot.send_message(call.message.chat.id, 'Ведите имя!', reply_markup=specmarkup)
                data["users"][n]["proc"]["message_id"] = bm.id
                data["users"][n]["proc"]["stage"] = 'changefirst_namefromkeyboard'
            if call.data == "changelastname" or call.data == "backtohowtogetlastname":
                enterlastnamefromkeyboardbutton = types.InlineKeyboardButton('Ввести вручную',
                                                                             callback_data="enterlastnamefromkeyboard")
                getlastnamefromaccauntbutton = types.InlineKeyboardButton('Взять из аккаунта Telegram',
                                                                          callback_data="getlastnamefromaccaunt")
                markup.add(getlastnamefromaccauntbutton, enterlastnamefromkeyboardbutton,
                           backtochoosewhattochangemenubutton)
                bot.edit_message_text(
                    f'Сейчас ваша фамилия в моей базе данных: {data["users"][n]["last_name"]}. Откуда брать новую?',
                    data["users"][n]["id"],
                    call.message.id,
                    reply_markup=markup)
            if call.data == "getlastnamefromaccaunt":
                backtohowtogetlastnamebutton = types.InlineKeyboardButton('<<Назад', callback_data="backtohowtogetlastname")
                markup.add(backtohowtogetlastnamebutton)
                data["users"][n]["first_name"] = call.message.chat.first_name
                bot.edit_message_text(
                    f'Сейчас ваша фамилия в моей базе данных: {data["users"][n]["last_name"]}',
                    data["users"][n]["id"],
                    call.message.id,
                    reply_markup=markup)
            if call.data == "enterlastnamefromkeyboard":
                bot.delete_message(call.message.chat.id, call.message.id)
                specmarkup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                specmarkup.add(types.KeyboardButton('Отмена'))
                bm = bot.send_message(call.message.chat.id, 'Ведите фамилию!', reply_markup=specmarkup)
                data["users"][n]["proc"]["message_id"] = bm.id
                data["users"][n]["proc"]["stage"] = 'changelast_namefromkeyboard'
            if call.data == "changeusername":
                data["users"][n]["username"] = call.message.chat.username
                markup.add(backtochoosewhattochangemenubutton)
                if call.message.chat.username is not None:
                    bot.edit_message_text(
                        f'Теперь в моей базе данных ваше имя пользователя @{data["users"][n]["username"]}',
                        data["users"][n]["id"],
                        call.message.id,
                        reply_markup=markup)
                else:
                    bot.edit_message_text(
                        'Имя пользователя не задано!',
                        data["users"][n]["id"],
                        call.message.id,
                        reply_markup=markup)
            if call.data == 'delemail':
                data["users"][n]["email"] = None
                backtoemailfuncbutton = types.InlineKeyboardButton('<<Назад', callback_data='backtoemailfunc')
                markup.add(backtoemailfuncbutton)
                bot.edit_message_text('Почта удалена из базы данных',
                                      data["users"][n]["id"],
                                      call.message.id,
                                      reply_markup=markup)
            if call.data == 'addemail':
                bot.delete_message(call.message.chat.id,call.message.id)
                specmarkup = types.ReplyKeyboardMarkup(True)
                cancelbutton = types.KeyboardButton('Отмена')
                specmarkup.add(cancelbutton)
                botmes = bot.send_message(call.message.chat.id, 'Введите почту!', reply_markup=specmarkup)
                data["users"][n]["proc"]["stage"] = 'getemailfromkeyboard'
                data["users"][n]["proc"]["message_id"] = botmes.id
            if call.data  == 'backtoemailfunc':
                commands_scripts.email_func(call.message, False)
        else:
            bot.send_message(call.message.chat.id, 'Cначала заверши процесс!')
    else:
        bot.reply_to(call.message, 'Ты новичок, чтобы я понял как тебе отвечать напиши /start !')
    with open('db.json', "w") as file:
        json.dump(data, file, indent=2)
    os.execl(sys.executable, sys.executable, *sys.argv)


def reg_handlers():
    bot.register_callback_query_handler(click, func=lambda call: True)
