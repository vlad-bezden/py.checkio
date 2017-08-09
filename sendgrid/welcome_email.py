"""Welcome Email by SendGrid

To solve this mission you must use the SendGrid API Key
It is all starts with your first email. Let’s try to send one.
Your mission is to create a function that sends a welcome email to a user.
The function gets two arguments: email and name of the user.
Subject of the email should be "Welcome" and body simply "Hi, {name}"
({name} should be replaced by users name)

Input: Two arguments. email and username
Output: None. You should send an email. You don’t need to return anything.
send_email('a.lyabah@checkio.org', 'oduvan')
send_email('somebody@gmail.com', 'Some Body')
"""

import os

import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content

API_KEY = os.environ.get('SENDGRID_API_KEY')
SUBJECT = 'Welcome'
SENDER = os.environ.get('SENDGRID_SENDER')
RECEIVER = os.environ.get('SENDGRID_RECEIVER')
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)


def send_email(email, name):
    from_email = Email(SENDER)
    to_email = Email(email)
    content = Content('text/plain', BODY.format(name))
    mail = Mail(from_email, SUBJECT, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


def main():
    try:
        send_email(RECEIVER, 'Vlad')
    except Exception as ex:
        print(ex)
        os.sys.exit(1)


if __name__ == '__main__':
    main()
    print('Done')
    os.sys.exit(0)
