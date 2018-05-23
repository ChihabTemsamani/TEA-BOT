from threading import Thread

def functioninit(command, client, message):
 
    impcom = ("import " + str(command[1]))
    exec(impcom)
    cmdexec = command[1] + ".script(command, client, message)"
    exec(cmdexec)

def procssschedule(command, client, message):

    background_thread = Thread(target=functioninit, args=(command, client, message))
    background_thread.start()
    