import time, requests
import main
from create_bot import bot
bot.send_message(1358414277, 'Я new')
main.main()
while True:
    time.sleep(60)
    requests.post('https://my-webhook-telegram-bot.herokuapp.com/systemofpy')