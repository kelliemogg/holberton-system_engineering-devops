#!/usr/bin/python3
""" returns a list with the titles of all hot articles for a subreddit """

import json
import requests


def recurse(subreddit, hot_list=[]):
    """ uses recursive function to query Reddit API """
    hotURL = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {"User-Agent": "user"}
    getDict = requests.get(
        hotURL,
        headers=headers,
        allow_redirects=False).json()
    forData = getDict.get("data")

    if 'data' not in getDict:
        print("None")
    else:
        forChildren = forData.get("children")
        for titles in forChildren[:10]:
            print(titles.get('data')['title']) 
