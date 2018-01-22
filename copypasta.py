from copypasta_content import *
from constants import *


def copypastascript(command, client, message):
    if len(command) < 3:
        run_coro(client.send_message(message.channel, "You must input a copypasta or `list`"), client)
        return

    if command[2].lower() == "list":
        cpnamesstr = (" ".join(cpnames[0:]))  # Get list of CP names
        run_coro(client.send_message(message.channel, cpnamesstr), client)  # Send List

    elif command[2].lower() in cpnames:
        cprequest = command[2].lower()  # All lowercase name
        cplocate = cpnames.index(cprequest)  # Get index number of CP
        cpserve = cplist[cplocate]  # Get the CP
        run_coro(client.send_message(message.channel, cpserve), client)  # Send CP

    if len(command) > 3 and command[3].lower() == "-s":
        pass
        #  run_coro(client.delete_message(message), client)  # this broke
