#!/usr/bin/python

import smtplib

gmail_user = 'jagatjyoti0@gmail.com'
gmail_pwd = 'user@1234'
FROM = 'jagatjyoti0@gmail.com'
TO = 'jagatjyoti0@gmail.com' if type('jagatjyoti0@gmail.com') is list else ['jagatjyoti0@gmail.com']
SUBJECT = 'Test mail'
TEXT = 'Hi there! This is just a test mail using smtplib module in python'

# Prepare actual message
message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
try:
    server_ssl = smtplib.SMTP("smtp.gmail.com", 465 )
    server_ssl.ehlo()
    server_ssl.starttls()
    server_ssl.login(gmail_user, gmail_pwd)
    server_ssl.sendmail(FROM, TO, message)
    server_ssl.close()
    print 'successfully sent the mail'
except:
    print "failed to send mail"
