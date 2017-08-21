#!/usr/bin/env bash

crontab -l > autocron
echo "* * * * * cd `pwd`; ./rbot.py >> log; tail -n1 log > `tty`" >> autocron
crontab autocron
rm autocron
