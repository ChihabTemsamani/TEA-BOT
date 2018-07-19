import urllib.request, random, time, os, rif, constants

def script(command, client, message):
    sortbymodes=["hot","new","controversial","top","rising"]
    
    
    if len(command) < 3:
        constants.run_coro(client.send_message(message.channel, "You must enter a media type [image] and a subreddit."), client)
        return
    
    if command[1].lower() == "image":
        srname=command[2]
        print("Getting random image from",srname)
                
        #Sortby
        if "-s" in str(command).lower():
            sloc=command.index("-s")
            if len(command)>sloc+1 or len(command)==sloc+1 and str(command[sloc+1]).lower() in sortbymodes:
                sortby=str(command[sloc+1]).lower()
            else:
                sortby="hot"
        else:
            sortby="hot"
        
        #Range
        if "-r" in str(command).lower():
            rloc=command.index("-r")
            if len(command)>rloc+1 or len(command)==rloc+1 and int(command[rloc+1])>0 and int(command[rloc+1])<1000:
                maxrange=int(command[rloc+1])
            else:
                maxrange=100
        else:
            maxrange=100    
    
        #Attempts
        if "-a" in str(command).lower():
            aloc=command.index("-a")
            if len(command)>aloc+1 or len(command)==aloc+1 and int(command[aloc+1])>0 and int(command[aloc+1])<30:
                attempts=int(command[aloc+1])
            else:
                attempts=5
        else:
            attempts=5
        
        #Spam
        if "-m" in str(command).lower():
            spamloc=command.index("-m")
            if len(command)>spamloc+1 or len(command)==spamloc+1 and int(command[spamloc+1])>0 and int(command[spamloc+1])<10:
                print(command[spamloc+1])
                spam=int(command[spamloc+1])
            else:
                spam=1
        else:
            spam=1
        
        print("Spam:", spam)
        x=0
        while x<spam:
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
                time.sleep(2)
                print("Sending Image")
                constants.run_coro(client.send_file(message.channel, file_name), client) # Send Image
                print("Sent Image")
                os.remove(file_name + ".lock")
                print(file_name, " unlocked.")
            
            x=x+1
           