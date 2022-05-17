import os
import sys
import json
from not_spec_simb_checker import check
import code_generator
import commands_scripts
import mail_sender
from create_bot import bot
from telebot import types


def somemessage(message):
    n = 0
    global new
    new = True
    with open('db.json', "r") as file:
        data = json.load(file)
    for i in range(0, len(data["users"])):
        if data["users"][i]["id"] == message.from_user.id:
            new = False
            n = i
    if not new:
        if data["users"][n]["proc"]["stage"] is not None:
            if data["users"][n]["proc"]["stage"] == 'changefirst_namefromkeyboard':
                data["users"][n]["proc"]["stage"] = None
                markup = types.InlineKeyboardMarkup(row_width=2)
                if message.text == 'Отмена':
                    changefromaccauntbutton = types.InlineKeyboardButton('Взять имя из аккаунта Telegram',
                                                                         callback_data="getfirstnamefromaccaunt")
                    changefromkeyboardbutton = types.InlineKeyboardButton('Ввести вручную',
                                                                          callback_data="enterfirstnamefromkeyboard")
                    backtochangemydatamenubutton = types.InlineKeyboardButton('<<Назад',
                                                                              callback_data='backtochoosewhattochangemenu')
                    markup.add(changefromaccauntbutton, changefromkeyboardbutton, backtochangemydatamenubutton)
                    bot.delete_message(message.chat.id, data["users"][n]["proc"]["message_id"])
                    bot.send_message(message.chat.id,
                                     f'Сейчас ваше имя в моей базе данных: {data["users"][n]["first_name"]}. Откуда брать новое?',
                                     reply_markup=markup)
                else:
                    backtochangemydatamenubutton = types.InlineKeyboardButton('<<Назад',
                                                                              callback_data='backtochoosewhattochangemenu')
                    markup.add(backtochangemydatamenubutton)
                    bot.delete_message(message.chat.id, data["users"][n]["proc"]["message_id"])
                    data["users"][n]["first_name"] = message.text
                    bot.send_message(message.chat.id, f'Теперь в базе данных ваше имя: {data["users"][n]["first_name"]}',
                                     reply_markup=markup)
                data["users"][n]["proc"]["message_id"] = 0
                bot.delete_message(message.chat.id, message.id)
            elif data["users"][n]["proc"]["stage"] == 'changelast_namefromkeyboard':
                data["users"][n]["proc"]["stage"] = None
                markup = types.InlineKeyboardMarkup(row_width=2)
                if message.text == 'Отмена':
                    changefromaccauntbutton = types.InlineKeyboardButton('Взять фамилию из аккаунта Telegram',
                                                                         callback_data="getlastnamefromaccaunt")
                    changefromkeyboardbutton = types.InlineKeyboardButton('Ввести вручную',
                                                                          callback_data="enterlastnamefromkeyboard")
                    backtochangemydatamenubutton = types.InlineKeyboardButton('<<Назад',
                                                                              callback_data='backtochoosewhattochangemenu')
                    markup.add(changefromaccauntbutton, changefromkeyboardbutton, backtochangemydatamenubutton)
                    bot.delete_message(message.chat.id, data["users"][n]["proc"]["message_id"])
                    bot.send_message(message.chat.id,
                                     f'Сейчас ваша фамилия в моей базе данных: {data["users"][n]["last_name"]}. Откуда брать новую?',
                                     reply_markup=markup)
                else:
                    backtochangemydatamenubutton = types.InlineKeyboardButton('<<Назад',
                                                                              callback_data='backtochoosewhattochangemenu')
                    markup.add(backtochangemydatamenubutton)
                    bot.delete_message(message.chat.id, data["users"][n]["proc"]["message_id"])
                    data["users"][n]["last_name"] = message.text
                    bot.send_message(message.chat.id, f'Теперь в базе данных ваша фамилия: {data["users"][n]["last_name"]}',
                                     reply_markup=markup)
                data["users"][n]["proc"]["message_id"] = 0
                bot.delete_message(message.chat.id, message.id)
            elif data["users"][n]["proc"]["stage"] == 'getemailfromkeyboard':
                if message.text == 'Отмена':
                    bot.delete_message(message.chat.id, message.id)
                    bot.delete_message(message.chat.id, data["users"][n]["proc"]['message_id'])
                    data["users"][n]["proc"]["message_id"] = 0
                    data["users"][n]["proc"]["stage"] = None
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    if data["users"][i]["email"] is None:
                        addemailbutton = types.InlineKeyboardButton('Добавить почту', callback_data='addemail')
                        markup.add(addemailbutton)
                    else:
                        editemailbutton = types.InlineKeyboardButton('Изменить почту', callback_data='addemail')
                        delemailbutton = types.InlineKeyboardButton('Удалить почту', callback_data='delemail')
                        markup.add(editemailbutton, delemailbutton)
                    bot.send_message(message.chat.id,
                                     f' Сейчас ваша почта: {data["users"][n]["email"]}\nЧто вы, {data["users"][n]["first_name"]}, хотите сделать?',
                                     reply_markup=markup)
                else:
                    dog_index = -1
                    dot_after_dog = False
                    dot_index = -1
                    next_must_be_not_spec = True
                    email_is_correct = True
                    for i in range(0, len(message.text)):
                        if email_is_correct:
                            if next_must_be_not_spec:
                                email_is_correct = False
                                eng_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                                for l in range(0, len(eng_letters) - 1):
                                    if message.text[i] == eng_letters[l].lower() or message.text[i] == eng_letters[l] or message.text[i] == '0' or message.text[
                                        i] == '1' or message.text[i] == '2' or message.text[i] == '3' or message.text[
                                        i] == '4' or message.text[i] == '5' or message.text[i] == '6' or message.text[
                                        i] == '7' or message.text[i] == '8' or message.text[i] == '9':
                                        email_is_correct = True
                                        next_must_be_not_spec = False
                                        break
                            else:
                                if check(message.text[i]):
                                    pass
                                elif message.text[i] == '@' and i > 0:
                                    if dog_index > -1:
                                        email_is_correct = False
                                    else:
                                        dog_index = i
                                        next_must_be_not_spec = True
                                elif message.text[i] == '.':
                                    if i - dog_index > 1 and dog_index > -1:
                                        dot_after_dog = True
                                        next_must_be_not_spec = True
                                    else:
                                        next_must_be_not_spec = True
                                else:
                                    email_is_correct = False
                    if not check(message.text[0]) or not check(message.text[len(message.text) - 1]) or len(
                            message.text) < 4 or not dot_after_dog:
                        email_is_correct = False
                    if email_is_correct:
                        bot.delete_message(message.chat.id, message.id)
                        bot.delete_message(message.chat.id, data["users"][n]["proc"]["message_id"])
                        specmarkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                        cancelbutton = types.KeyboardButton('Отмена')
                        specmarkup.add(cancelbutton)
                        data["users"][n]["old_email"] = data["users"][n]["email"]
                        data["users"][n]["email"] = message.text
                        botmes = bot.send_message(message.chat.id,
                                                  f'Теперь отправьте код из сообщения на почте {data["users"][n]["email"]} !',
                                                  reply_markup=specmarkup)
                        data["users"][n]["proc"]["message_id"] = botmes.id
                        code = code_generator.get_code()
                        mail_sender.send_mail(data["users"][0]["email"],
                                              'Superbot',
                                              data["users"][0]["email_password"],
                                              message.text,
                                              'Добавление эл.почты в базу данных бота',
                                              f'Отправьте боту этот код: \n \n {code}')
                        data["users"][n]["proc"]["stage"] = f'entercode-{code}'
                    else:
                        specmarkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                        cancelbutton = types.KeyboardButton('Отмена')
                        specmarkup.add(cancelbutton)
                        botmes = bot.send_message(message.chat.id, 'Вы ввели не почту! Введите ещё раз!',
                                                  reply_markup=specmarkup)
                        bot.delete_message(message.chat.id, message.id)
                        bot.delete_message(data["users"][n]["id"], data["users"][n]["proc"]["message_id"])
                        data["users"][n]["proc"]["message_id"] = botmes.id
            elif 'entercode-' in data["users"][n]["proc"]["stage"]:
                if message.text == 'Отмена':
                    bot.delete_message(message.chat.id, message.id)
                    bot.delete_message(message.chat.id, data["users"][n]["proc"]["message_id"])
                    specmarkup = types.ReplyKeyboardMarkup(True)
                    cancelbutton = types.KeyboardButton('Отмена')
                    specmarkup.add(cancelbutton)
                    botmes = bot.send_message(message.chat.id, 'Введите почту!', reply_markup=specmarkup)
                    data["users"][n]["proc"]["stage"] = 'getemailfromkeyboard'
                    data["users"][n]["proc"]["message_id"] = botmes.id
                    data["users"][n]["email"] = data["users"][n]["old_email"]
                    data["users"][n]["old_email"] = None
                else:
                    code = ''
                    for i in range(len(data["users"][n]["proc"]["stage"]) - 1 - 1 - 10,
                                   len(data["users"][n]["proc"]["stage"])):
                        code += data["users"][n]["proc"]["stage"][i]
                    if message.text == code:
                        data["users"][n]["old_email"] = None
                        bot.delete_message(message.chat.id, data["users"][n]["proc"]["message_id"])
                        data["users"][n]["proc"]["stage"] = None
                        data["users"][n]["proc"]["message_id"] = 0
                        with open('db.json', "w") as file:
                            json.dump(data, file, indent=2)
                        commands_scripts.email_func(message)
                    else:
                        bot.delete_message(message.chat.id, message.id)
                        bot.delete_message(message.chat.id, data["users"][n]["proc"]["message_id"])
                        specmarkup = types.ReplyKeyboardMarkup(True)
                        cancelbutton = types.KeyboardButton('Отмена')
                        specmarkup.add(cancelbutton)
                        botmes = bot.send_message(message.chat.id, f'Вы ввели неверный код из сообщения на почте  {data["users"][n]["email"]} !\nВведите код ещё раз!', reply_markup=specmarkup)
                        data["users"][n]["proc"]["message_id"] = botmes.id
        elif data["users"][n]["mode"] == "calm":
            if 'Привет' in message.text or 'привет' in message.text:
                bot.reply_to(message, 'Привет')
            elif 'Hello' in message.text or 'hello' in message.text or 'Hi' in message.text or 'hi' in message.text:
                bot.reply_to(message, 'Hello')
            else:
                bot.reply_to(message, 'Хммм, что бы это могло значить?')
        elif data["users"][n]["mode"] == "fun":
            if 'Привет' in message.text or 'привет' in message.text:
                bot.reply_to(message, 'Привет друг!')
            elif 'Hello' in message.text or 'hello' in message.text or 'Hi' in message.text or 'hi' in message.text:
                bot.reply_to(message, 'Hi friend!')
            else:
                bot.reply_to(message, 'Эй, друг, извини но я тебя не понял, скажи ещё раз!')
        elif data["users"][n]["mode"] == "agr":
            if 'Привет' in message.text or 'привет' in message.text:
                bot.reply_to(message, 'Привет щ-щенок!')
            elif 'Hello' in message.text or 'hello' in message.text or 'Hi' in message.text or 'hi' in message.text:
                bot.reply_to(message, 'Hi puppy!')
            else:
                bot.reply_to(message, 'Этот лошок забыл как слова выглядят и поэтому я его не понял! хахаххаха!')
    else:
        bot.reply_to(message, 'Ты новичок, чтобы я понял как тебе отвечать напиши /start !')
    with open('db.json', "w") as file:
        json.dump(data, file, indent=2)
    #os.execl(sys.executable, sys.executable, *sys.argv)


def reg_handlers():
    bot.register_message_handler(somemessage, content_types=['text'])
