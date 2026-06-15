import random
size = int(input("Enter the tree size: "))

row_num = 1
while row_num <= size:
    row_string = ""
    oranaments = 0
    while oranaments <= (row_num*2-1):
        random_num = random.randint(1, 4) == 1
        if random_num:
                 row_string = row_string + "o"
        else:
                row_string = row_string + "^"

        oranaments += 1
    print(" "*(size - row_num) +(row_string))
    row_num += 1
trunk_num = 0
while trunk_num < 2:
        print(" "*(size-1)+"#"*1)
        trunk_num += 1

