import smtplib
from email.message import EmailMessage
msg = EmailMessage()


def SendEmail(received_email,message):


    # receive_email = "**********
    password = '9828086689qwer'
   
    msg['Subject'] = "Response From Todo  ---Suman Aryal"
    msg['From'] = 'sumanaryal83p3@gmail.com'
    msg['To'] = str(received_email)
    msg.set_content(message)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('sumanaryal83p3@gmail.com', password)
    server.send_message(msg)
    return

