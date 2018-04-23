import asyncio

cmdlist = ["help","about","copypasta", "dankmeme", "cache","subreddit"]  # All available commands go here

versionnumber="1.38"


def run_coro(coro, client):
    fut = asyncio.run_coroutine_threadsafe(coro, client.loop)