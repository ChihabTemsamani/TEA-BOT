from multiprocessing import Process
import os, time

#This is just the boot file which launches the threads. All the botty-goodness is in bot.py.

def bgprocess():
    os.system('python background.py')

def fgprocess():
    os.system('python bot.py')

        
if __name__ == '__main__':
  p1 = Process(target=bgprocess)
  p1.start()
  time.sleep(10)
  p2 = Process(target=fgprocess)
  p2.start()
  p1.join()
  p2.join()