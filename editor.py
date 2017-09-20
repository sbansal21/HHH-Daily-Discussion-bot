#!/usr/bin/python3

import os
import praw
import prawcore
from getpass import getpass
import sys
import configparser

help = ("\nPOSSIBLE COMMANDS:",
	"'account'",
	"\tedits the account the bot runs on (i.e. username-password combo)",
	"\tUsage: python3 editor.py account",
	"'subreddit'",
	"\tedits the subreddit the bot tracks and runs within",
	"\tUsage: python3 editor.py subreddit",
	"'trigger'",
	"\tedits the keyword or phrase that triggers the bot",
	"\t(can be left blank to comment under every post in the subreddit)",
	"\tUsage: python3 editor.py trigger",
	"'comment'",
	"\tedits the comment the bot posts when triggered by a thread",
	"\tUsage: python3 editor.py comment\n")
help = "\n".join(help)
usage = "[USAGE] Only valid args are 'setup', 'account', 'subreddit', 'trigger', and 'comment'"
settings = 'settings.ini'

config = configparser.ConfigParser()

# sets up the initial client settings
def setupClient():
	print("\nclient setup:")
	config.add_section('client')
	config.set('client', 'client_id', input("client_id? "))
	config.set('client', 'secret', input("secret? "))
	config.set('client', 'username', input("username? "))
	config.set('client', 'password', getpass("password? "))
	verifyClient()
	savePrefs()

# sets up the necessary options for the 'commenter' module
def setupCommenter():
	print("\ncommenter setup:")
	config.add_section('commenter')
	config.set('commenter', 'subreddit', input("subreddit? "))
	config.set('commenter', 'trigger', input("trigger? "))
	config.set('commenter', 'comment', input("comment? "))
	savePrefs()

# verifies the client credentials and resets the client if necessary
def verifyClient():
	bot = praw.Reddit(user_agent = 'pingbot',
	                  client_id = config.get('client', 'client_id'),
	                  client_secret = config.get('client', 'secret'),
	                  username = config.get('client', 'username'),
	                  password = config.get('client', 'password'))
	try:
		for submission in bot.subreddit('redditdev').new(limit = 1):
			pass
	except prawcore.exceptions.ResponseException:
		print("[ERROR] invalid client configuration")
		config.remove_section('client')
		setupClient()

# ensures that the commenter settings are set up
def verifyCommenter():
	if not config.has_section('commenter'):
		setupCommenter()

# edits account settings
def account():
	config.set('client', 'username', input("username? "))
	config.set('client', 'password', getpass("password? "))

# edits subreddit preference
def subreddit():
	config.set('commenter', 'subreddit', input("subreddit? "))

# edits trigger preference
def trigger():
	config.set('commenter', 'trigger', input("trigger? "))

# edits comment preference
def comment():
	config.set('commenter', 'comment', input("comment? "))

# prints help page
def printHelp():
	print(help)

# writes file with new configuration settings
def savePrefs():
	with open(settings, 'w') as file:
		config.write(file)

# loads current configuration settings from file
def loadPrefs():
	config.read(settings)
	return config

# main method
def main():

	if not os.path.isfile(settings):
		setupClient()
		verifyClient()
		savePrefs()
		if len(sys.argv) <= 1:
			return

	with open(settings, 'r') as file:
		loadPrefs()

	botreqs = {
		'subreddit' : verifyCommenter,
		'trigger' : verifyCommenter,
		'comment' : verifyCommenter
	}

	commands = {
		'account' : account,
		'subreddit' : subreddit,
		'trigger' : trigger,
		'comment' : comment
	}

	# runs appropriate defs if all args valid, else usage error
	if len(sys.argv) > 1:
		invalid = []
		for arg in sys.argv[1:]:
			if arg not in commands:
				invalid.append(arg)
		if invalid:
			print("[ERROR] invalid commands: " + " ".join(invalid))
			print(usage)
		else:
			for arg in sys.argv[1:]:
				botreqs[arg]()
				commands[arg]()
			savePrefs()
	else:
		printHelp()

# main script
if __name__ == '__main__':
	main()