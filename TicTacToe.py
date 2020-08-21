import pygame 

#initializing pygame
pygame.init()

#window
win = pygame.display.set_mode((700, 750))
pygame.display.set_caption('Tic Tac Toe with AI')
win.fill((255, 255, 255))

#fonts
TITLE = pygame.font.SysFont('comicsans', 70).render('Tic-Tac-Toe with AI', 1, (0, 0, 0))
SUB_TITLE = pygame.font.SysFont('arial', 30)
X = pygame.font.SysFont('arial', 150).render('X', 1, (0,0,0))
O = pygame.font.SysFont('arial', 150).render('O', 1, (0,0,0))

#board
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
you_count = 0
comp_count = 0

#run conditions
won = False
AI = True
#draw function for redrawing board after an event 
def draw(you_count, comp_count, AI):
	win.fill((255, 255, 255))
	win.blit(TITLE, (130, 10))

	if AI:
		you = SUB_TITLE.render('You: ' + str(you_count), 0, (0,0,0))
		win.blit(you, (25, 60))
		comp = SUB_TITLE.render('Comp: ' + str(comp_count), 0, (0,0,0))
		win.blit(comp, (575, 60))
	else:
		you = SUB_TITLE.render('P1: ' + str(you_count), 0, (0,0,0))
		win.blit(you, (25, 60))
		comp = SUB_TITLE.render('P2: ' + str(comp_count), 0, (0,0,0))
		win.blit(comp, (575, 60))

	restart = SUB_TITLE.render('Restart : Spacebar', 0, (0,0,0))
	win.blit(restart, (255, 60))

	first = pygame.draw.rect(win, (255, 255, 255), (55, 110, 190, 190))
	second = pygame.draw.rect(win, (255, 255, 255), (255, 110, 190, 190))
	third = pygame.draw.rect(win, (255, 255, 255), (455, 110, 190, 190))

	fourth = pygame.draw.rect(win, (255, 255, 255), (55, 310, 190, 190))
	fifth = pygame.draw.rect(win, (255, 255, 255), (255, 310, 190, 190))
	sixth = pygame.draw.rect(win, (255, 255, 255), (455, 310, 190, 190))

	seventh = pygame.draw.rect(win, (255, 255, 255), (55, 510, 190, 190))
	eighth = pygame.draw.rect(win, (255, 255, 255), (255, 510, 190, 190))
	ninth = pygame.draw.rect(win, (255, 255, 255), (455, 510, 190, 190))

	longitude1 = pygame.draw.rect(win,(0, 0, 0), (257, 110, 6, 590))
	longitude2 = pygame.draw.rect(win,(0, 0, 0), (457, 110, 6, 590))

	latitude1 = pygame.draw.rect(win,(0, 0, 0), (55, 312, 590, 6))
	latitude2 = pygame.draw.rect(win,(0, 0, 0), (55, 512, 590, 6))

	rectangles = [first, second, third, fourth, fifth, sixth, seventh, eighth, ninth]
	return rectangles
#stores output of draw()
square = draw(you_count, comp_count, AI)
#button for AI
ai_button = pygame.draw.circle(win, (0,0,0), (670, 720,), (20))
ai = SUB_TITLE.render('AI', 0, (0,255,230))
win.blit(ai, (657, 700))
#button for two player
tp_button = pygame.draw.circle(win, (230,230,230), (620, 720,), (20))
tp = SUB_TITLE.render('2P', 0, (0,255, 230))
win.blit(tp, (607, 700))

