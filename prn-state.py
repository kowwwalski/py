#!/usr/bin/python3
# just check network accessibility for each device in dict and output status to stdout
import subprocess

class color:
    GREEN = '\033[1;32;48m'
    RED = '\033[1;31;48m'
    END = '\033[1;37;0m'

printers = { 'printer1': '10.99.13.34', 'printer2': '10.99.13.35', 'printer3': '10.99.13.36', 'printer4': '10.99.13.37' }

for name, ip in printers.items():
    state = subprocess.call("ping -c 3 %s" % ip, shell=True, stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT)
    if state == 0:
        print("{} is ".format(name) + color.GREEN + "UP" + color.END)
    else:
        print(color.RED + "Smth is wrong with {}".format(name) + " ({})".format(ip) + color.END)
