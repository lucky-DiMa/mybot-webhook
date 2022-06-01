import time, requests
import main
if __name__ == '__activator__':
    main.main()
    while True:
        time.sleep(60)
        requests.post(main.APP_URL)