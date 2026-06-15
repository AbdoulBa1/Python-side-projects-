def white_rook_can_capture(rook,board):
    rook_column = rook[0]
    rook_row = rook[1]
    capturable_squares = []
    for square, piece in board.items():
        square_column = square[0]
        square_row = square[1]
        if (square_column == rook_column or square_row == rook_row) and piece[0]=='b':
            capturable_squares.append(square)
    return capturable_squares
print(white_rook_can_capture('d5',{'d8':'bQ','d2':'bB','f1':'wP', 'c5':'bN' })) # i can put any piece in the board and it will return the list of capturable squares for the white rook at d5 or etc .


            
