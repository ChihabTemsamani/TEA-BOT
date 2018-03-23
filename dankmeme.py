from constants import *
import praw, reddit_config, urllib.request, random, time, os

def dankmemescript(command, client, message):
    subredditchoice=["me_irl","trippinthroughtime","youdontsurf","WatchPeopleDieInside","vsaucememes","trebuchetmemes","SpaceXMasterrace","ProgrammerHumor","lossedits","labelmemes","masterhacker"]
    subredditcount=len(subredditchoice)
    chosenreddit=random.randint(0,subredditcount-1)
    print("Choosing subreddit number", chosenreddit)
    srname=subredditchoice[int(chosenreddit)]
    
    
    print("Getting random image from me_irl")
    reddit = praw.Reddit(client_id=reddit_config.client_id, client_secret=reddit_config.client_secret,
                         user_agent=reddit_config.user_agent)
    print(srname)
    sr = reddit.subreddit(srname)
    x=True
    accepted_type= ["jpg","peg","png","gif"] #last three characters of image file extensions
    while x:
        url = str(sr.random().url)
        url_type=url[-3:]
        print(url)
        print(url_type)
        if url_type in accepted_type:
            x=False
            print("URL is to an image file")
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