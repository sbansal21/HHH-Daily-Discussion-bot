# reddit-bots
A couple useful, easily-configurable Reddit bots.

#### rbot
A general Reddit bot that automatically comments on posts that contain certain keywords.

#### hhhbot
A Reddit bot that automatically posts submissions to /r/hiphopheads Daily and Sunday General Discussion threads.

## Installing python3 and modules
```
~$ sudo apt-get install python3
~$ sudo apt-get install python3-pip
~$ sudo pip3 install praw
```

## Using the bot on *nix systems
1. Add "rbot.py" to some directory.
2. Give "rbot.py" permission to execute:  
&emsp;`~$ chmod u+x rbot.py`
3. Set up a cron job:  
&emsp;Give the autocron script permission to execute:  
&emsp;`~$ chmod u+x autocron.sh`  
&emsp;Run the autocron script:  
&emsp;`./autocron.sh [-l] [-o] <botname>`  
&emsp;`-l writes output to a log file`  
&emsp;`-o prints the output to the running terminal`  
&emsp;Botnames are simply the script names minus the extension (e.g. rbot, hhhbot).
4. To configure the bot, follow the first time setup to automatically populate these fields in the bot's settings:  
&emsp;`client_id = <provided by Reddit when you declare a bot under account prefs>`  
&emsp;`client_secret = <provided by Reddit when you declare a bot under account prefs>`  
&emsp;`username = <your Reddit username>`  
&emsp;`password = <your Reddit password>`  
&emsp;`subreddit = <the subreddit to point the bot to>`  
&emsp;`trigger = <the phrase that triggers the bot>`  
&emsp;`comment = <your comment under the appropriate post>`  

## TODO
- follower
- archive diver
