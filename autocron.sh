#!/usr/bin/env bash

# parse opts
log=false	# writes stdout to a log
out=false	# redirects stdout to the running terminal
while getopts ":lo" opt; do
	case $opt in
		l)	log=true
			;;
		o)	out=true
			;;
		\?)	echo "Usage: ./autocron.sh [-l] [-o] <bot>"
			exit 1
			;;
		:)	echo "Specify which bots to set cron jobs for."
			exit 1
			;;
	esac
done

# adds cron jobs for each positional parameter
crontab -l > autocron
while [ $# -gt 0 ]
do
	if [[ $1 == *"-"* ]]; then
		shift
		continue
	fi

	if [ "$log" = true ] && [ "$out" = true ]; then
		echo "* * * * * cd `pwd`; ./${1}.py >> ${1}.log; tail -n1 log > `tty`" >> autocron
	elif [ "$log" = true ] && [ "$out" = false ]; then
		echo "* * * * * cd `pwd`; ./${1}.py >> ${1}.log" >> autocron
	elif [ "$log" = false ] && [ "$out" = true ]; then
		echo "* * * * * cd `pwd`; ./${1}.py > `tty`" >> autocron
	elif [ "$log" = false ] && [ "$out" = false ]; then
		echo "* * * * * cd `pwd`; ./${1}.py" >> autocron
	fi
	echo "created cron job for $1"
	shift
done
crontab autocron
rm autocron
