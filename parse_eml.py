import os
import re
import email
from email import policy
from email.parser import Parser
from email.parser import BytesParser
# for all *.eml files in current directory – open and parse to plain text
for f_name in os.listdir('.'):
    if f_name.endswith('.eml'):
        with open(f_name, 'rb') as fp:  # for each file from the list
            msg = BytesParser(policy=policy.default).parse(fp)
        text = msg.get_body(preferencelist=('plain')).get_content()
        fullsubject = msg.get('Subject')
        # get data by templates
        subj = re.findall(r' %your_search_template% .*\w+', fullsubject, re.I)
        name = re.findall(r' %your_search_template% .*\w+', text, re.I)
        cont = re.findall(r' %your_search_template% .*\w+', text, re.I)
        print(name[0] + ';' + cont[0] + ';' + subj[0] + ';')
#
# then in my case I grab some unique data with "| awk '{print $1, $3, $n}' >> output.csv"
