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
	sys_url = 'https://raw.githubusercontent.com/mishakorzik/Email-Spammer/main/src/.version'
	try:
		sys_rqst = requests.get(sys_url)
		sys_sc = sys_rqst.status_code
		if sys_sc == 200:
			github_sys = sys_rqst.text
			github_sys = github_sys.strip()

			if systemR == github_sys:
				print(C + '[' + G + ' Up-To-Date ' + C +']' + '\n')
				print(R + '[-] ' + C + 'successfully checked, no updates')
			else:
				print(C + '[' + R + ' Available : {} '.format(github_sys) + C + ']' + '\n')
				print(R + '[-] ' + C + 'Please update the system! reinstall repository...')
		else:
			print(C + '[' + R + ' Status : {} '.format(sys_sc) + C + ']' + '\n')
			print(R + '[-] ' + C + 'The system failed to start!')
			print(R + '[-] ' + C + 'Error code: 401 the server cannot boot')
	except Exception as e:
		print('\n' + R + '[-]' + C + ' Critical Error code: 105 Maybe you dont have internet - Exception : ' + W + str(e))

