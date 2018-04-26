from constants import *
import praw, reddit_config, urllib.request, random, time, os

def script(command, client, message):
    subredditchoice=["me_irl","trippinthroughtime","youdontsurf","vsaucememes","trebuchetmemes","dankmemes","lossedits","labelmemes","meirl"]    
    subredditcount=len(subredditchoice)
    chosenreddit=random.randint(0,subredditcount-1)
    print("Choosing subreddit number", chosenreddit)
    srname=subredditchoice[int(chosenreddit)]    
    reddit = praw.Reddit(client_id=reddit_config.client_id, client_secret=reddit_config.client_secret,
                         user_agent=reddit_config.user_agent)
    print("Getting random image from", srname)    
    #Find the max amount of posts in a subreddit, or whatever reddit tops out at (usually 100) in order to prevent index errors
    #Max posts stored as postcount variable
    postcount = 0
    for post in reddit.subreddit(srname).top(limit = 100):
        postcount += 1
    print("Post range = ",postcount)   
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
    if url_type=="jpg":
        file_name="temp/"+str(random.randint(1,1000))+".jpg"
    if url_type=="jpeg":
        file_name="temp/"+str(random.randint(1,1000))+".jpeg"
    if url_type=="png":
        file_name="temp/"+str(random.randint(1,1000))+".png"           
    print("Downloading image from: ", url)
    urllib.request.urlretrieve(url, file_name)
    open(file_name + ".lock","a").close()
    print("Image placed at: ",file_name," and locked")
    time.sleep(1)
    print("Sending Image")
    run_coro(client.send_file(message.channel, file_name), client) # Send Image
    print("Sent Image")

    