import time, requests
if __name__ == '__main__':
    while True:
        time.sleep(60)
        requests.get('https://my-webhook-telegram-bot.herokuapp.com/')