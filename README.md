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
&emsp;`~$ crontab -e`  
&emsp;Within the crontab file, add `* * * * * cd <directory of bot files>; ./rbot.py`.   
4. (Optional) To have the cron job provide updates on the terminal:  
        &emsp;Determine the pts file of the running terminal through the `tty` command.         
        &emsp;&emsp;`~$ tty`        
        &emsp;&emsp;`/dev/pts/0` or some variant        
		&emsp;Change `./rbot.py` to `./rbot.py > /dev/pts/0` (or whatever the output of `tty` was).        
5. (Optional) Log the cron job updates:  
        &emsp;Change `./rbot.py > /dev/pts/0` to `./rbot.py >> log`.        
        &emsp;To continue printing updates on the terminal, add the following command to the cron job: `tail -n1 log > /dev/pts/0`.  
        &emsp;The full cron job should then be `* * * * * cd <directory>; ./rbot.py >> log; tail -n1 log > /dev/pts/0`.  
6. To configure the bot, follow the first time setup to automatically populate these fields in the bot's settings:  
&emsp;`client_id = <provided by Reddit when you declare a bot under account prefs>`  
&emsp;`client_secret = <provided by Reddit when you declare a bot under account prefs>`  
&emsp;`username = <your Reddit username>`  
&emsp;`password = <your Reddit password>`  
&emsp;`subreddit = <the subreddit to point the bot to>`  
&emsp;`trigger = <the phrase that triggers the bot>`  
&emsp;`comment = <your comment under the appropriate post>`  

## TODO
- crontab script
- follower
- archive diver