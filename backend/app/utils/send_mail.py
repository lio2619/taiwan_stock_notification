from app import app
#from app import mail

from threading import Thread
from flask_mail import Message

def send_async_email(app, msg):
    from app import mail
    with app.app_context():
        mail.send(msg)

def send_mail(msg_title, email_recipients, msg_information):
    msg_sender     = app.config['MAIL_USERNAME']
    msg_recipients = [email_recipients]
    
    msg      = Message(msg_title, sender = msg_sender, recipients = msg_recipients)
    msg.body = msg_information

    thr = Thread(target = send_async_email, args = [app, msg])
    thr.start()