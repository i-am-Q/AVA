import smtplib
from voice import talking
import config
from base64 import b64decode


# send_email sends an from pyemailsender@gmail.com to qbenbow@gmail.com
def send_email(my_msg, my_subj):
    # this can be a List of Email Ids
    email_list = config.mail_list

    for emailID in email_list:
        try:
            text = 'sending email to ' + emailID
            talking(text)
            username = config.mail_sender
            access = b64decode(config.mail_access)
            fromaddr = config.mail_sender
            toaddrs = emailID
            msg = 'Subject: Here is your ' + my_subj + ' from your personal assistant\r\n' + my_msg + \
                  '\nThis message was sent using my personal Python Assistant\n Python is Great !!!'
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(username, access)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()
            talking('your Email has been sent')

        except Exception, e:
            print e
