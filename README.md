# HHH-Daily-Discussion-bot
A Reddit bot that automatically posts submissions to /r/hiphopheads Daily Discussion threads.

# Installing python3 and modules
```
~$ sudo apt-get install python3
~$ sudo apt-get install python3-pip
~$ sudo pip3 install praw
```

# Using the bot on *nix systems
1. Add "hhhbot.py" to some directory.
2. Give "hhhbot.py" permission to execute:  
&emsp;`~$ chmod u+x hhhbot.py`
3. Create a new file "bot.py" and populate it:  
&emsp;`client_id = <provided by Reddit>`  
&emsp;`client_secret = <provided by Reddit>`  
&emsp;`username = <your Reddit username>`  
&emsp;`password = <your Reddit password>`  
4. Set up a cron job:  
&emsp;`~$ crontab -e`  
&emsp;Within the crontab file, add `* * * * * cd <directory of bot files>; ./hhhbot.py`.   
5. (Optional) To have the cron job provide updates on the terminal:  
        &emsp;Determine the pts file of the running terminal through the `tty` command.         
        &emsp;&emsp;`~$ tty`        
        &emsp;&emsp;`/dev/pts/0` or some variant        
		&emsp;Change `./hhhbot.py` to `./hhhbot.py > /dev/pts/0` (or whatever the output of `tty` was).        
6. (Optional) Log the cron job updates:  
        &emsp;Change `./hhhbot.py > /dev/pts/0` to `./hhhbot.py >> log`.        
        &emsp;To continue printing updates on the terminal, add the following command to the cron job: `tail -n1 log > /dev/pts/0`.  
        &emsp;The full cron job should then be `* * * * * cd <directory>; ./hhhbot.py >> log; tail -n1 log > /dev/pts/0`.  