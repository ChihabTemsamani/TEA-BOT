from copypasta_content import *


def copypastascript(command, client, message):
    if len(command) < 3:
        client.send_message(message.channel, "You must input a copypasta or `list`")
        return

    if command[2].lower() == "list":
        cpserve = (" ".join(cpnames[0:]))  # Get list of CP names
        client.send_message(message.channel, cpserve)  # Send List

    elif command[2].lower() in cpnames:
        cprequest = command[2].lower()  # All lowercase name
        cplocate = cpnames.index(cprequest)  # Get index number of CP
        cpserve = cplist[cplocate]  # Get the CP
        client.send_message(message.channel, cpserve)  # Send CP

    if command[3].lower() == "-s":
        cprequest = command[2].lower()  # All lowercase name
        cplocate = cpnames.index(cprequest)  # Get index number of CP
        cpserve = cplist[cplocate]  # Get the CP
        client.send_message(message.channel, cpserve)  # Send CP
        client.delete_message(message)  # remove command
