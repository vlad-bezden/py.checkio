"""SendGrid Geo Stats mission

To solve this mission you must use the SendGrid API Key.
You should be able to operate with your statistical email data and SendGrid
has a lot of APIs that provide information you may need.
Your mission is to figure out which country opens your emails the most.
You can use this information in order to focus on a specific segment.

Input: Day as a string in format 'YYYY-MM-DD'
Output: String, Two-digit country code of country that has more unique clicks.
Example:
best_country('2016-01-01') == 'UA'

response example:
[
  {
    "date": "2014-10-01",
    "stats": [
      {
        "metrics": {
          "clicks": 0,
          "opens": 1,
          "unique_clicks": 0,
          "unique_opens": 1
        },
        "name": "US",
        "type": "country"
      }
    ]
  },
  {
    "date": "2014-10-02",
    "stats": [
      {
        "metrics": {
          "clicks": 0,
          "opens": 0,
          "unique_clicks": 0,
          "unique_opens": 0
        },
        "name": "US",
        "type": "country"
      }
    ]
  }
]
"""

import os
import json

import sendgrid

API_KEY = os.environ.get('SENDGRID_API_KEY')

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)


def best_country(str_date):
    response = sg.client.geo.stats.get(query_params={
        'start_date': str_date,
        'end_date': str_date
    })

    parsed_json = json.loads(response.body)
    data = [(x['stats'][0]['name'], x['stats'][0]['metrics']['unique_clicks'])
            for x in parsed_json]
    data.sort(key=lambda t: t[1], reverse=True)
    print(data)
    return data[0][0] if data else 'NA'


def main():
    try:
        # These "asserts" using only for self-checking and not necessary for
        # auto-testing
        result = best_country('2017-01-07')
        print(f"Your best country in 2016-01-01 was {result}")
        print('Check your results')
    except Exception as ex:
        print(ex)
        os.sys.exit(1)


if __name__ == '__main__':
    main()
    print('Done')
    os.sys.exit(0)
