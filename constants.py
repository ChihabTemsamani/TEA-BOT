import asyncio, discord

cmdlist = ["help","copypasta", "dankmeme","subreddit"]  # All available commands go here

loggingchannel = discord.Object(id=435092761268584450)

def run_coro(coro, client):
    fut = asyncio.run_coroutine_threadsafe(coro, client.loop)