#!/usr/bin/python3
"""
this file contain a function that query the reddit API
for tittle of the first 10 hot posts lists
"""


def top_ten(subreddit):
    """
     function that queries the Reddit API
    :param subreddit: particular topic of the website reddit
    :return: ints the titles of the first 10 hot posts
    listed for a given subreddit
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
        childrens = response.json().get('data').get('children')
        for children in childrens:
            title = children.get('data').get('title')
            print(title)
    else:
        return print('None')
