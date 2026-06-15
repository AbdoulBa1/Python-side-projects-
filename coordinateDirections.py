def get_end_cordinates(direction):
     x = 0
     y = 0
     for move in direction:
        if move == 'N':
            y += 1
        elif move == 'S':
            y -= 1
        elif move == 'E':
            x += 1
        elif move == 'W':
            x -= 1
     return (x, y)
     
valid_moves= ['N', 'S', 'E', ' or W']
collected_direction = []
user_input = input("Enter a direction (N, S, E, or W) or press Enter to stop: ")
while user_input != "":   
     collected_direction.append(user_input.upper())
     user_input = input("Enter a direction (N, S, E, or W) or press Enter to stop: ")
print(get_end_cordinates(collected_direction))

  

