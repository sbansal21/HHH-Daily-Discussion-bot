#!/usr/bin/python

import bot  # contains private bot info

import praw
import re
import os

# tracks which posts have already been visited
if not os.path.isfile("visited.txt"):
    visited = []
else:
    with open("visited.txt", "r") as f:
        visited = f.read().split("\n")
        visited = list(filter(None, visited))

# creates PRAW Reddit instance
bot = praw.Reddit(user_agent = 'HHH PyBot',
                  client_id = bot.client_id,
                  client_secret = bot.client_secret,
                  username = bot.username,
                  password = bot.password)

# points bot to a specific subreddit
subreddit = bot.subreddit('hiphopheads')

# iterates through 100 newest posts in subreddit
posts = 100
post = "Daily Discussion Thread"
comment = "yeezy yeezy what's good"
found = False
for submission in subreddit.hot(limit = posts):
    if submission.id not in visited:
        if re.search(post, submission.title, re.IGNORECASE):
            submission.reply(comment)
            found = True
            print("bot successfully commented in thread ", submission.id)
            visited.append(submission.id)
if not found:
    print("specified thread not found.")

with open("visited.txt", "w") as f:
    for post in visited:
        f.write(post + "\n")