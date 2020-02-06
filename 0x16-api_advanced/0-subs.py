#!/usr/bin/python3
"""
this file has a function that queries the
number of susbscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns
    the number of subscribers (not active users,
    total subscribers) for a given subreddit.
    """

    # setting custom User-Agent.
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = requests.utils.default_headers()

    headers.update(
       {
        'User-Agent': 'My User Agent 1.0',
       }
    )

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:

        return 0
