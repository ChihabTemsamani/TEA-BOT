from constants import *
from importlib import reload
import textsend
import praw, reddit_config, random, requests
import cpindex




def script(command, client, message):
    if len(command) < 3:
        run_coro(client.send_message(message.channel, "You must input a copypasta, `list`, or random"), client)
        return


    #Copypasta List
    if command[2].lower() == "list":
        cpnames = reload(cpindex)
        cpnamesstr = (" ".join(cpnames.cplibrary[0:]))  # Get list of CP names
        textsend.send(cpnamesstr, client, message)  # Send List
        run_coro(client.send_message(message.channel, "You can also try `random` to try your luck."), client)
        return


    #Copypasta random
    elif command[2].lower() == "random":
        print("Trying to get a random CP from reddit. This could take a moment.")
        reddit = praw.Reddit(client_id=reddit_config.client_id, client_secret=reddit_config.client_secret,
                             user_agent=reddit_config.user_agent)
        
        sr = reddit.subreddit("copypasta")
        pasta=sr.random().selftext #Pasta acquired
        
        
    #Valid copypasta name, gets url, downloads file, reads file, sends text
    elif command[2].lower() in cpindex.cplibrary:
        cpname = command[2].lower()  # All lowercase name
        cpurl=("http://raw.githubusercontent.com/Shitscord/cp-lib/master/"+cpname+".txt")
        durl=requests.get(cpurl)
        randint=random.randint(1,1000)
        lname=("temp/"+str(randint)+".txt")
        with open(lname, "wb") as w:
            w.write(durl.content)
            
        lfile=open(lname,"r",encoding="utf8")
        
        pasta= lfile.read()
        
    textsend.send(pasta, client, message)