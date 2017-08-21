#!/usr/bin/python3

import os
import getpass
import sys

from collections import OrderedDict

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
usage = "[USAGE] Only valid args are 'setup', 'account', 'subreddit', 'trigger', and 'comment'"
set = False
map=OrderedDict()

# first time setup
def setup():
	print("first time setup")
	with open("settings", "w") as file:
		file.write("client_id='" + input("client_id: ") + "'\n")
		file.write("client_secret='" + input("client_secret: ") + "'\n")
		file.write("username='" + input("username: ") + "'\n")
		file.write("password='" + getpass.getpass("password: ") + "'\n")
		file.write("subreddit='" + input("subreddit: ") + "'\n")
		file.write("trigger='" + input("trigger: ") + "'\n")
		file.write("comment='" + input("comment: ") + "'\n")
		set = True

# edits account settings
def account():
	map['username'] = input("username? ")
	map['password'] = getpass.getpass("password? ")
	return ":".join((map['username'], map['password']))

# edits subreddit preference
def subreddit():
	map['subreddit'] = input("subreddit? ")
	return map['subreddit']

# edits trigger preference
def trigger():
	map['trigger']=input("trigger? ")
	return map['trigger']

# edits comment preference
def comment():
	map['comment'] = input("comment? ")
	return map['comment']

def help():
	print(cmds)

if not os.path.isfile("settings"):
	setup()

with open("settings", "r") as file:
	data = file.readlines()

def prefs():
	for entry in data:
		key = entry[0:entry.index("=")]
		val = entry[entry.index("=")+2:entry.index("\n")-1]
		map[key]=val
	return map

opts = {
	"account" : account,
	"subreddit" : subreddit,
	"trigger" : trigger,
	"comment" : comment,
	"setup"	: setup
}

prefs()

# runs appropriate defs if all args valid, else usage error
if len(sys.argv) > 1:
	invalid = False
	for arg in sys.argv[1:]:
		if arg not in opts:
			print(usage)
			invalid = True
	if not invalid:
		for arg in sys.argv[1:]:
			opts[arg]()
		with open("settings", "w") as file:
			for entry in map:
				file.write(entry + "='" + map[entry] + "'\n")
else:
	if not set:
		help()
