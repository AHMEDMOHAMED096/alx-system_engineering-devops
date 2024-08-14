#!/usr/bin/python3
"""Import requests module"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit"""
    headers = {"User-Agent": "MyRedditScript/0.1"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", None)
            if posts is not None:
                posts = posts.get("children", None)
            else:
                posts = None
        if posts is not None:
            for post in posts:
                print(post["data"]["title"])
        else:
            print(None)
    except Exception as e:
        print(None)
