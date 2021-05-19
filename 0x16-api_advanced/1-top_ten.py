#!/usr/bin/python3
""" queries the Reddit API and returns the number of subs """

import requests
import json

def top_ten(subreddit):
    """ returns top ten hot posts of a subreddit """
    hotURL = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {"User-Agent": "user"}
    getDict = requests.get(hotURL, headers=headers, allow_redirects=False).json()
    #json_response = getDict.json()
    forData = getDict.get("data")
    forChildren = forData.get("children")

    if 'data' not in getDict:
        return("None")
    for titles in forChildren[:10]:
        print(titles.get('data')['title'])

            