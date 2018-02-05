import discord
from discord.ext import commands
from constants import *
import os

try:
    from discord_token import discord_token
    # Token stored in file called discord_token.py as var token.
    # This is a try loop so the program can run locally or when deployed
except ImportError:
    print("Token file not found. Using var from OS")
    discord_token = os.environ.get('discord_token')
    
#Read Reddit auth either locally or from global var
try:
    from reddit_config import client_id
    from reddit_config import client_secret
    from reddit_config import user_agent
    print(client_id)    
    reddit_client_id = client_id
    reddit_client_secret = client_secret
    reddit_user_agent = user_agent
    
    
    
except ImportError:
    print("Token file not found. Using var from OS")
    
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')
    user_agent = os.environ.get('user_agent')
    
    reddit_conf_file = open("reddit_config.py","w+")
    reddit_conf_file.write("client_id = " + client_id)
    reddit_conf_file.write("client_secret = " + client_secret)
    reddit_conf_file.write("user_agent = " + user_agent)
    reddit_conf_file.close()

Client = discord.Client()
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Bot is online and connected to Discord")  # When Bot Connects

# importing commands
x = 0
while x < len(cmdlist):
    filename = str(cmdlist[x])
    funcname = str(cmdlist[x]) + "script"
    importfunc = "from " + filename + " import " + funcname
    print(importfunc)
    exec(importfunc)
    x += 1


@client.event
async def on_message(message):
    if message.content.upper().startswith('!SHITSCORD'):
        print("I Have Been Summoned")
        command = message.content.split(" ")
        print("User States:", command)
        # checks if input is valid command with weird double if else and acts accordingly
        if len(command) > 1:
            if command[1].lower() in cmdlist:  # If command is correct (all command actions (most of bot) go here)
                cmdexec = command[1] + "script(command, client, message)"
                exec(cmdexec)
                print(cmdexec)
                if message.content.lower().endswith("-s"):
                    await client.delete_message(message)
            else:
                await client.send_message(message.channel, "Thats not a command")

        else:
            await client.send_message(message.channel, ":shit:")  # If no command is given


client.run(discord_token)
