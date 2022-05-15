import os
from telebot import types
from create_bot import bot, token
from flask import Flask, request
import reg_h
APP_URL = 'https://my-webhook-telegram-bot.herokuapp.com/'
reg_h.reg_handlers()
server = Flask(__name__)
@server.route(f"/{token}", methods=["POST"])
def route():
    jsonstr = request.get_data().decode("utf-8")
    update = types.Update.de_json(jsonstr)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    server.run(host="0.0.0.0",  port=int(os.environ.get("PORT", 5000)))