import time, requests
import main
if __name__ == '__main__':
    main.main()
    while True:
        time.sleep(60)
        requests.get('https://my-webhook-telegram-bot.herokuapp.com/')