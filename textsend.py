import time
from constants import *


def textmessagesend(text, client, message):
    debug=1
    text_len=len(text) #length of pasta found to allow for proper message division
    if debug==1:
        run_coro(client.send_message(message.channel, ("Message Length: "+str(text_len))), client)
    if text_len < 2000:
        run_coro(client.send_message(message.channel, text), client)
    else:
        x=0
        z=2000
        
        while x<text_len: #loops until every character in the message has been sent
            text_output=""
            y=True
            while y:
                if z<text_len: #Go to 2000th character and find last space before that character
                    if text[z]==" ":
                        y=False
                    else:
                        z=z-1
                else: #End of message can be fit in one last message, ex loop two with 2500 total characters
                    y=False
            while x<z and x<text_len: #When last possible space is found, put all the characters into string to send
                text_output=text_output+text[x]
                x=x+1
            z=z+2000 #Skip forward another 2000 characters and repeat
            run_coro(client.send_message(message.channel, text_output), client) #Send message from variable text_output
            time.sleep(.5) #Sleep to prevent spam