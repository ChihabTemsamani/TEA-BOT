import time, os

global run
print("Background open")
while True:
    time.sleep(300)
    print("Clearing the images folder")
    for item in os.listdir("images"):
        if not item.endswith(".lock") and not os._exists(item + ".lock"):
            os.remove(item)