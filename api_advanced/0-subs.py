#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.
    
    subreddit: str, the name of the subreddit
    return: int, the number of subscribers or 0 if the subreddit is invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}  # Add a custom user agent to prevent errors

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'subscribers' in data['data']:
                return data['data']['subscribers']
        return 0
    except requests.RequestException:
        return 0
