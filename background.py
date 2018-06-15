import time, os, requests, shutil

#This file is all the background tasks required to keep the bot running, This file is executed on launch and every 5 minutes after.

print("Background open")
 
if not os.path.exists("temp"):
    os.makedirs("temp")  
    
while True:
    #This script runs every 5 minutes
        
    #Clear Images Folder
    print("Clearing the temp folder")
    for item in os.listdir("temp"):
        if not item.endswith(".lock") and not os._exists(item + ".lock"):
            filename = ("temp/" + item)
            print("Removing: ", filename)
            os.remove(filename)
            
            
    #Retrieve copypasta index from GitHub
    print("Downloading cpindex")
    url = "https://raw.githubusercontent.com/Shitscord/cp-lib/master/index.py"
    r = requests.get(url)
    with open("temp/cpindex.py", "wb") as w:
        w.write(r.content)
    time.sleep(2)
    shutil.move("temp/cpindex.py","cpindex.py")
    print("Done")
    
    #Retrieve images index from Github
    print("Downloading memeindex")
    url = "https://raw.githubusercontent.com/Shitscord/meme-lib/master/index.py"
    r = requests.get(url)
    with open("temp/memeindex.py", "wb") as w:
        w.write(r.content)
    time.sleep(2)
    shutil.move("temp/memeindex.py","memeindex.py")
    print("Done")
    
    time.sleep(300)
    