# Shitscord
An automatic shitposter for discord

# Use

NOTE: The Discord token is no longer stored in the variable "token", but rather "discord_token"

To use simply run the bot on a linux machine with python3 installed and the discord pip3 module, or a script hosting platform like Heroku.
Be sure to clone the `master` branch, and not `dev` as `dev` is the build we are currently working on, with new and possibly broken features.

If on your own machine, the bot token must be placed as the variable named token in a file named `discord_token.py`.
The variable should be a tuple. To utilize the reddit functions of Shitscord you will also need to create a `reddit_config.py`, and define the variables 
`client_id`, `client_secret`, and `user_agent` which you get from adding an app on Reddit dev.
If deploying into Heroku, you must set a config var with the key as "token" and the value as you Discord API key.

The bot will autodetect the discord_token file, or lack of. If the file cannot be found, it will refer to the OS variables, as set by Heroku

Current command sets include:
 - Copypasta
 - Subreddit
 - Dankmeme
# Modularity
Commands are formatted as modules now! Each command has its own python file which the script is imported as a function from.
Example: the copypasta script is stored in copypasta.py, containting the function copypastascript, and stated in the commands list as copypasta.
Following this naming scheme, commands can be essentially dynamically added to the bot. This allows less messy development and easier repairs and containment should a command bug out.

# Copypasta
 The copypasta files are stored in the copypasta_content.py file where the copypasta name in the cpname variable shares the same index value as the pasta itself in the cptext variable.
 If supplied with Reddit API keys the bot can automatically pull copypastas from Reddit, and the bot will automatically split the text by its spaces into <2000 character messages for Discord.

#Subreddit
 The subreddit command allows for a random image to be retrieved from a specific subreddit. This relies on the Reddit API Keys.
 
#Dankmeme
 This command will retrieve a random image from a random subreddit contained in a list of subreddits.