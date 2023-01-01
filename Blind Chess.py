from stockfish import Stockfish
import random
stockfish = Stockfish()
shouldFish=False
white=True

def testSquare():
	global shouldFish
	while(True):
		s=random.choice('abcdefgh')+random.choice('12345678')
		p=str(stockfish.get_what_is_on_square(s))
		if(p=='None'):
			p=""
		else:
			p=p.split(".")[1].split("_")
			p=p[0][0]+p[1][0]+p[1][-1]
		print("What is on "+s+"?")
		if(input().upper()==p):
			return
		shouldFish=True
		print("Wrong, it's actually a "+p+"!")
		print(stockfish.get_board_visual(white))

def move():
	global shouldFish
	while(True):
		m=input("Your move: ")
		if(m and stockfish.is_move_correct(m)):
			stockfish.make_moves_from_current_position([m])
			return
		shouldFish=True
		print(stockfish.get_board_visual(white))

def aiMove(m):
	global shouldFish
	if(shouldFish):
		shouldFish=False
		stockfish.make_moves_from_current_position([m])
		print(m)
		return
	l=[]
	for a in 'abcdefgh':
		for b in '12345678':
			for c in 'abcdefgh':
				for d in '12345678':
					m=a+b+c+d
					if(stockfish.is_move_correct(m)):
						l.append(m)
	m=random.choice(l)
	stockfish.make_moves_from_current_position([m])
	print("Opponent's move: "+m)

if(random.random()<0.5):
	white=False
	print("You are black!")
	aiMove(None)
while(True):
	if(stockfish.get_best_move() is None):
		exit()
	testSquare()
	move()
	m=stockfish.get_best_move()
	if(m is None):
		exit()
	print("\033c\033[3J")
	testSquare()
	aiMove(m)