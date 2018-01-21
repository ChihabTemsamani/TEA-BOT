import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from discord_token import token #Token stored in file called discord_token.py as var token 

#Client loaded and connected
Client = discord.Client()
client = commands.Bot(command_prefix = "?") 


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #When Bot Connects

@client.event
async def on_message(message):
    if message.content.upper().startswith('!SHITSCORD'):
        print("I Have Been Summoned")
        print("User States:", message.content)
        await client.send_message(message.channel, ":shit:")

client.run(token)
