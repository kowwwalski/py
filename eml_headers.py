#!/usr/bin/python
import email
from email import policy
from email.parser import BytesParser
import re

with open('file.eml', 'rb') as eml:
    try:
        msg = BytesParser(policy=policy.default).parse(eml, headersonly=False)
    except Exception as e:
        print(e)

    print('Let see...\n')

    params = [
            'Received',
            'Authentication-Results',
            'From',
            'Return-Path',
            'Bcc',
            'Reply-To',
            'Bounces-To',
            'X-Distribution',
            'X-Mailer',
            'X-OriginatorOrg'
    ]

    for i in params:
        print('{}: '.format(i), msg.get('{}'.format(i)), '\n')

    try:
        msgBody = msg.get_body(preferencelist=('plain')).get_content()
    except Exception as e:
        print(e)

    links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', msgBody, re.I)

    if not links:
        print('No links in email')
    else:
        print('Links:')
        for l in links:
            print(l.strip("[]<>"))

eml.close()
