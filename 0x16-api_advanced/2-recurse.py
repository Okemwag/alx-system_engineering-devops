#!/usr/bin/python3
""" This module uses recursion to retrieve a paginated json """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ This method recursively retrieves an API """

    articles = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ObedBrowser/v1.0.9"}
    params = {"after": after, 'limit': 100}
    response = requests.get(articles, headers=headers, params=params,
                            allow_redirects=False).json()

    resp = response  # For columns to be less in line 19
    if 'data' in response and 'children' in response.get('data'):
        for i in response.get('data').get('children'):
            hot_list.append(i.get('data').get('title'))

        if 'after' in resp.get('data') and resp.get('data').get('after'):
            return recurse(subreddit, hot_list, resp.get('data').get('after'))
        else:
            return hot_list
    return None
