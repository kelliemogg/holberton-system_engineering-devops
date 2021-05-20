#!/usr/bin/python3
""" returns a list with the titles of all hot articles for a subreddit """

import json
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """ uses recursive function to query Reddit API """
    # passes in subreddit as arg to our url
    hotResponse = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    # reddit is picky about headers
    headers = {"User-Agent": "user"}
    # response for after query aka next page
    afterResponse = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    # gets correct json data for our desired subreddit page
    if after is None:
        response = requests.get(
            hotResponse,
            headers=headers,
            allow_redirects=False).json()
    else:
        response = requests.get(
            afterResponse,
            headers=headers,
            allow_redirects=False).json()

    forData = response.get("data")

    if 'data' not in response:
        return (None)
    else:
        children = forData.get("children")
        for child in children:
            this = child.get("data").get("title")
            hot_list.append(this)
            count += 1
    if after is None:
        return hot_list
    return (recurse(subreddit, hot_list, count, after))
