'''
You are massively sending thousands and thousands emails every day,
meanwhile experimenting with subject lines and the message itself.
SendGrid allows you to see statistics of your spam reports.

Your mission is to figure out how many spam reports you receive
on a specific day.

Input: Day as a string in format 'YYYY-MM-DD'

Output: Int. The amount of spam reports
'''

import os
import json
from datetime import datetime
from datetime import timedelta

import sendgrid

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))


def how_spammed(str_date):
    start_date = datetime.strptime(str_date, '%Y-%m-%d')
    end_date = start_date + timedelta(days=1)

    response = sg.client.suppression.spam_reports.get(query_params={
        'end_time': int(end_date.timestamp()),
        'start_time': int(start_date.timestamp())
    })

    data = json.loads(response.body)

    return len(data)


if __name__ == '__main__':
    # These asserts' using only for self-checking and not necessary
    # for auto-testing
    date = '2014-5-5'
    spams_count = how_spammed(date)

    print(f'You had {spams_count} spam reports in {date}')
