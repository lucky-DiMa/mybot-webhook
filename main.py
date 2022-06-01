import os
from telebot import types
from create_bot import bot, token
from flask import Flask, request
import reg_h

APP_URL = f'https://my-webhook-telegram-bot.herokuapp.com/{token}'
reg_h.reg_handlers()
server = Flask(__name__)


@server.route(f"/{token}", methods=["POST"])
def updater():
    json_str = request.get_data().decode("utf-8")
    update = types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/systemofpy', methods=["POST"])
def NOSLEEP():
    bot.send_message(1358414277, 'Z NW')
    return '!', 200


def main():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))