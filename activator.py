import time, requests
import main
main.main()
while True:
    time.sleep(60)
    requests.post('https://my-webhook-telegram-bot.herokuapp.com/')