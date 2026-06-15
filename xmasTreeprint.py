import random
size = int(input("Enter the tree size: "))
for row_num in range (1, size + 1):
    row_string = ""
    
    for oranaments in range (0, row_num*2-1):
        random_num = random.randint(1, 4) == 1
        if random_num:
            row_string = row_string + "o"
        else:
            row_string = row_string + "^"
   
    print(" "*(size - row_num) + row_string)


for trunk_num in range (1,3):
    print(" "*(size - 1) + "#"*1)
    