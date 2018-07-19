import constants, time

def script(command, client, message):
    constants.run_coro(client.send_message(message.channel, "I shitpost memes and copypastas"), client)
    time.sleep(.25)
    constants.run_coro(client.send_message(message.channel, "Availible commands:"), client)
    time.sleep(.25)
    commands_str = "`" + ", ".join(constants.cmdlist[0:]) + "`"
    constants.run_coro(client.send_message(message.channel, commands_str), client)
    time.sleep(.25)
    constants.run_coro(client.send_message(message.channel, "You can end any command in `-p` to preserve your message."), client)
    time.sleep(.25)
    constants.run_coro(client.send_message(message.channel, "https://github.com/Shitscord/Shitscord"), client)
    print("help info requested")