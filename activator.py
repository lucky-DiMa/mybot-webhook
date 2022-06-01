import time, requests
import main
from create_bot import bot, token
bot.send_message(1358414277, 'Я new')
requests.post(f'https://my-webhook-telegram-bot.herokuapp.com/{token}', 'HELLO')
bot.send_message(1358414277, 'Я new2')
main.main()
while True:
    time.sleep(60)
    requests.post('https://my-webhook-telegram-bot.herokuapp.com/')