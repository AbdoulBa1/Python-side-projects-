import time
WIDTH = 50
counter = 0
while True:
    for counter in range(50):
       print(("O"*counter)+(50-counter)*".")
       time.sleep(0.05)
    for counter in range(50):
        print(("."*counter)+(50-counter)*"O")
        time.sleep(0.05)

 
