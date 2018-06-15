#Reddit image finder algorithm
import praw, reddit_config, random

def find(subreddit): 
    reddit = praw.Reddit(client_id=reddit_config.client_id, client_secret=reddit_config.client_secret, user_agent=reddit_config.user_agent)
    try:
        reddit.subreddits.search_by_name(subreddit, exact=True)
    except:
        return("sr_invalid")
    postcount = 0
    for post in reddit.subreddit(subreddit).hot(limit = 100):
        postcount += 1    
    w=0
    x=True
    accepted_type= ["jpg","peg","png"] #last three characters of image file extensions
    while x:
        sub = reddit.subreddit(subreddit)
        srposts = [post for post in sub.hot(limit=postcount)]
        randpostnum = random.randint(0, postcount-1)
        randpost = srposts[randpostnum]
        url = str(randpost.url)
        url_type=url[-3:]
        print(url)
        print(url_type)
        if url_type in accepted_type:
            x=False
        w += 1
        if w==30:
             x=False
             return("noimagefound")
        else:
            return(str(url))