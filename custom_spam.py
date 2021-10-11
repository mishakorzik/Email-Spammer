import os
import sys

print("1. python1  -  .cpython-39.opt-2.pyc")
print("2. python3  -  .cpython-310.opt-2.pyc")
diya = input("Options: ")
if diya == '1' or diya == '01' or diya == 'python1' or diya == 'Python1':
	os.system("python src/custom_spam.cpython-39.opt-2.pyc")
if diya == '2' or diya == '02' or diya == 'python3' or diya == 'Python3':
	os.system("python3 src/custom_spam.cpython-310.opt-2.pyc")
