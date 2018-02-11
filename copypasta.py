from copypasta_content import *
from constants import *
import praw, reddit_config, time

def copypastascript(command, client, message):
    if len(command) < 3:
        run_coro(client.send_message(message.channel, "You must input a copypasta or `list`"), client)
        return

    if command[2].lower() == "list":
        cpnamesstr = (" ".join(cpnames[0:]))  # Get list of CP names
        run_coro(client.send_message(message.channel, cpnamesstr), client)  # Send List
        run_coro(client.send_message(message.channel, "You can also try `random` to try your luck."), client)

    elif command[2].lower() == "random":
        char_length_2000_debug=False # Requires pasta to be >2000 if true, for testing purposes
        print("Trying to get a random CP from reddit. This could take a moment.")
        reddit = praw.Reddit(client_id=reddit_config.client_id, client_secret=reddit_config.client_secret,
                             user_agent=reddit_config.user_agent)
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
            ranpasta_len=len(random_pasta) #length of pasta found to allow for proper message division
            print("Copypasta Length in Characters: ", ranpasta_len)           
        print("Collected random CP")
        if ranpasta_len < 2000:
            run_coro(client.send_message(message.channel, random_pasta), client)
        else:
            x=0
            z=2000
            
            while x<ranpasta_len: #loops until every character in the message has been sent
                ranpasta_output=""
                print("ranpasta_output Var reset")
                y=True
                while y:
                    if z<ranpasta_len: #Go to 2000th character and find last space before that character
                        if random_pasta[z]==" ":
                            y=False
                        else:
                            z=z-1
                    else: #End of message can be fit in one last message, ex loop two with 2500 total characters
                        y=False
                while x<z and x<ranpasta_len: #When last possible space is found, put all the characters into string to send
                    ranpasta_output=ranpasta_output+random_pasta[x]
                    x=x+1
                z=z+2000 #Skip forward another 2000 characters and repeat
                print()
                print("This message:", ranpasta_output)
                run_coro(client.send_message(message.channel, ranpasta_output), client) #Send message from variable ranpasta_output
                time.sleep(.5) #Sleep to prevent spam    
            
    elif command[2].lower() in cpnames:
        cprequest = command[2].lower()  # All lowercase name
        cplocate = cpnames.index(cprequest)  # Get index number of CP
        cpserve = cplist[cplocate]  # Get the CP
        run_coro(client.send_message(message.channel, cpserve), client)  # Send CP
