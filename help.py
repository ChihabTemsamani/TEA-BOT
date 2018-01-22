from discord import *


def helpscript(command):
    client.send_message(message.channel, "I shitpost memes and copypastas")
    client.send_message(message.channel, "Availible commands:")
    commands_str = "`".join(commands[0:]).join("`")
    client.send_message(message.channel, commands_str)
