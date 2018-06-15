import urllib.request, random, time, os, rif, constants

def script(command, client, message):
    if len(command) < 3:
        constants.run_coro(client.send_message(message.channel, "You must enter a media type [image] and a subreddit."), client)
        return
    
    if command[1].lower() == "image":
        srname=command[2]
        print("Getting random image from",srname)
        
        if "-s" in command:
            sloc=command.index("-s")
            if len(command)==sloc+1 or len(command)<sloc+1:
                sortby="hot" #Use Default
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        url=rif.find(srname, sortby, maxrange, attempts)        
        
        if url=="sr_invalid":
            print("Invalid Subreddit")
            constants.run_coro(client.send_message(message.channel, "That Subreddit does not exist."), client)
            return

        if url=="noimagefound":
            print("No Image Found")
            constants.run_coro(client.send_message(message.channel, "No image found in that Subreddit."), client)
            return
            
        else:
            url_type=url[-3:]
            print("Image Found")
            if url_type=="jpg":
                file_name="images/"+str(random.randint(1,1000))+".jpg"
            if url_type=="jpeg":
                file_name="images/"+str(random.randint(1,1000))+".jpeg"
            if url_type=="png":
                file_name="images/"+str(random.randint(1,1000))+".png"         
            print("Downloading image from: ", url)
            urllib.request.urlretrieve(url, file_name)
            open(file_name + ".lock","a").close()
            print("Image placed at: ",file_name," and locked")
            time.sleep(1)
            print("Sending Image")
            constants.run_coro(client.send_file(message.channel, file_name), client) # Send Image
            print("Sent Image")
            os.remove(file_name + ".lock")
            print(file_name, " unlocked.")

           