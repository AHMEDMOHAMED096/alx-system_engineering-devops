#!/usr/bin/python3
"""Import requests module"""
import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API
    and returns the number of subscribers"""
    header = {"User-Agent": "MyRedditScript/0.1"}

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers=header, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        else:
            return 0
    except Exception as e:
        return 0
