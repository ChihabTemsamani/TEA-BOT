import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from copypasta_content import * #yes this is bad
from copypasta import copypastascript

try:
    from discord_token import token #Token stored in file called discord_token.py as var token. This is a try loop so the program can run locally or when deployed
except: 
    print("Token file not found. Trying to import OS")
    import os
    token=os.environ.get('token')
#Client loaded and connected
Client=discord.Client()
client=commands.Bot(command_prefix = "!") 


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #When Bot Connects

commands = ["help","copypasta"] #All available commands go here
cmdlist = (" ".join(commands[0:]))#Make List of available commands

@client.event
async def on_message(message):
    if message.content.upper().startswith('!SHITSCORD'):
        print("I Have Been Summoned")
        command = message.content.split(" ")
        print("User States:", command)

        #checks if input is valid command with weird double if else and acts accordingly
        if len(command) > 1:
            if command[1].lower() in commands: #If command is correct (all command actions (most of bot) go here)
                if command[1].lower()=="copypasta":
                    cpfunction(command)
            else:
                await client.send_message(message.channel, ":shit:")# If command is incorrect
        else:
            await client.send_message(message.channel, ":shit:") #If no command is given

client.run(token)
