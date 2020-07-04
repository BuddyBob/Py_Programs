import smtplib
import config
from colorama import *
sub = (input(Fore.YELLOW+"What is the subject: "))
ask = (input(Fore.YELLOW+"Enter body: "))
recipients = 'airstalk3r@gmail.com'
def mult():
    for r in recipients:
        email = r
def send_email(subject,msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'subject: {}\n\n{}'.format(subject,msg)
        server.sendmail(config.EMAIL_ADDRESS,config.EMAIL_ADDRESS, message)
        server.quit()
        print(Fore.GREEN+'Email Sent!')
    except:
        print(Fore.RED+'email failed to send')


subject = str(sub)
msg = str(ask)
send_email(subject,msg)