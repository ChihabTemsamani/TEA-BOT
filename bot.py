from discord.ext import commands
import constants, procopen
import discord, os, time

try:
    from discord_token import token
except ImportError:
    print("Token file not found. Using var from OS")
    token = os.environ.get('discord_token')
    

try:
    from reddit_config import client_id
    from reddit_config import client_secret
    from reddit_config import user_agent 
    reddit_client_id = client_id
    reddit_client_secret = client_secret
    reddit_user_agent = user_agent  
except ImportError:    
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')
    user_agent = os.environ.get('user_agent')
    reddit_conf_file = open("reddit_config.py","w+")
    reddit_conf_file.write("client_id = '" + client_id +"'\n")
    reddit_conf_file.write("client_secret = '" + client_secret +"'\n")
    reddit_conf_file.write("user_agent = '" + user_agent +"'\n")
    reddit_conf_file.close()
    time.sleep(3)
    
if not os.path.exists("images"):
    os.makedirs("images")    

Client = discord.Client()
client = commands.Bot(command_prefix="!")
loggingchannel = discord.Object(id=435092761268584450)

@client.event
async def on_ready():
    print("Bot is online and connected to Discord")  # When Bot Connects
    await client.send_message(loggingchannel, "Bot Online")

@client.event
async def on_message(message):
    if message.content.upper().startswith('!SHITSCORD'):
        print("I Have Been Summoned")
        command = message.content.split(" ")
        print("User States:", command)
        # checks if input is valid command with weird double if else and acts accordingly
        if len(command) > 1:
            if command[1].lower() in constants.cmdlist:  # If command is correct (all command actions (most of bot) go here)
                procopen.procssschedule(command, client, message)
                await client.delete_message(message)
            else:
                await client.send_message(message.channel, "Thats not a command")
        else:
            await client.send_message(message.channel, ":poop:")  # If no command is given
            await client.send_message(message.channel, "Type !shitscord 'help' or 'about' for more information.")

client.run(token)