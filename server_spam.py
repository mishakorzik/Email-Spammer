from sendtomail import *
import time, random, os, sys

def cls():
        if sys.platform == 'win32':
                # clear in windows, java
                os.system('cls')
        else:
                # clear in linux, android, ubuntu
                os.system('clear')

class bcolors:
        OKGREEN = '\033[92m'
        WARNING = '\033[0;33m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        LITBU = '\033[94m'
        YELLOW = '\033[3;33m'
        CYAN = '\033[0;36'
        colors = ['\033[92m', '\033[91m', '\033[0;33m']
        RAND = random.choice(colors)

class FG:
        black = "\033[30m"
        red = "\033[31m"
        green = "\033[32m"
        orange = "\033[33m"
        blue = "\033[34m"
        purple = "\033[35m"
        cyan = "\033[36m"
        lightgrey = "\033[37m"
        darkgrey = "\033[90m"
        lightred = "\033[91m"
        lightgreen = "\033[92m"
        yellow = "\033[93m"
        lightblue = "\033[94m"
        pink = "\033[95m"
        lightcyan = "\033[96m"

def start_bomb():
        cls()
        print(bcolors.OKGREEN + '''
[>] Prepare for spam and attack ...''')

cls()
print(bcolors.RAND + '''

▓█████  ███▄ ▄███▓ ▄▄▄       ██▓  ██▓      ██████  ██▓███   ▄▄▄       ███▄ ▄███▓
▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    ▓██▒ ▓██▒    ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒
▒███   ▓██    ▓██░▒██  ▀█▄  ▒██▒ ▒██░    ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░
▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██░ ▒██░      ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██
░▒████▒▒██▒   ░██▒ ▓█   ▓██▒░██░ ░██████▒▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒
░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░  ▒░▓  ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░
 ░ ░  ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░  ░ ▒  ░░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░
   ░   ░      ░     ░   ▒    ▒ ░  ░  ░   ░  ░  ░  ░░         ░   ▒   ░      ░
   ░  ░       ░         ░  ░ ░       ░  ░      ░                 ░  ░       ░''')
print(" ")
print(bcolors.WARNING + 'Using Alternative email spammer ' + bcolors.ENDC)

email = input(bcolors.WARNING + 'Sent To (жертва): ' + bcolors.ENDC)
text = input(bcolors.WARNING + 'Message (сообщение): ' + bcolors.ENDC)
nomes = int(int(input(bcolors.OKGREEN + 'Number of Emails to send (1-99): ' + bcolors.ENDC)))
en0 = 25
if en0 <= nomes:
    time.sleep(2)
    os.execl(sys.executable, sys.executable, *sys.argv)
    cls()

for i in range(nomes):
    try:
        code = server.send("ru", email, text)
        if code == '429':
            code = server.send("tr", email, text)
        print(code)
    
