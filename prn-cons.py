#!/usr/bin/python3
# works fine with Canon MFPs, for example, iRA C5535i, and obviously you'll need to change OIDs for your devices
import subprocess
import re
import time
class color:
    RED = '\033[1;31;48m'
    GREEN = '\033[1;32;48m'
    BLACK = '\033[1;30;48m'
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
# strip full snmp strings to digits list
    black = re.findall(r'[0-9]*\d+', blackstr)
    cyan = re.findall(r'[0-9]*\d+', cyanstr)
    magenta = re.findall(r'[0-9]*\d+', magentastr)
    yellow = re.findall(r'[0-9]*\d+', yellowstr)
#
# output stuff in a pseudo-table style
    print("=" * 32)
#
    if int(black[-1]) > 60:
        print('{}\n'.format(name) + 'black cartridge is near ' + color.GREEN + '{}%'.format(black[-1]) + color.END)
    elif int(black[-1]) < 10:
        print('{}\n'.format(name) + 'black cartridge is near ' + color.RED + '{}%'.format(black[-1]) + color.END)
    else:
        print('{}\n'.format(name) + 'black cartridge is near {}%'.format(black[-1]))
#
    if not cyan:
        pass
    else:
        if int(cyan[-1]) > 60:
            print(color.CYAN + 'cyan ' + color.END + 'cartridge is near ' + color.GREEN + '{}%'.format(cyan[-1]) + color.END)
        elif int(cyan[-1]) < 10:
            print(color.CYAN + 'cyan ' + color.END + 'cartridge is near ' + color.RED + '{}%'.format(cyan[-1]) + color.END)
        else:
            print(color.CYAN + 'cyan ' + color.END + 'cartridge is near {}%'.format(cyan[-1]))
#
    if not magenta:
        pass
    else:
        if int(magenta[-1]) > 60:
            print(color.MAGENTA + 'magenta ' + color.END + 'cartridge is near ' + color.GREEN + '{}%'.format(magenta[-1]) + color.END)
        elif int(magenta[-1]) < 10:
            print(color.MAGENTA + 'magenta ' + color.END + 'cartridge is near ' + color.RED + '{}%'.format(magenta[-1]) + color.END)
        else:
            print(color.MAGENTA + 'magenta ' + color.END + 'cartridge is near {}%'.format(magenta[-1]))
#
    if not yellow:
        pass
    else:
        if int(yellow[-1]) > 60:
            print(color.YELLOW + 'yellow ' + color.END + 'cartridge is near ' + color.GREEN + '{}%'.format(yellow[-1]) + color.END)
        elif int(yellow[-1]) < 10:
            print(color.YELLOW + 'yellow ' + color.END + 'cartridge is near ' + color.RED + '{}%'.format(yellow[-1]) + color.END)
        else:
            print(color.YELLOW + 'yellow ' + color.END + 'cartridge is near {}%'.format(yellow[-1]))
#
    print("=" * 32)
    time.sleep(2)
