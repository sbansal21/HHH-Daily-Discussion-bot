#!/usr/bin/python3

import datetime

import praw
import re
import os
import sys

sys.stdout = open(os.devnull, 'w')
from edit import setup, prefs
sys.stdout = sys.__stdout__

from collections import OrderedDict

# ensures settings properly initialized
if not os.path.isfile("settings"):
	edit.setup()

map = prefs()

# tracks which posts have already been visited
if not os.path.isfile("visited.txt"):
	visited = []
else:
	with open("visited.txt", "r") as file:
		visited = file.read().split("\n")
		visited = list(filter(None, visited))

# creates PRAW Reddit instance
bot = praw.Reddit(user_agent = 'HHH PyBot',
                  client_id = map['client_id'],
                  client_secret = map['client_secret'],
                  username = map['username'],
                  password = map['password'])
# points bot to a specific subreddit
subreddit = bot.subreddit('hiphopheads')

timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') + "\t\t"
success = "bot successfully commented in thread "
failure = "specified thread not found."

# iterates through 100 newest posts in subreddit
trigger = "Daily Discussion"
comment = "yeezy yeezy what's good"
found = False
for submission in subreddit.new(limit = 100):
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
