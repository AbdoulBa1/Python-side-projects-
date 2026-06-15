size = int(input("Enter the tree size: "))
row_num = 1
while row_num <= size:
    print(" "*(size - row_num) + "^"*(row_num*2-1))
    row_num += 1

trunk_num = 0
while trunk_num < 2:
        print(" "*(size-1)+"#"*1)
        trunk_num += 1

