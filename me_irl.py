from constants import *
import praw, reddit_config, urllib.request, random, time

def me_irlscript(command, client, message):
    print("Getting random image from me_irl")
    reddit = praw.Reddit(client_id=reddit_config.client_id, client_secret=reddit_config.client_secret,
                         user_agent=reddit_config.user_agent)
    sr = reddit.subreddit("me_irl")
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
    print("Image placed at: ",file_name)
    time.sleep(1)
    print("Sending Image")
    run_coro(client.send_file(message.channel, file_name), client) # Send Image
    print("Sent Image")