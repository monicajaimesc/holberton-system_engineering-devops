#!/usr/bin/python3
"""
file that contains a query function
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    recursive function that queries the Reddit API
    :param after: is the next page
    :param subreddit: particular topic of the website reddit
    :param hot_list: titles of all hot articles
    :return: list containing the titles of all hot
     articles for a given subreddit.
    """
    # setting custom User-Agent.
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'My User Agent 1.0.555',
        }
    )

    # print(after)
    if after is None:
        request = requests.get('https://www.reddit.com/r/{}/hot.json?limit=100'
                               .format(subreddit), headers=headers)
        if request.status_code != 200:
            return None
        data = request.json().get('data')
        childrens = data.get('children')
        if not childrens:
            return None
        for children in childrens:
            hot_list.append(children.get('data').get('title'))
        recurse(subreddit, hot_list, data.get('after'))
    else:
        request = requests.get('https://www.reddit.com/r/{}/'
                               'hot.json?limit=100&after={}'
                               .format(subreddit, after), headers=headers)
        data = request.json().get('data')
        childrens = data.get('children')
        for children in childrens:
            hot_list.append(children.get('data').get('title'))
        # print(data.get('after'))
        if data.get('after') is None:
            return hot_list
        else:
            recurse(subreddit, hot_list, data.get('after'))
    return hot_list
