#!/usr/bin/python3

import os
import getpass
import sys

cmds = ("\nPOSSIBLE COMMANDS:\n"
	"'account'\n"
	"\tedits the account the bot runs on (i.e. username-password combo)\n"
	"\tUsage: ./edit.py account\n"
	"'subreddit'\n"
	"\tedits the subreddit the bot tracks and runs within\n"
	"\tUsage: ./edit.py subreddit\n"
	"'trigger'\n"
	"\tedits the keyword or phrase that triggers the bot\n"
	"\t(can be left blank to comment under every post in the subreddit)\n"
	"\tUsage: ./edit.py trigger\n"
	"'comment'\n"
	"\tedits the comment the bot posts when triggered by a thread\n"
	"\tUsage: ./edit.py comment\n")

setup = False

# first time setup
if not os.path.isfile("settings.py"):
	with open("settings.py", "w") as file:
		print("first time setup")
		file.write("client_id = '" + input("client_id: ") + "'\n")
		file.write("client_secret = '" + input("client_secret: ") + "'\n")
		file.write("username = '" + input("username: ") + "'\n")
		file.write("password = '" + getpass.getpass("password: ") + "'\n")
		file.write("subreddit = '" + input("subreddit: ") + "'\n")
		file.write("trigger = '" + input("trigger: ") + "'\n")
		file.write("comment = \"" + input("comment: ") + "\"\n")
		setup = True

import settings

with open("settings.py", "r") as file:
	data = file.readlines()

# edits account settings
def account():
	data[2] = property("username", input("username? "))
	data[3] = property("password", getpass.getpass("password? "))
	return "".join((data[2], data[3]))

# edits subreddit preference
def subreddit():
	data[4] = property("subreddit", input("subreddit? "))
	print(data[4])
	return data[4]

# edits trigger preference
def trigger():
	data[5] = property("trigger", input("trigger? "))
	return data[5]

def help():
	print(cmds)

# edits comment preference
def comment():
	data[6] = "comment = \"" + input("comment? ") + "\"\n"
	return data[6]

# internal def
def property(key, value):
	return str(key + " = '" + value + "'\n")

opts = {
	"account" : account,
	"subreddit" : subreddit,
	"trigger" : trigger,
	"comment" : comment
}

# runs appropriate defs if all args valid, else usage error
if len(sys.argv) > 1:
	invalid = False
	for arg in sys.argv[1:]:
		if arg not in opts:
			print("usage error: only valid args are 'account', 'subreddit', 'trigger', and 'comment'")
			invalid = True
	if not invalid:
		for arg in sys.argv[1:]:
			opts[arg]()
		with open("settings.py", "w") as file:
			file.writelines(data)
else:
	if not setup:
		help()
