import os
import sys
import time
import glob
import shutil
import socket
import subprocess
import threading
import ctypes
import requests
import base64
import winreg as reg
from colorama import Fore, init, Back
import winshell
import win32com.client
import win32api, win32con
from dikz_funcs import *

os_comp()
init()
cls()
logo_com()
print(f"""
Welcome to Dikz terminal, type "help" to get program commands.

""")
# fakiu=open("adder.py","r");print(fakiu.readlines());
with open("main.py","r") as f:
    print(f.read())

def comandeget():
    commande = input(f"{Fore.RED}[{Fore.YELLOW}%{Fore.RED}]{Fore.RESET} {Fore.RED}[{Fore.YELLOW}Dikz Terminal{Fore.RED}] > {Fore.RESET}")
    if commande == "help":
        print("""
        """)
    else:
        eval(commande)

while True:
    comandeget()
# aptf("deps.py", "mlw.py")
