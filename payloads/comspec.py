from operator import le
import subprocess
import sys

"""
This file get computer info and write it into wl.fg
"""

command = "systeminfo"
sysinfos = subprocess.check_output(command, shell=True) 
sysinfo = sysinfos.decode('latin_1', 'replace')
auxi = ""
auxi += "-- System Info \n"
auxi += str(sysinfo)
auxi += "\n"
print(auxi)