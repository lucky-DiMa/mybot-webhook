import time, requests
import main
if __name__  == '__activator__':
    main.main()
    requests.post('https://my-updater.herokuapp.com/')