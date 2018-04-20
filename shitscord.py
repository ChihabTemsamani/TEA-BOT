from multiprocessing import Process
import os

#This is just the boot file which launches the threads. All the botty-goodness is in bot.py.


def fgprocess():
    os.system('python bot.py')

def bgprocess():
    os.system('python background.py')
        
        
        
if __name__ == '__main__':
  p1 = Process(target=fgprocess)
  p1.start()
  p2 = Process(target=bgprocess)
  p2.start()
  p1.join()
  p2.join()
