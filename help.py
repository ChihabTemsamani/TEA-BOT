import constants

def script(command, client, message):
    constants.run_coro(client.send_message(message.channel, "I shitpost memes and copypastas"), client)
    constants.run_coro(client.send_message(message.channel, "Availible commands:"), client)
    commands_str = "`" + ", ".join(constants.cmdlist[0:]) + "`"
    constants.run_coro(client.send_message(message.channel, commands_str), client)
    constants.run_coro(client.send_message(message.channel, "You can end any command in `-p` to preserve your message."), client)
    constants.run_coro(client.send_message(message.channel, "https://github.com/Shitscord/Shitscord"), client)
    print("help info requested")