from constants import *


def helpscript(command, client, message):
    run_coro(client.send_message(message.channel, "I shitpost memes and copypastas"), client)
    run_coro(client.send_message(message.channel, "Availible commands:"), client)
    commands_str = "`".join(cmdlist[0:]).join("`")
    run_coro(client.send_message(message.channel, commands_str), client)
