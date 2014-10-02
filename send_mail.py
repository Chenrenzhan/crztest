


import smtplib
import sys
#import email.mime.text
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

import time
import datetime

# to_addrs: 发送给谁 
# subject: 主题
# context: 内容
def send_mail(to_addrs, subject, content):
    host = 'smtp.gmail.com'
    post = 25
    
    server = smtplib.SMTP(host, post)
    server.ehlo()  
    server.starttls()  
    server.ehlo()
        
    try:
        server.login('dengzuoheng@gmail.com', 'ainsophaur000')
    except:
        print('LOGIN FAIL')
        sys.exit(1)
    
    msg = MIMEText(content,_charset='utf-8') 
    #msg['From'] = "from_addr"
    msg['To'] = to_addrs
    msg['Subject'] = subject
    #msg['Date'] = formatdate(localtime=True) #不止为何设置不了时间
    #server.sendmail('dengzuoheng@gmail.com', to_addrs, msg.as_string())
    server.send_message(msg, 'dengzuoheng@gmail.com', to_addrs) #发送Message实例
    server.quit()
    
    print('send mail success!')

    
content = 'test_text2014102'
send_mail('1039939475@qq.com','test_subject', content)