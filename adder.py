A_VERSION = 1.0
from colorama import Fore

#FUNC (ADD PAYLOAD TO FILE) (STRING) (STRING) (STRING) (BOOLEAN)
def aptf(ptype, pname, fname, *prepeat):
    if prepeat != True and prepeat != False:
        prepeat = False
    print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}\\{Fore.YELLOW}]{Fore.RESET} Adding {pname} to {fname} {Fore.YELLOW}  ({ptype}) ({prepeat}){Fore.RESET}")