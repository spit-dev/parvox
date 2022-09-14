A_VERSION = 1.0
from colorama import Fore

#FUNC (ADD PAYLOAD TO FILE) (STRING) (STRING) (STRING)
def aptf(ptype, pname, fname):
    print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}\\{Fore.YELLOW}]{Fore.RESET} Adding {pname} to {fname} {Fore.YELLOW}  ({ptype}){Fore.RESET}")