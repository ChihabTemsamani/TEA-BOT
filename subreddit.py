from constants import *
import praw, reddit_config, urllib.request, random, time, os

def script(command, client, message):
    if len(command) < 4:
        run_coro(client.send_message(message.channel, "You must enter a media type [image] and a subreddit."), client)
        return
    
    if command[2].lower() == "image":
        srname=command[3]
        print("Getting random image from",srname)
        reddit = praw.Reddit(client_id=reddit_config.client_id, client_secret=reddit_config.client_secret,
                             user_agent=reddit_config.user_agent)
    
    #Check to make sure subreddit exists
    try:
        reddit.subreddits.search_by_name(srname, exact=True)
    except:
        print("Invalid Subreddit")
        run_coro(client.send_message(message.channel, "Invalid Subreddit"), client)
    else: 
        
        #Find the max amount of posts in a subreddit, or whatever reddit tops out at
        #Max posts stored as postcount variable
        postcount = 0
        for post in reddit.subreddit(srname).hot(limit = 100):
            postcount += 1
        print("Post range = ",postcount)
        
        w=0
        x=True
        accepted_type= ["jpg","peg","png"] #last three characters of image file extensions
        while x:
            sub = reddit.subreddit(srname)
            srposts = [post for post in sub.hot(limit=postcount)]
            randpostnum = random.randint(0, postcount-1)
            randpost = srposts[randpostnum]
            url = str(randpost.url)
            url_type=url[-3:]
            print(url)
            print(url_type)
            if url_type in accepted_type:
                x=False
                print("URL is to an image file")
            w += 1
            if w==5:
                x=False
                run_coro(client.send_message(message.channel, "An image could not be found in this subreddit."), client)
                foundimage=0
            else:
                foundimage=1
                
                
        if foundimage==1:
            print("Image Found")
            if url_type=="jpg":
                file_name="images/"+str(random.randint(1,1000))+".jpg"
            if url_type=="jpeg":
                file_name="images/"+str(random.randint(1,1000))+".jpeg"
            if url_type=="png":
                file_name="images/"+str(random.randint(1,1000))+".png"
            if url_type=="gif":
                file_name="images/"+str(random.randint(1,1000))+".gif"            
            print("Downloading image from: ", url)
            urllib.request.urlretrieve(url, file_name)
            open(file_name + ".lock","a").close()
            print("Image placed at: ",file_name," and locked")
            time.sleep(1)
            print("Sending Image")
            run_coro(client.send_file(message.channel, file_name), client) # Send Image
            print("Sent Image")
            os.remove(file_name + ".lock")
            print(file_name, " unlocked.")

           