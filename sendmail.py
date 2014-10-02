#!/usr/bin/env python3  
#coding: utf-8  
import smtplib  
handle = smtplib.SMTP('smtp.yeah.net', 25)  
handle.ehlo()  
handle.starttls()  
handle.ehlo()  
handle.login('crz0316@yeah.net', 'crz332066279')  
msg = "To: username@domain\r\nFrom: username@domain\r\
\nSubject: test \r\n\r\n test mail\r\n" 
handle.sendmail('crz0316@yeah.net','dengzuoheng@gmail.com', msg)  
handle.close() 