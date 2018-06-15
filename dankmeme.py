import urllib.request, random, time, os, rif, constants

def script(command, client, message):
    subredditchoice=["me_irl","trippinthroughtime","vsaucememes","dankmemes","lossedits","labelmemes","meirl"]    
    subredditcount=len(subredditchoice)
    chosenreddit=random.randint(0,subredditcount-1)
    srname=subredditchoice[int(chosenreddit)]    
    url=rif.find(srname, "hot", 50, 10)
    url_type=url[-3:]
    if url_type=="jpg":
        file_name="temp/"+str(random.randint(1,1000))+".jpg"
    if url_type=="jpeg":
        file_name="temp/"+str(random.randint(1,1000))+".jpeg"
    if url_type=="png":
        file_name="temp/"+str(random.randint(1,1000))+".png"           
    urllib.request.urlretrieve(url, file_name)
    open(file_name + ".lock","a").close()
    time.sleep(1)
    constants.run_coro(client.send_file(message.channel, file_name), client) # Send Image

    