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
    reddit_conf_file.write("client_id = '" + str(client_id) +"'\n")
    reddit_conf_file.write("client_secret = '" + str(client_secret) +"'\n")
    reddit_conf_file.write("user_agent = '" + str(user_agent) +"'\n")
    reddit_conf_file.close()
    time.sleep(3)
    
if not os.path.exists("images"):
    os.makedirs("images")    

Client = discord.Client()
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Bot is online and connected to Discord")  # When Bot Connects
    await client.send_message(constants.loggingchannel, "Bot Online")

@client.event
async def on_message(message):
    if message.content.upper().startswith('!'):
        command = message.content.split(" ")
        print("User States:", command)
        
        commodule=''.join(command[0].split('!', 1)).lower()
        
        print("Calling: ", commodule)
        if commodule in constants.cmdlist:
            procopen.procssschedule(command, client, message, commodule)
            await client.delete_message(message)
client.run(token)