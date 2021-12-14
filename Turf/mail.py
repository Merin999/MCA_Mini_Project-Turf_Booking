import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# from Hostel.models import Hostel


def mail(toaddr, tname, sta):

    fromaddr = "ramesh.v7439@gmail.com"

    # instance of MIMEMultipart
    msg = MIMEMultipart()
    # toaddr = "ankitpchandran353@gmail.com"
    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Turf Activation Details"
    # msg['Subject'] = subject

    # string to store the body of the mail

    # attach the body with the msg instance

    html = """
    <html>
      <head></head>
      <body>
      <p>mr/ms:<br>"""+toaddr+"""

        </p>
        <p>Your turf:<br>"""+tname+""" is """+sta+"""

        </p> <br>
        <p> Join Link <br>
           Check it out <a href = "http://127.0.0.1:8000/LoginView"> Login now </a> .
        </p>
      </body>
    </html>
    """

    msg.attach(MIMEText(html, 'html'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "ramesh@123")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


def ownermail(toaddr, sta):

    fromaddr = "ramesh.v7439@gmail.com"

    # instance of MIMEMultipart
    msg = MIMEMultipart()
    # toaddr = "ankitpchandran353@gmail.com"
    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Account Activation Details"
    # msg['Subject'] = subject

    # string to store the body of the mail

    # attach the body with the msg instance

    html = """
    <html>
      <head></head>
      <body>
      <p>mr/ms:<br>"""+toaddr+"""

        </p>
        <p>Your Play Spots Account will """+sta+"""...

        </p> <br>
        <p> Join Link <br>
           Check it out <a href = "http://127.0.0.1:8000/LoginView"> Login now </a> .
        </p>
      </body>
    </html>
    """

    msg.attach(MIMEText(html, 'html'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "ramesh@123")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


def bookmail(toaddr, tname, bdate):

    fromaddr = "ramesh.v7439@gmail.com"

    # instance of MIMEMultipart
    msg = MIMEMultipart()
    # toaddr = "ankitpchandran353@gmail.com"
    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "New Booking Alert"
    # msg['Subject'] = subject

    # string to store the body of the mail

    # attach the body with the msg instance

    html = """
    <html>
      <head></head>
      <body>
      <p>mr/ms:<br>"""+toaddr+"""

        </p>
        <p>Your turf """ + tname + """ will booked at """ + bdate + """...

        </p> <br>
        <p> Join Link <br>
           Check it out <a href = "http://127.0.0.1:8000/LoginView"> Login now </a> .
        </p>
      </body>
    </html>
    """

    msg.attach(MIMEText(html, 'html'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "ramesh@123")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


def passresetmail(toaddr, password):

    fromaddr = "ramesh.v7439@gmail.com"

    # instance of MIMEMultipart
    msg = MIMEMultipart()
    # toaddr = "ankitpchandran353@gmail.com"
    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Password remaider details"
    # msg['Subject'] = subject

    # string to store the body of the mail

    # attach the body with the msg instance

    html = """
    <html>
      <head></head>
      <body>
      <p>mr/ms:<br>"""+toaddr+"""

        </p>
        <p>Your play spots password is """ + password + """

        </p> <br>
        <p> Join Link <br>
           Check it out <a href = "http://127.0.0.1:8000/LoginView"> Login now </a> .
        </p>
      </body>
    </html>
    """

    msg.attach(MIMEText(html, 'html'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "ramesh@123")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()
