#!/usr/bin/python3

import datetime

import praw
import re
import os
import sys
from edit import settings, setupClient, loadPrefs, verifyCommenter
import configparser

# ensures settings properly initialized
if not os.path.isfile(settings):
	setupClient()

config = loadPrefs()

# tracks which posts have already been visited
if not os.path.isfile("visited.txt"):
	visited = []
else:
	with open("visited.txt", "r") as file:
		visited = file.read().split("\n")
		visited = list(filter(None, visited))

# creates PRAW Reddit instance
bot = praw.Reddit(user_agent = 'HHH PyBot',
                  client_id = config.get('client', 'client_id'),
                  client_secret = config.get('client', 'secret'),
                  username = config.get('client', 'username'),
                  password = config.get('client', 'password'))

# points bot to a specific subreddit
subreddit = bot.subreddit("hiphopheads")

timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') + "\t\t"
success = "bot successfully commented in thread "
failure = "specified thread not found."

# iterates through 100 newest posts in subreddit
posts = 100
trigger = "Daily Discussion"
comment = "yeezy yeezy what's good"
found = False
for submission in subreddit.new(limit = posts):
	if submission.id not in visited:
		if re.search(trigger, submission.title, re.IGNORECASE):
			submission.reply(comment)
			found = True
			print(timestamp + success + submission.id)
			visited.append(submission.id)

if not found:
	print(timestamp + failure)

# logs triggered submissions as visited
with open("visited.txt", "w") as file:
	for post in visited:
		file.write(post + "\n")
