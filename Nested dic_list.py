# Nested dictonary in lists 
game = {'Home': {}, 'Visitor': {}}
for inning in range(1, 10000):  # Loop from 1 to 10000 exclude 10000.
    game['Home'][inning] = 0  # Initialize home team runs for this inning to 0.
    game['Visitor'][inning] = 0  # Initialize visitor team runs for this inning to 0.
    # Fill in the code for this part.
game['Home'][3] = 1  # Set one run in third inning.