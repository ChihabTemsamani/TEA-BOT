import asyncio

cmdlist = ["help","about","copypasta", "dankmeme", "cache","subreddit"]  # All available commands go here
services = ["clean"]

versionnumber="1.29"

def run_coro(coro, client):
    fut = asyncio.run_coroutine_threadsafe(coro, client.loop)