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

import sendgrid

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))


def how_spammed(date):
    params = {'aggregated_by': 'day',
              'start_date': date, 'end_date': date, 'offset': 1}
    response = sg.client.stats.get(query_params=params)
    data = json.loads(response.body)

    return data[0]['stats'][0]['metrics']['spam_reports']


if __name__ == '__main__':
    # These asserts' using only for self-checking and not necessary
    # for auto-testing
    date = '2018-01-07'
    spams_count = how_spammed(date)

    print(f'You had {spams_count} spam reports in {date}')
