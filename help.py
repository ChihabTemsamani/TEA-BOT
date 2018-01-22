from constants import *


def helpscript(command, client, message):
    client.send_message(message.channel, "I shitpost memes and copypastas")
    client.send_message(message.channel, "Availible commands:")
    commands_str = "`".join(cmdlist[0:]).join("`")
    client.send_message(message.channel, commands_str)
