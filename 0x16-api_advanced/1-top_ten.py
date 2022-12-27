#!/usr/bin/python3
""" This module uses flask to receive Reddit API """
import requests


def top_ten(subreddit):
    """ This method prints the top ten hot posts listed """

    url = 'https://www.reddit.com/r/{}/.json'.format(subreddit)
    headers = {"User-Agent": "Obed'sBrowser/5.0 (Windows NT 10.0)"}
    ten = requests.get(url, headers=headers)

    if ten:
        for top in range(10):
            print(ten.json()['data'][top]['data']['title'])
    else:
        print('None')