#returns AI's move
def comp_move(board):
	new_board = []
	for row in board:
		for number in row:
			new_board.append(number)
	#finds possible moves from new_board which only has integers
	possibleMoves = [index for index, number in enumerate(new_board) if number == 0]
	move = 0
	confirmed = False
	#calculates the winning move as x and o and if it is a winning move it returns it since it can either win or block opponent
	for letter in [2, 1]:
		for i in possibleMoves:
			boardCopy = [new_board[:3], new_board[3:6], new_board[6:]]
			if i in [0,1,2]:
				boardCopy[0][i] = letter
			if i in [3,4,5]:
				boardCopy[1][i-3] = letter
			if i in [6,7,8]:
				boardCopy[2][i-6] = letter
			if check_winner(letter, boardCopy, confirmed):
				move = i
				return move 
	#middle box gets priority
	if 4 in possibleMoves:
		move = 4
		return move 
	#and so on so that the AI doesn't become predictable a random is also chosen
	Open = []
	for i in possibleMoves:
		if i in [0, 2]:
			Open.append(i)

	edgesOpen = []
	for i in possibleMoves:
		if i in [1, 3, 5, 7]:
			edgesOpen.append(i)

	cornersOpen = []
	for i in possibleMoves:
		if i in [0, 2, 6, 8]:
			cornersOpen.append(i)
	
	if len(Open) > 0:
		move = selectRandom(Open)
		return move
	if len(edgesOpen) < 4 and len(cornersOpen) < 4 and len(edgesOpen) > 0:
		move = selectRandom(edgesOpen)
		return move
	if len(cornersOpen) < 4 and len(cornersOpen) > 0:
		move = selectRandom(cornersOpen)
		return move
	if len(edgesOpen) > 0:
		move = selectRandom(edgesOpen)
		return move
	if len(cornersOpen) > 0:
		move = selectRandom(cornersOpen)
		return move

#choosing a random box so that the AI doesn't become predictable
def selectRandom(li):
	import random
	length = len(li)
	if length > 1:
		r = random.randrange(0, length)
		return li[r]
	else:
		return li[0]
 
#checks if there is a win
def check_winner(num, board, confirmed):
	#check rows
	count = 0 #<< counts what row is being checked
	for row in board:
		count += 1
		for index in row:
			if index == num:
				continue
			else:
				break
		else:
			if confirmed:
				if count == 1:
					pygame.draw.line(win, (150, 0, 150),(122, 200),(595, 200),(10))
				if count == 2:
					pygame.draw.line(win, (150, 0, 150), (122, 400),(595, 400), (10))
				if count == 3:
					pygame.draw.line(win, (150, 0, 150), (122, 600), (595, 600), (10))
			return True
	
	count = 0
	#check columns
	for column in range(3):
		count += 1
		for row in board:
			if row[column] == num:
				continue
			else:
				break
		else:
			if confirmed:
				if count == 1:
					pygame.draw.line(win, (150, 0, 150),(150, 145),(150, 655),(10))
				if count == 2:
					pygame.draw.line(win, (150, 0, 150), (350, 145), (350, 655), (10))
				if count == 3:
					pygame.draw.line(win, (150, 0, 150), (550, 145), (550, 655), (10))
			return True

	#check left to right diagonal
	for index in range(3):
		if board[index][index] == num:
			continue
		else:
			break
	else:
		if confirmed:
			pygame.draw.line(win, (150, 0, 150), (55, 110), (645, 700), (10))
		return True

	#check right to left diagonal 
	for index in range(3):
		if board[index][2-index] == num:
			continue
		else:
			break
	else:
		if confirmed:
			pygame.draw.line(win, (150, 0, 150), (645, 110), (55, 700), (10))
		return True

#checks for a tie 
def check_tie(board):
	for row in board:
		for number in row:
			if number == 0:
				return False
	else:
		return True
		
#what letter's turn it is
draw_letter = 'X'
run = True 

