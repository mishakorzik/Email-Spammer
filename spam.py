import smtplib
import time
import os
import getpass
import sys

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	LITBU = '\033[94m'


def bomb():
	os.system('clear')
	print bcolors.OKGREEN + '''                            																											
[>] Preparing and attacking ...
[>] Pending ...



