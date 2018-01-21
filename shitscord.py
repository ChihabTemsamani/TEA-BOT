import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from discord_token import token #Token stored in file called discord_token.py as var token
from copypasta import * #yes this is bad

#Client loaded and connected
Client = discord.Client()
client = commands.Bot(command_prefix = "?") 


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #When Bot Connects

commands = ["copypasta"] #All available commands go here

@client.event
async def on_message(message):
    if message.content.upper().startswith('!SHITSCORD'):
        print("I Have Been Summoned")
        command = message.content.split(" ")
        print("User States:", command)

        #checks if input is valid command with weird double if else and acts accordingly
        if len(command) > 1:
            if command[1] in commands: #If command is correct (all command actions (most of bot) go here)
                if command[1].lower()=="copypasta":
                    print("Copypasta Requested")
                    if command[2].lower() in cpnames:
                        cprequest=command[2].lower() #All lowercase name
                        cplocate=cpnames.index(cprequest) #Get index number of CP
                        cpserve=cplist[cplocate] #Get the CP
                        await client.send_message(message.channel, cpserve) #Send CP
                        
            else:
                await client.send_message(message.channel, ":shit:")# If command is incorrect
        else:
            await client.send_message(message.channel, ":shit:") #If no command is given

client.run(token)
