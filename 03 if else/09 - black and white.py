chess_string = int(input('enter the number of string in chess table\n'))
chess_column = int(input('enter the number of column in chess table\n'))
if (chess_string + chess_column) % 2 == 0:
    print('square is black')
else:
    print('square is white')