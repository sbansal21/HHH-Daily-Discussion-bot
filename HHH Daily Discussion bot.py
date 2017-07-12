#!/usr/bin/python

import bot  # contains private bot info

import praw

# creates praw Reddit instance
bot = praw.Reddit(user_agent = 'HHH PyBot v1',
                  client_id = bot.client_id,
                  client_secret = bot.client_secret,
                  username = bot.username,
                  password = bot.password)