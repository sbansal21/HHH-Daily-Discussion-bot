# HHH-Daily-Discussion-bot
A Reddit bot that automatically posts submissions to /r/hiphopheads Daily Discussion threads.

# Using the bot on *nix systems
1. Add "hhhbot.py" to some directory.
2. Give "hhhbot.py" permission to execute (`chmod u+x hhhbot.py`).
3. Create a new file "bot.py" and populate it:  
&emsp;`client_id = <provided by Reddit>`  
&emsp;`client_secret = <provided by Reddit>`  
&emsp;`username = <your Reddit username>`  
&emsp;`password = <your Reddit password>`  
4. Set up a cron job:  
&emsp;`$ crontab -e`  
&emsp;Within the crontab file, add `* * * * * cd <directory of bot files>; ./hhhbot`.