import asyncio

cmdlist = ["copypasta", "help"]  # All available commands go here

def run_coro(coro, client):
    fut = asyncio.run_coroutine_threadsafe(coro, client.loop)