from threading import Thread

def functioninit(command, client, message, commodule):
 
    impcom = ("import " + commodule)
    exec(impcom)
    cmdexec = commodule + ".script(command, client, message)"
    exec(cmdexec)

def procssschedule(command, client, message, commodule):

    background_thread = Thread(target=functioninit, args=(command, client, message, commodule))
    background_thread.start()
    