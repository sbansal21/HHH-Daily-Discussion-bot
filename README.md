# reddit-bots
A couple useful, easily-configurable Reddit bots.

#### rbot
A general Reddit bot that automatically comments on posts that contain certain keywords.

#### hhhbot
A Reddit bot that automatically posts submissions to /r/hiphopheads Daily and Sunday General Discussion threads.

#### editor
A repo-specific editor to manage bot settings.

## Installing python3 and necessary packages
```
~$ sudo apt-get install python3
~$ sudo apt-get install python3-setuptools
~$ sudo easy_install3 pip
~$ sudo pip3 install praw
```

## Using the bot on \*nix systems
1. Download the repository and navigate to that directory.
2. Set up the bots' basic client settings:
```
~$ python3 editor.py
```
3. Set up a cron job by giving the `autocron.sh` script permission to execute and then running it:  
```
~$ chmod u+x autocron.sh
~$ ./autocron.sh [-l] [-o] <botname> <botname>`
	-l writes output to a log file`
	-o prints the output to the running terminal`
	Botnames are just the script names minus the extension (e.g. rbot, hhhbot).
```
4. The first time the bots run, they will need to be configured with the following fields:  
&emsp;__General__  
&emsp;`client_id`&emsp;&emsp;provided by Reddit when you declare a bot under account preferences  
&emsp;`secret`&emsp;&emsp;&emsp;&thinsp;&thinsp;provided by Reddit when you declare a bot under account preferences  
&emsp;`username`&emsp;&emsp;&ensp;your Reddit username  
&emsp;`password`&emsp;&emsp;&ensp;your Reddit password  
&emsp;__Commenter__   
&emsp;`subreddit`&emsp;&emsp;the subreddit to point the bot to  
&emsp;`trigger`&emsp;&emsp;&ensp;&thinsp;&thinsp;the phrase that triggers the bot  
&emsp;`comment`&emsp;&emsp;&ensp;&thinsp;&thinsp;your comment under the appropriate post  

## TODO
- prerequisite scripts
- better Windows support (incl. automated task scheduling), although the bots themselves are completely cross-platform <!-- schtasks /tn /? -->
- follower
- archive diver
