import asyncio

cmdlist = ["copypasta", "help", "me_irl", "cache"]  # All available commands go here
services = ["clean"]

def run_coro(coro, client):
    fut = asyncio.run_coroutine_threadsafe(coro, client.loop)