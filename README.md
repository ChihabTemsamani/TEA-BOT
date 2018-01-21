# Shitscord
An automatic shitposter for discord

# Use
To use simply run the bot on a linux machine with python3 installed and the discord pip3 module, or a script hosting platform like Heroku.

If on your own machine, the bot token must be placed as the variable named token in a file named discord_token.py.
If deploying into Heroku, you must set a config var with the key as "token" and the value as you Discord API key.

The bot will autodetect the discord_token file, or lack of. If the file cannot be found, it will refer to the OS variables, as set by Heroku

Current command sets include:
 - Copypasta
 
# Copypasta
 The copypasta files are stored in the copypasta.py file where the copypasta name in the cpname variable shares the same index value as the pasta itself in the cptext variable.