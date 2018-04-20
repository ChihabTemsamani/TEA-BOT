import time, os

global run
print("Background open")
while True:
    #This script runs every 5 minutes
    time.sleep(300)
    print("Clearing the images folder")
    for item in os.listdir("images"):
        if not item.endswith(".lock") and not os._exists(item + ".lock"):
            filename = ("images/" + item)
            print("Removing: ", filename)
            os.remove(filename)