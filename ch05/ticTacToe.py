the_board = {'top_L': ' ','top_M': ' ','top_R': ' ',
			 'mid_L': ' ','mid_M': ' ','mid_R': ' ',
			 'low_L': ' ','low_M': ' ','low_R': ' ',}

def print_board(board):
	print(board['top_L'] + '|' + board['top_M'] + '|' + board['top_R'] )
	print('-+-+-')
	print(board['mid_L'] + '|' + board['mid_M'] + '|' + board['mid_R'] )
	print('-+-+-')
	print(board['low_L'] + '|' + board['low_M'] + '|' + board['low_R'] )

turn = 'X'
for i in range(9):
	print_board(the_board)
	print(turn + 'の番です。どこに打つ？')
	move = input()
	the_board[move] = turn
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'

print_board(the_board)
