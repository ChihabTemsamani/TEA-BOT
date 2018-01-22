def copypastascript(command):
    if command[2].lower() == "list":
        cpserve=(" ".join(cpnames[0:])) #Get list of CP names
        client.send_message(message.channel, cpserve) #Send List

    if command[2].lower() in cpnames:
        cprequest=command[2].lower() #All lowercase name
        cplocate=cpnames.index(cprequest) #Get index number of CP
        cpserve=cplist[cplocate] #Get the CP
        client.send_message(message.channel, cpserve) #Send CP                     