from constants import *

def script(command, client, message):
    run_coro(client.send_message(message.channel, "I shitpost memes and copypastas"), client)
    run_coro(client.send_message(message.channel, "Version "+str(versionnumber)), client)
    run_coro(client.send_message(message.channel, "https://github.com/Shitscord/Shitscord"), client)
    print("about info requested")