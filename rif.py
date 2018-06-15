#Reddit image finder algorithm
import praw, reddit_config, random

def find(subreddit, sortby, maxrange, attempts): 
    print("looking in subreddit: ", subreddit, ". Sorting by: ", sortby, ". Random range: ", maxrange, ". And giving ", attempts, " attempts.")
    reddit = praw.Reddit(client_id=reddit_config.client_id, client_secret=reddit_config.client_secret, user_agent=reddit_config.user_agent)
    try:
        reddit.subreddits.search_by_name(subreddit, exact=True)
    except:
        return("sr_invalid")
    postcount = 0
    for post in reddit.subreddit(subreddit).hot(limit = maxrange):
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
            return(str(url))
        w += 1
        if w==attempts:
             x=False
             return("noimagefound")