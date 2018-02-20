import time, os

sleeptime = 60

class Service:
    def __init__(self):
        pass
    def run(self):
        while True:
            time.sleep(sleeptime)
            for item in os.listdir("images"):
                if not item.endswith(".lock") and not os._exists(item + ".lock"):
                    os.remove(item)