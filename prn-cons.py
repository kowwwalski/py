#!/usr/bin/python3
# works fine with Canon MFPs, for example, iRA C5535i, and obviously you'll need to change OIDs for your devices
import subprocess
import re
import time
class color:
    #RED = '\033[1;31;48m'
    #BLACK = '\033[1;30;48m'
    MAGENTA = '\033[1;35;48m'
    CYAN = '\033[1;36;48m'
    YELLOW = '\033[1;33;48m'
    END = '\033[1;37;0m'
#
# put your devices names and ip-addresses in that dict
printers = { 'printer1': '10.99.13.34', 'printer2': '10.99.13.35', 'printer3': '10.99.13.36', 'printer4': '10.99.13.37' }
#
# here we trying to get full snmp string (and convert in to str type) for each cartridge on all devices
for name, ip in printers.items():
    blackstr = (subprocess.check_output("snmpwalk -v 1 -c public %s 1.3.6.1.2.1.43.11.1.1.9.1.1" % ip, shell=True, stderr=subprocess.STDOUT)).decode("utf-8")
    cyanstr = (subprocess.check_output("snmpwalk -v 1 -c public %s 1.3.6.1.2.1.43.11.1.1.9.1.2" % ip, shell=True, stderr=subprocess.STDOUT)).decode("utf-8")
    magentastr = (subprocess.check_output("snmpwalk -v 1 -c public %s 1.3.6.1.2.1.43.11.1.1.9.1.3" % ip, shell=True, stderr=subprocess.STDOUT)).decode("utf-8")
    yellowstr = (subprocess.check_output("snmpwalk -v 1 -c public %s 1.3.6.1.2.1.43.11.1.1.9.1.4" % ip, shell=True, stderr=subprocess.STDOUT)).decode("utf-8")
#
# let's strip full snmp strings to just last int value
    black = re.findall(r': [0-9]*\w+', blackstr, re.I)
    cyan = re.findall(r': [0-9]*\w+', cyanstr, re.I)
    magenta = re.findall(r': [0-9]*\w+', magentastr, re.I)
    yellow = re.findall(r': [0-9]*\w+', yellowstr, re.I)
#
# output stuff in a pseudo-table style
    print("=" * 32)
    print('{}\n'.format(name) + 'black cartridge is near{}%'.format(black[0]))
#
    if not cyan:
        pass
    else:
        print(color.CYAN + 'cyan ' + color.END + 'cartridge is near{}%'.format(cyan[0]))
#
    if not magenta:
        pass
    else:
        print(color.MAGENTA + 'magenta ' + color.END + 'cartridge is near{}%'.format(magenta[0]))
#
    if not yellow:
        pass
    else:
        print(color.YELLOW + 'yellow ' + color.END + 'cartridge is near{}%'.format(yellow[0]))
#
    print("=" * 32)
    time.sleep(2)
