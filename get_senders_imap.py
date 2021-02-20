#!/usr/bin/python3
import imaplib, email, email.utils
import getpass
import re
#import csv

# you can set server and username directly in script, but I highly recommend using getpass in pwd section for security reasons
hostname = input('Enter your imap server address:\n')
username = input('Enter your username:\n')
password = getpass.getpass()

connection = imaplib.IMAP4_SSL(hostname)
connection.login(username, password)

with connection as c:
    c.select('%folder_name%', readonly=True) # set some folder into your mailbox
    return_code, data = c.search(None, '(SINCE "01-Jan-1970" BEFORE "01-Jan-2020")') # set date from-to
    mail_ids = data[0].decode()
    id_list = mail_ids.split()
    first_id = int(id_list[0])
    last_id = int(id_list[-1])
    addr_list = []
    for i in range(first_id, last_id+1, 1):
        typ, data = c.fetch(str(i), "(BODY[HEADER.FIELDS (FROM)])")
        #print(data)
        for a in data:
            addr = re.findall('<(.*?)>', str(a))
            if not addr:
                pass
            else:
                #print(addr)
                addr_list += addr
    print(addr_list)
#                with open('senders_list.csv', mode='a') as senders_list:
#                    addr_writer = csv.writer(senders_list, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#                    addr_writer.writerow(addr)
    connection.close()
#
# uncomment csv sections to save output in csv-file