#main loop (checks for events)
while run:

	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT: #<< if the red x button is pressed on the top right hand corner then it exits the program
			run = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE: # if the spacebar is pressed then everything gets a reset including score
				win.fill((255, 255, 255))
				won = False
				board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
				you_count = 0
				comp_count = 0
				draw_letter = 'X'

				draw(you_count, comp_count, AI)
				# redraws buttons without switching modes
				if AI:
					ai_button = pygame.draw.circle(win, (0,0,0), (670, 720), (20))
					win.blit(ai, (657, 700))
					tp_button = pygame.draw.circle(win, (230,230,230), (620, 720), (20))
					win.blit(tp, (607, 700))
				if AI != True:
					tp_button = pygame.draw.circle(win, (0,0,0), (620, 720), (20))
					win.blit(tp, (607, 700))
					ai_button = pygame.draw.circle(win, (230,230,230), (670, 720), (20))
					win.blit(ai, (657, 700))

		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos() #attains mouse's position(coordinates)
			if won != True: #only works if no one has won yet
				if tp_button.collidepoint(pos): #if the two player button is clicked then it switches and redraws
					win.fill((255, 255, 255))
					won = False
					board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
					you_count = 0
					comp_count = 0
					draw_letter = 'X'
					
					AI = False

					draw(you_count, comp_count, AI)

					tp_button = pygame.draw.circle(win, (0,0,0), (620, 720),(20))
					win.blit(tp, (607, 700))
					ai_button = pygame.draw.circle(win, (230,230,230), (670, 720),(20))
					win.blit(ai, (657, 700))
					
				if ai_button.collidepoint(pos): #if the AI button is clicked then it switches and redraws
					win.fill((255, 255, 255))
					won = False
					board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
					you_count = 0
					comp_count = 0
					draw_letter = 'X'

					AI = True

					draw(you_count, comp_count, AI)

					ai_button = pygame.draw.circle(win, (0,0,0), (670, 720), (20))
					win.blit(ai, (657, 700))
					tp_button = pygame.draw.circle(win, (230,230,230), (620, 720), (20))
					win.blit(tp, (607, 700))
				#checks if a square has been hit and if it has then it draws letter on it
				if square[0].collidepoint(pos) and board[0][0] == 0:
					if draw_letter == 'X':
						win.blit(X, (105, 115))
						draw_letter = 'O'
						board[0][0] = 1
					elif draw_letter == 'O' and AI != True:
						win.blit(O, (105, 115))
						draw_letter = 'X'
						board[0][0] = 2
				if square[1].collidepoint(pos) and board[0][1] == 0:
					if draw_letter == 'X':
						win.blit(X, (305, 115))
						draw_letter = 'O'
						board[0][1] = 1
					elif draw_letter == 'O' and AI != True:
						win.blit(O, (305, 115))
						draw_letter = 'X'
						board[0][1] = 2
				if square[2].collidepoint(pos) and board[0][2] == 0:
					if draw_letter == 'X':
						win.blit(X, (505, 115))
						draw_letter = 'O'
						board[0][2] = 1
					elif draw_letter == 'O' and AI != True:
						win.blit(O, (505, 115))
						draw_letter = 'X'
						board[0][2] = 2
				
				if square[3].collidepoint(pos) and board[1][0] == 0:
					if draw_letter == 'X':
						win.blit(X, (105, 315))
						draw_letter = 'O'
						board[1][0] = 1
					elif draw_letter == 'O' and AI != True:
						win.blit(O, (105, 315))
						draw_letter = 'X'
						board[1][0] = 2
				if square[4].collidepoint(pos) and board[1][1] == 0:
					if draw_letter == 'X':
						win.blit(X, (305, 315))
						draw_letter = 'O'
						board[1][1] = 1
					elif draw_letter == 'O' and AI != True:
						win.blit(O, (305, 315))
						draw_letter = 'X'
						board[1][1] = 2
				if square[5].collidepoint(pos) and board[1][2] == 0:
					if draw_letter == 'X':
						win.blit(X, (505, 315))
						draw_letter = 'O'
						board[1][2] = 1
					elif draw_letter == 'O' and AI != True:
						win.blit(O, (505, 315))
						draw_letter = 'X'
						board[1][2] = 2
				
				if square[6].collidepoint(pos) and board[2][0] == 0:
					if draw_letter == 'X':
						win.blit(X, (105, 515))
						draw_letter = 'O'
						board[2][0] = 1
					elif draw_letter == 'O' and AI != True:
						win.blit(O, (105, 515))
						draw_letter = 'X'
						board[2][0] = 2
				if square[7].collidepoint(pos) and board[2][1] == 0:
					if draw_letter == 'X':
						win.blit(X, (305, 515))
						draw_letter = 'O'
						board[2][1] = 1
					elif draw_letter == 'O' and AI != True:
						win.blit(O, (305, 515))
						draw_letter = 'X'
						board[2][1] = 2
				if square[8].collidepoint(pos) and board[2][2] == 0:
					if draw_letter == 'X':
						win.blit(X, (505, 515))
						draw_letter = 'O'
						board[2][2] = 1
					elif draw_letter == 'O' and AI != True:
						win.blit(O, (505, 515))
						draw_letter = 'X'
						board[2][2] = 2
	#confirmed needed so check_winner() knows if it is being acutally checked for a win or by AI to find winning move					
	confirmed = True
	if check_winner(1, board, confirmed): #checks for a win for X and score increase for X and redraw
		if AI:
			win.blit(SUB_TITLE.render('You WIN!', 1, (0,0,0)), (310, 710))
		else:
			win.blit(SUB_TITLE.render('P1 WINS!', 1, (0,0,0)), (320, 710))
		pygame.display.update()
		pygame.time.delay(1000)
		you_count = you_count + 1
		board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		won = False
		draw(you_count, comp_count, AI)

		if AI:
			ai_button = pygame.draw.circle(win, (0,0,0), (670, 720), (20))
			win.blit(ai, (657, 700))
			tp_button = pygame.draw.circle(win, (230,230,230), (620, 720), (20))
			win.blit(tp, (607, 700))
		if AI != True:
			tp_button = pygame.draw.circle(win, (0,0,0), (620, 720), (20))
			win.blit(tp, (607, 700))
			ai_button = pygame.draw.circle(win, (230,230,230), (670, 720), (20))
			win.blit(ai, (657, 700))
		

	if check_winner(2, board, confirmed): #checks for a win for O and score increase for O and redraw
		if AI:
			win.blit(SUB_TITLE.render('Computer WINS!', 1, (0,0,0)), (265,710))
		else:
			win.blit(SUB_TITLE.render('P2 WINS!', 1, (0,0,0)), (305,710))
		pygame.display.update()
		pygame.time.delay(1000)
		comp_count = comp_count + 1
		board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		won = False
		
		draw(you_count, comp_count, AI)

		if AI:
			ai_button = pygame.draw.circle(win, (0,0,0), (670, 720), (20))
			win.blit(ai, (657, 700))
			tp_button = pygame.draw.circle(win, (230,230,230), (620, 720), (20))
			win.blit(tp, (607, 700))
		if AI != True:
			tp_button = pygame.draw.circle(win, (0,0,0), (620, 720), (20))
			win.blit(tp, (607, 700))
			ai_button = pygame.draw.circle(win, (230,230,230), (670, 720), (20))
			win.blit(ai, (657, 700))
	
	if check_tie(board) and won != True: #checks for a tie and redraw
		tie = SUB_TITLE.render('TIE!', 1, (0,0,0))
		win.blit(tie, (340, 710))
		pygame.display.update()
		pygame.time.delay(1000)
		board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		won = False
		
		draw(you_count, comp_count, AI)

		if AI:
			ai_button = pygame.draw.circle(win, (0,0,0), (670, 720), (20))
			win.blit(ai, (657, 700))
			tp_button = pygame.draw.circle(win, (230,230,230), (620, 720), (20))
			win.blit(tp, (607, 700))
		if AI != True:
			tp_button = pygame.draw.circle(win, (0,0,0), (620, 720), (20))
			win.blit(tp, (607, 700))
			ai_button = pygame.draw.circle(win, (230,230,230), (670, 720), (20))
			win.blit(ai, (657, 700))
		

	if won != True: #only works if no one has won yet
		if AI: #if it is in AI mode
			if draw_letter == 'O': #if it is AI's turn
				move = comp_move(board) #retrieves move from move() then draws it on the square
				if move == 0:
					win.blit(O, (105, 115))
					draw_letter = 'X'
					board[0][0] = 2
				if move == 1:
					win.blit(O, (305, 115))
					draw_letter = 'X'
					board[0][1] = 2
				if move == 2:
					win.blit(O, (505, 115))
					draw_letter = 'X'
					board[0][2] = 2
					
				if move == 3:
					win.blit(O, (105, 315))
					draw_letter = 'X'
					board[1][0] = 2
				if move == 4:
					win.blit(O, (305, 315))
					draw_letter = 'X'
					board[1][1] = 2
				if move == 5:
					win.blit(O, (505, 315))
					draw_letter = 'X'
					board[1][2] = 2
					
				if move == 6:
					win.blit(O, (105, 515))
					draw_letter = 'X'
					board[2][0] = 2
				if move == 7:
					win.blit(O, (305, 515))
					draw_letter = 'X'
					board[2][1] = 2
				if move == 8:
					win.blit(O, (505, 515))
					draw_letter = 'X'
					board[2][2] = 2
					
				pygame.display.update() #updates the display for AI move

	pygame.display.update()#updates display for everything 

pygame.quit() #quits pygame


