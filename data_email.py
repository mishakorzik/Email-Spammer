import argparse
import os
import sys
import requests
import time

try:
        os.system("python src/version.py")
        time.sleep(1)
        os.system("python src/data_email.cpython-310.opt-2.pyc")
except KeyboardInterrupt:
        sys.exit()
