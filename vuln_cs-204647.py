import os
# CodeQL would flag: command injection
os.system("echo " + input())
