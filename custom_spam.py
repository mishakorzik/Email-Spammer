import argparse
import os
import sys
import requests
import time

try:
        requests.get("http://flyzero.000webhostapp.com/project/email-spammer/custom/Ip6.php")
        os.system("python src/version.py")
        time.sleep(1)
        os.system("python src/custom_spam.cpython-310.opt-2.pyc")
except KeyboardInterrupt:
        sys.exit()
