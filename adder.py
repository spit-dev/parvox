A_VERSION = 1.0
from colorama import Fore

#FUNC (ADD PAYLOAD TO FILE) (STRING) (STRING) (STRING)
def aptf(pname, fname):
    print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}\\{Fore.YELLOW}]{Fore.RESET} Adding {pname} to {fname} {Fore.YELLOW} (HAPPY HACKING) {Fore.RESET}")
    ffp = open(f"./payloads/{pname}", "r")
    fftp = open(f"./output/{fname}", "a")
    for i in ffp.readlines():
        print(f"{Fore.LIGHTGREEN_EX}{i}{Fore.RESET}")
        fftp.write(i)
        print("[%] Added line.")
