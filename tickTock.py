import time
def tickTock(seconds):
  
    for i in range(seconds): 
        if i % 2 == 0: 
            print("Tick....")
        else:
            print("Tock....") 
        time.sleep(1)
tickTock(10)

