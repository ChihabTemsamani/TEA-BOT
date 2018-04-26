from constants import *
from importlib import reload
from textsend import textmessagesend
import praw, reddit_config, time
import cpindex



def script(command, client, message):
    if len(command) < 3:
        run_coro(client.send_message(message.channel, "You must input a copypasta, `list`, or random"), client)
        return


    #Copypasta List
    if command[2].lower() == "list":
        cpnames = reload(cpindex)
        cpnamesstr = (" ".join(cpnames.cplibrary[0:]))  # Get list of CP names
        textmessagesend(cpnamesstr, client, message)  # Send List
        run_coro(client.send_message(message.channel, "You can also try `random` to try your luck."), client)


    #Copypasta random
    elif command[2].lower() == "random":
        print("Trying to get a random CP from reddit. This could take a moment.")
        reddit = praw.Reddit(client_id=reddit_config.client_id, client_secret=reddit_config.client_secret,
                             user_agent=reddit_config.user_agent)



    char_length_2000_debug=False
    if char_length_2000_debug==True:
        g=True
        ranpasta_len=0
        while g:
            sr = reddit.subreddit("copypasta")
            random_pasta=sr.random().selftext #Pasta acquired
            ranpasta_len=len(random_pasta) #length of pasta found to allow for proper message division
            print("Copypasta Length in Characters: ", ranpasta_len)
            if ranpasta_len>2000:
                g=False
    else:
        sr = reddit.subreddit("copypasta")
        random_pasta=sr.random().selftext #Pasta acquired
    textmessagesend(random_pasta, client, message)
        
'''
    elif command[2].lower() in cpnames:
        cprequest = command[2].lower()  # All lowercase name
        cplocate = cpnames.index(cprequest)  # Get index number of CP
        cpserve = cplist[cplocate]  # Get the CP
        run_coro(client.send_message(message.channel, cpserve), client)  # Send CP
'''