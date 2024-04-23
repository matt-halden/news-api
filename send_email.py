import smtplib  # used for sending emails
import ssl

# to store a password securely, import your relative os library to get env variable
# in terminal, run this: touch ~/.zshrc; open ~/.zshrc
# create local env variables in this, give actual pw to gmail account
# secures password to our mac, other people could see our password if we have it right here
import os

def send_email(message):
    host = "smtp.gmail.com"  # standard gmail smtp host
    port = 465

    username = "mjah.py@gmail.com"  # enter my app email
    password = os.getenv("PASSWORD")
    #password = ""  # app password, not secure, recommended to use environment variables

    receiver = "mjah.py@gmail.com"  # same as username or whatever # we want
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)