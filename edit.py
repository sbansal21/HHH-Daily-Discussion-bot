#!/usr/bin/python3

import os
import getpass
import sys

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
