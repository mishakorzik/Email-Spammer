R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'

import time, os, random, sys, json, argparse, requests, smtplib, time
import subprocess as subp
import logging

logger = logging.getLogger('dev')
logger.setLevel(logging.INFO)

fileHandler = logging.FileHandler('spammer.log')
fileHandler.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)

logger.info('Email Spammer - Started!')
row = []
info = ''
result = ''
systemR = '1.7.4'

def update_check():
    get = requests.get("https://raw.githubusercontent.com/mishakorzik/Email-Spammer/main/src/.version").text
    get = get.replace("\n", "")
    if get == systemR:
        print(f"\033[0mINFO: \033[92mno update found.")
    else:
        print(f"\033[0mINFO: \033[91mnew version found, please update tool from\n\033[0mINFO: \033[91mgithub.com/mishakorzik/Email-Spammer")

def exit_error():
    print(bcolors.FAIL + 'Works only with Gmail.')
    sys.exit()

def cls():
        if sys.platform == 'win32':
                # clear in windows, java
                os.system('cls')
        else:
                # clear in linux, android, ubuntu
                os.system('clear')

# gmail   : port = 587 , smtp_server = smtp.gmail.com
# outlook : port = 465 , smtp_server = smtp-mail.outlook.com
# yahoo   : port = 587 , smtp_server = smpt.mail.yahoo.com
# hotmail : port = 587 , smtp_server = smtp-mail.outlook.com
# Yandex  : port = 465 , smtp_server = smtp.yandex.com
# MailRu  : port = 587 , smtp_server = smtp.mail.ru

GMAIL_PORT = "587"
GMAIL_SSL_PORT = "465"
YAHOO_PORT = "587"
OUTLOOK_PORT = "587"
AOL_PORT = "587"
MAILRU_PORT = "465"

cls()

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

print(f"\033[0mWARN: \033[0;33myou are using the free version. Buy full version TG: @ubp2q")
print(f"\033[0mWARN: \033[0;33msending a message to email is supported only in English language.")
update_check()
print(bcolors.RAND + '''

▓█████  ███▄ ▄███▓ ▄▄▄       ██▓  ██▓      ██████  ██▓███   ▄▄▄       ███▄ ▄███▓
▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    ▓██▒ ▓██▒    ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒
▒███   ▓██    ▓██░▒██  ▀█▄  ▒██▒ ▒██░    ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░
▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██░ ▒██░      ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██
░▒████▒▒██▒   ░██▒ ▓█   ▓██▒░██░ ░██████▒▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒
░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░  ▒░▓  ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░
 ░ ░  ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░  ░ ▒  ░░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░
   ░   ░      ░     ░   ▒    ▒ ░  ░  ░   ░  ░  ░  ░░         ░   ▒   ░      ░
   ░  ░       ░         ░  ░ ░       ░  ░      ░                 ░  ░       ░
           .::.: EmailSpammer v1.7.4  Developer: misha korzhik :.::.''')

print(bcolors.WARNING + '''                                                                               
\033[95m[1] Gmail    -  powered google
[2] Anon E.  -  powered google
[3] Buy VIP  -  buy full version
[4] Exit     -  log out utility         ''')

try:
        server = input(bcolors.WARNING + 'Select option: ' + bcolors.ENDC)
        if server == '4' or server == '04' or server == 'exit' or server == 'Exit' or server == 'quit' or server == 'Quit':
                print(bcolors.FAIL + 'Exiting utility ...' + bcolors.ENDC)
                sys.exit()
        elif server == '1' or server == '01' or server == 'gmail' or server == 'Gmail':
                print('01. fire.send482@gmail.com')
                print('02. auto.send583@gmail.com')
                print(bcolors.WARNING + 'example: auto.send583@gmail.com' + bcolors.ENDC)
                user = input(bcolors.WARNING + 'Select email: ' + bcolors.ENDC)
                to = input(bcolors.LITBU + 'Sent To (жертва): ' + bcolors.ENDC)
                subject = input(bcolors.LITBU + 'Subject (заголовок): ' + bcolors.ENDC)
                body = input(bcolors.LITBU + 'Message (сообщение): ' + bcolors.ENDC)
                delay = input(bcolors.OKGREEN + 'Speed of sending letters (1-5): ' + bcolors.ENDC)
                nomes = int(input(bcolors.OKGREEN + 'Number of Emails to send (1-99): ' + bcolors.ENDC))
                logger.info('Email: '+user)
                logger.info('Target email: '+to)
                logger.info('Email list to send: '+str(nomes))
                en0 = 600
                if en0 <= nomes:
                        cls()
                        print(bcolors.FAIL + 'denied access: Error \nsending maximum number 599')
                        time.sleep(2)
                        os.execl(sys.executable, sys.executable, *sys.argv)
        elif server == '2' or server == '02' or server == 'anon' or server == 'Anon':
                print('01. jiki.mioli08@gmail.com')
                print(bcolors.WARNING + 'example: jiki.mioli08@gmail.com' + bcolors.ENDC)
                user = input(bcolors.WARNING + 'Select email: ' + bcolors.ENDC)
                to = input(bcolors.LITBU + 'Sent To (кому): ' + bcolors.ENDC)
                subject = input(bcolors.LITBU + 'Subject (заголовок): ' + bcolors.ENDC)
                body = input(bcolors.LITBU + 'Message (сообщение): ' + bcolors.ENDC)
                delay = '1'
                logger.info('One Email: '+user)
                logger.info('Target email: '+to)
                logger.info('Email list to send: Its a anonymous message! nomes: 0')
                delay_name = 'special'
        elif server == '3' or server == '03' or server == 'buy' or server == 'Buy':
                print("15$ (USD) - 50 emails per 12th. For 1 week")
                print("30$ (USD) - 100 emails per 12th. For 1 week")
                print("50$ (USD) - 200 emails per 12th. For 1 week")
                print("85$ (USD) - 400 emails per 12th. For 1 week")
                print("")
                print("if you want to buy, write to Telegram: @ubp2q")
                exit()
        no = 0
        if to == 'misakorzik528@gmail.com' or to == 'miguardzecurity@gmail.com' or to == 'korzikmisha@gmail.com':
                print(bcolors.FAIL + '\nWhat?  seems to have failed to process \nyour request, please try another email.' + bcolors.ENDC)
                sys.exit(0)
        if delay == '1' or delay == '01':
                SPEED = .1
                delay_name = 'fast'
        elif delay == '2' or delay == '02':
                SPEED = .3
                delay_name = 'medium'
        elif delay == '3' or delay == '03':
                SPEED = .5
                delay_name = 'slow'
        elif delay == '4' or delay == '04':
                SPEED = .7
                delay_name = 'unhurried'
        elif delay == '5' or delay == '05':
                SPEED = .9
                delay_name = 'snail'
        else:
                SPEED = .3
                delay_name = 'default'

        message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
