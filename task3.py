import requests
import time
from datetime import date, timezone, timedelta
from pprint import pprint as p


def print_all_questions_2_days_ago():
    dt = date.today().replace() - timedelta(days=2)
    timestamp = int(time.mktime(dt.timetuple()))
    # print(timestamp)
    # timestamp = 1644105600

    current_page = 1
    base_url = 'https://api.stackexchange.com/'
    request = f'2.3/questions?page={current_page}&fromdate={timestamp}&order=desc&sort=activity&tagged=python&site=stackoverflow'
    current_request = base_url + request

    while True:
        request = f'2.3/questions?page={current_page}&fromdate={timestamp}&order=desc&sort=activity&tagged=python&site=stackoverflow'
        current_request = base_url + request
        current_response = requests.get(current_request).json()

        print(f'--- {current_page} page ---')
        p(current_response)
        print(f'--- end of {current_page} page ---')

        if not current_response['has_more']:
            break

        current_page += 1


print_all_questions_2_days_ago()


