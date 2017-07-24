#!/usr/bin/python3

import datetime

import praw
import re
import os

import runpy
import edit

# ensures settings properly initialized
runpy.run_path("edit.py")

import settings

# tracks which posts have already been visited
if not os.path.isfile("visited.txt"):
    visited = []
else:
    with open("visited.txt", "r") as file:
        visited = file.read().split("\n")
        visited = list(filter(None, visited))

# creates PRAW Reddit instance
bot = praw.Reddit(user_agent = 'HHH PyBot',
                  client_id = settings.client_id,
                  client_secret = settings.client_secret,
                  username = settings.username,
                  password = settings.password)

# points bot to a specific subreddit
subreddit = bot.subreddit('hiphopheads')

timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') + "\t\t"
success = "bot successfully commented in thread "
failure = "specified thread not found."

# iterates through 100 newest posts in subreddit
trigger = "Daily Discussion Thread"
comment = "yeezy yeezy what's good"
found = False
for submission in subreddit.new(limit = 100):
	if submission.id not in visited:
		if re.search(trigger, submission.title, re.IGNORECASE):
			submission.reply(comment)
			found = True
			print(timestamp + failure)
			visited.append(submission.id)

# logs triggered submissions as visited
with open("visited.txt", "w") as file:
	for post in visited:
		file.write(post + "\n")
