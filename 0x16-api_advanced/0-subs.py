#!/usr/bin/python3
""" This module uses flask to receive Reddit API """
import requests


def number_of_subscribers(subreddit):
    """ This methos counts the number of subscribers for one sub_r """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0"}
    n_of_subs = requests.get(url, headers=headers, allow_redirects=False)

    if n_of_subs:
        return n_of_subs.json()['data']["subscribers"]
    return 0
