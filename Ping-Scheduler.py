import requests
import schedule
import time

from datetime import datetime

def ping_server():
    try:
        print('start pinging')
        response = requests.get("https://topazio-shop-backend.onrender.com")
        if response.status_code == 200:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - PING SUCCESS")
        else:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - PING FAILED (Status Code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - PING FAILED ({e})")

def job():
    current_time = datetime.now().strftime('%H:%M:%S')
    if "08:00:00" <= current_time <= "22:00:00":
        ping_server()

schedule.every(5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
