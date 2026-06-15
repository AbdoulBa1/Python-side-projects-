size = int(input("Enter the tree size: "))
for row_num in range (1, size + 1):
    print(" "*(size - row_num) + "^"*(row_num*2-1))
for trunk_num in range (1,3):
    print(" "*(size - 1) + "#"*1)