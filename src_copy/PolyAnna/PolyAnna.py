import numpy as np
import itertools
import os
import sys
import smtplib
from email.mime.text import MIMEText

emails = {
    'Britty':  'brittania.ganor@me.com',#
    'Erika':   'Erika.mainart@gmail.com',#
    'Julia':   'juliakotyla@icloud.com',#
    'Helen':   'bosslady918@comcast.net',#
    'John':    'jkotyla@comcast.net',#
    'JP':      'jkotyla@tepper.cmu.edu',#
    'Len':     'lmainart4@gmail.com'#
         }

cant_match = {
    'Britty': ['JP'],
    'Erika': ['Len'],
    'Julia': [''],
    'Helen': ['John'],
    'John': ['Helen'],
    'JP': ['Britty'],
    'Len': ['Erika']
    }

def find_matches(Emails = emails):

    matches = {}
    perms = list(itertools.permutations(range(len(Emails))))
    names = Emails.keys()

    done = False
    while( not done ):

        r = np.random.uniform(0,len(perms),size = 1)
        pairs = perms[int(r)]
        matches = {name: names[pairs[i]] for i,name in enumerate(names)}

        for giver,reciever in matches.iteritems():
            if (giver == reciever or (reciever in cant_match[giver])):
                done = False
                break
            else:
                done = True
    return matches


# def send_emails(matches):
#
#     s = smtplib.SMTP('localhost', 1025)
#     for giver,reciever in matches.iteritems():
#         # fp = open('/Users/jpkotyla/Desktop/'+reciever+'_polyanna.txt', 'rb')
#         fp = open('/Users/jpkotyla/Desktop/John_polyanna.txt', 'rb')
#         msg = MIMEText(fp.read())
#         fp.close()
#
#         #me = 'jkotyla @ tepper.cmu.edu'
#         me = 'jpkotyla@gmail.com'
#
#         recipient = emails[recipient]
#         recipient = 'jkotyla@tepper.cmu.edu'
#
#         msg['Subject'] = 'PolyAnna Info'
#         msg['From'] = me
#         msg['To'] = recipient
#         s.sendmail(me, [recipient], msg.as_string())
#     s.quit()

def create_files(matches):
    curr = os.getcwd()
    os.chdir('/Users/jpkotyla/Desktop/Programming/Python/Projects/Polyanna2')
    [os.system('cp '+reciever+'_pollyanna.txt '+giver+'_sendTo.txt')
     for giver,reciever in matches.iteritems()]
    os.chdir(curr)


matches = find_matches(emails)
print matches
create_files(matches)

