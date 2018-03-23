import os, threading
from constants import run_coro

def cachescript(command, client, message):
    if len(command) < 3:
        run_coro(client.send_message(message.channel, "You must input a subcommand"), client)
        return

    if command[2].lower == "clear":
        for item in os.listdir("images"):
            if not item.endswith(".lock") and not os._exists(item + ".lock"):
                os.remove(item)
        run_coro(client.send_message(message.channel, "Cache cleared"), client)