except KeyboardInterrupt:
        print(bcolors.FAIL + 'Canceled! Quiting ...' + bcolors.ENDC)
        sys.exit()


#Gmail powered google
if server == '1' or server == '01' or server == 'gmail' or server == 'Gmail':
        if user == "fire.send482@gmail.com":
            pwd = "dpusbvnihmvncaob"
        elif user == "auto.send583@gmail.com":
            pwd = "awlgkpsurszifppt"
        start_bomb()
        print(bcolors.WARNING + 'Email: ' + user + '  Target: ' + to + '  Speed: ' + delay_name)
        print("")
        server = smtplib.SMTP("smtp.gmail.com", GMAIL_PORT)
        print(bcolors.WARNING + 'Starting TLS - server0.starttls()')
        server.starttls()
        try:
                print(bcolors.WARNING + 'Connecting - server0.login(u, p)')
                server.login(user, pwd)
        except smtplib.SMTPAuthenticationError:
                try:
                        print(bcolors.WARNING + 'Reconnecting - server0.login(u, p)')
                        server.login(user, pwd)
                except smtplib.SMTPAuthenticationError:
                        try:
                                print(bcolors.WARNING + 'Reconnecting - server0.login(u, p)')
                                server.login(user, pwd)
                        except smtplib.SMTPAuthenticationError:
                                print(bcolors.WARNING + 'Error to connect! Please use a mini version, select option 5...')
                                sys.exit()
        for i in range(1, nomes+1):
                logger.info('Done! Spaming...')
                try:
                        server.sendmail(user, to, message)
                        print(bcolors.WARNING + 'Successfully messenge sent! ' + str(no+1) + ' emails' + bcolors.ENDC)
                        no += 1
                        time.sleep(SPEED)
                except KeyboardInterrupt:
                        print(bcolors.FAIL + '\nTerminaling...' + bcolors.ENDC)
                        sys.exit()
                except:
                        server.sendmail(user, to, message)
                        print(bcolors.WARNING + 'Successfully messenge sent! ' + str(no+1) + ' emails' + bcolors.ENDC)
                        no += 1
                        time.sleep(SPEED)
        server.close()
        print(bcolors.FAIL + 'Proccess Terminated! restart program ..?')
        op = input(bcolors.FAIL + 'Do you want to continue (Y/n): ')
        if op == 'y' or op == 'Y' or op == 'Yes' or op == 'yes':
                os.execl(sys.executable, sys.executable, *sys.argv)

elif server == '2' or server == '02' or server == 'anon' or server == 'Anon':
        if user == "jiki.mioli08@gmail.com":
            pwd = "gzwjsohldzxdpteh"
        start_bomb()
        print(bcolors.WARNING + 'Email: ' + user + '  Send To: ' + to)
        print("")
        server = smtplib.SMTP("smtp.gmail.com", GMAIL_PORT)
        server.starttls()
        try:
                server.login(user, pwd)
        except smtplib.SMTPAuthenticationError:
                sys.exit()
        for i in range(1):
                logger.info('Done! Anonymous message...')
                try:
                        server.sendmail(user, to, message)
                        print(bcolors.WARNING + 'Successfully messenge sent! ' + str(no+1) + ' emails' + bcolors.ENDC)
                        no += 1
                        time.sleep(SPEED)
                except KeyboardInterrupt:
                        print(bcolors.FAIL + '\nTerminaling...' + bcolors.ENDC)
                        sys.exit()
                except:
                        print(bcolors.FAIL + "Messange failed to Send! ")
        server.close()
        print(bcolors.FAIL + 'Proccess Terminated! restart program ..?')
        op = input(bcolors.FAIL + 'Do you want to continue (Y/n): ')
        if op == 'y' or op == 'Y' or op == 'Yes' or op == 'yes':
                os.execl(sys.executable, sys.executable, *sys.argv)
else:
    exit_error()
