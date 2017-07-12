#!/usr/bin/python

import bot  # contains private bot info

import praw

# creates praw Reddit instance
bot = praw.Reddit(user_agent = 'HHH PyBot v1',
                  client_id = bot.client_id,
                  client_secret = bot.client_secret,
                  username = bot.username,
                  password = bot.password)

# points bot to a specific subreddit
subreddit = bot.subreddit('hiphopheads')

# prints given number of posts from subreddit
posts = 10
for submission in subreddit.hot(limit = posts):
    print(submission.title)
    print("\tat ", submission.score, "\tby ", submission.author)
    print(submission.selftext)
    if len(submission.selftext) > 0:
        print()
    print("---------------------------------\n")