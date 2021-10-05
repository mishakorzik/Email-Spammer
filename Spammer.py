import random
import smtplib
import time
import os
import getpass
import sys
import base64

# gmail   : port = 587 , smtp_server = smtp.gmail.com
# outlook : port = 587 , smtp_server = smtp-mail.outlook.com
# yahoo   : port = 465 , smtp_server = smpt.mail.yahoo.com
# hotmail : port = 587 , smtp_server = smtp-mail.outlook.com

GMAIL_PORT = "587"
YAHOO_PORT = "465"
OUTLOOK_PORT = "587"

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

def gmail():
	server = smtplib.SMTP("smtp.gmail.com", GMAIL_PORT)
	server.ehlo()
	server.starttls()
	try:
		server.login(user1, pwd1)
	except smtplib.SMTPAuthenticationError:
		sys.exit()
	for i in range(1, nomes+1):
		try:
			server.sendmail(user1, to, message)
			print(bcolors.WARNING + 'Successfully messenge sent! ' + str(no+1) + ' emails' + bcolors.ENDC)
			no += 1
		except KeyboardInterrupt:
			print(bcolors.FAIL + '\nTerminaling...' + bcolors.ENDC)
			sys.exit()
		except:
			print("Messange failed to Send! ")
	server.close()


#Yahoo powered microsoft
def yahoo():
	server = smtplib.SMTP("smtp.mail.yahoo.com", YAHOO_PORT)
	server.starttls()
	try:
		server.login(user1, pwd1)
	except smtplib.SMTPAuthenticationError:
		sys.exit()
	for i in range(1, nomes+1):
		try:
			server.sendmail(user1, to, message)
			print(bcolors.WARNING + 'Successfully messenge sent! ' + str(no + 1) + ' emails' + bcolors.ENDC)
			no += 1
		except KeyboardInterrupt:
			print(bcolors.FAIL + '\nTerminaling...' + bcolors.ENDC)
			sys.exit()
		except:
			print("Messange failed to Send!")
	server.close()
	
# Outlook powered microsoft
def outlook():
	server = smtplib.SMTP("smtp-mail.outlook.com", OUTLOOK_PORT)

	server.ehlo()
	server.starttls()
	try:
		server.login(user1, pwd1)
	except smtplib.SMTPAuthenticationError:
		sys.exit()
	for i in range(1, nomes+1):
		try:
			server.sendmail(user1, to, message)
			print(bcolors.WARNING + 'Successfully messenge sent! ' + str(no + 1) + ' emails' + bcolors.ENDC)
			no += 1
		except KeyboardInterrupt:
			print(bcolors.FAIL + '\nTerminaling...' + bcolors.ENDC)
			sys.exit()
		except smtplib.SMTPAuthenticationError:
			print('\nThe username or password you entered is incorrect.')
			sys.exit()
		except:
			print("Messange failed to Send!")
	server.close()
