

print("{0:=>15}".format(""),end=" ")
print("Tic Tac Toe Game",end=" ")
print("="*15)
user_input = input("Press ENTER to start the game or type 'exit' to leave   ") or "play"
while user_input not in ("play","exit"):
	print("\nPlease give a correct response")
	user_input = input("Press ENTER to start the game or type 'exit' to leave   " or "play")


board_ls = ["1","2","3","4","5","6","7","8","9"]
used = []
winner  = None
if user_input == "play":
	play  = True
	print("\n\nGame Started!!!\nPlayer 1 will use 'X' and Player 2 will use 'O'")
	print("Type the number where you want to place your MARK\n")
	def make_board(l):
		print("\n")
		print(" " + l[6] + " | " + l[7] + " | " + l[8])
		print("-"*10)
		print(" " + l[3] + " | " + l[4] + " | " + l[5])
		print("-"*10)
		print(" " + l[0] + " | " + l[1] + " | " + l[2])
		print("-"*10)
		print("\n")
	make_board(board_ls)

	def space_check(ls,pos):
		return ls[pos] in ["1","2","3","4","5","6","7","8","9"]

	def full_check(ls):
		for i in range(0,9):
			if space_check(board_ls,i):
				return False
		return True		

	def checker(mark):
		return ((board_ls[0] == board_ls[3] == board_ls[6] == mark) or
				(board_ls[1] == board_ls[4] == board_ls[7] == mark) or
				(board_ls[2] == board_ls[5] == board_ls[8] == mark) or
				(board_ls[0] == board_ls[4] == board_ls[8] == mark) or
				(board_ls[6] == board_ls[7] == board_ls[8] == mark) or
				(board_ls[3] == board_ls[4] == board_ls[5] == mark) or
				(board_ls[0] == board_ls[1] == board_ls[2] == mark) or
				(board_ls[6] == board_ls[4] == board_ls[2] == mark))
	
	while play:
		# Player 1
		player1 = int(input("Choose your move, Player 1 > ")) - 1
		while player1 in used:
			print("WRONG MOVE! Take another number")
			player1 = int(input("\nChoose your move, Player 1 > ")) - 1
		else:	
			board_ls[player1] = "X"
			used.append(player1)
			if checker('X'):
				print("\nGame Ended!! \n\nPlayer 1 won\n\n")
				make_board(board_ls)
				break
			elif full_check(board_ls):
				print("The Game ended in a draw")
				make_board(board_ls)
				break	
		# Player 2	
		player2 = int(input("\nChoose your move, Player 2 > ")) - 1	
		while player2 in used:
			print("WRONG MOVE! Take another number")
			player2 = int(input("\nChoose your move, Player 2 > ")) - 1
		else:
			board_ls[player2] = "O"
			used.append(player2)	
			if checker('O'):
				print("\nGame Ended!! \n\nPlayer 2 won\n\n")
				make_board(board_ls)
				break
			elif full_check(board_ls):
				print("The Game ended in a draw")
				make_board(board_ls)
				break

		make_board(board_ls)
			

elif user_input == 'exit':
	print("\nThanks for visiting :)")	
