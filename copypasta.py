from copypasta_content import *
from constants import *
import reddit_config
import praw


def copypastascript(command, client, message):
    if len(command) < 3:
        run_coro(client.send_message(message.channel, "You must input a copypasta or `list`"), client)
        return

    if command[2].lower() == "list":
        cpnamesstr = (" ".join(cpnames[0:]))  # Get list of CP names
        run_coro(client.send_message(message.channel, cpnamesstr), client)  # Send List
        run_coro(client.send_message(message.channel, "You can also try `random` to try your luck."), client)

    elif command[2].lower() == "random":
        print("Trying to get a random CP from reddit. This could take a moment.")
        reddit = praw.Reddit(client_id=reddit_config.client_id, client_secret=reddit_config.client_secret,
                             user_agent=reddit_config.user_agent)
        sr = reddit.subreddit("copypasta")
        print("Collected random CP")
        run_coro(client.send_message(message.channel, sr.random().selftext), client)

    elif command[2].lower() in cpnames:
        cprequest = command[2].lower()  # All lowercase name
        cplocate = cpnames.index(cprequest)  # Get index number of CP
        cpserve = cplist[cplocate]  # Get the CP
        run_coro(client.send_message(message.channel, cpserve), client)  # Send CP
