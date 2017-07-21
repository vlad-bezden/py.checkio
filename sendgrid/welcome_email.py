import os

import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content

API_KEY = os.environ.get('SENDGRID_API_KEY')
SUBJECT = 'Welcome'
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)


def send_email(email, name):
    from_email = Email('vladbezden@yahoo.com')
    to_email = Email(email)
    subject = SUBJECT
    content = Content('text/plain', BODY.format(name))
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


def main():
    try:
        send_email('vladbezden@gmail.com', 'Vlad')
    except Exception as ex:
        print(ex)
        os.sys.exit(1)


if __name__ == '__main__':
    main()
    print('Done')
    os.sys.exit(0)
