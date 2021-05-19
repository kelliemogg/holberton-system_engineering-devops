#!/usr/bin/python3
""" queries the Reddit API and returns the number of subs """

import json
import requests


def number_of_subscribers(subreddit):
    """ returns number of subscribers """
    subURL = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    headers = {"User-Agent": "user"}
    getDict = requests.get(
        subURL,
        headers=headers,
        allow_redirects=False).json(
    )

    if "data" not in getDict:
        return 0
    else:
        getSubs = getDict.get("data")
        return (getSubs["subscribers"])
