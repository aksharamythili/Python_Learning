import random
ladder={6:20,12:98,34:50,67:75,2:15}
snake={7:4,33:10,99:1}
pos1=0
pos2=0
pos3=0
def move(pos):
    dice=random.randint(1,6)
	    print(f"dice:{dice}")
	    pos=pos+dice
	    if pos in snake:
		    print("Snake encounterd ")
		    pos=snake[pose]
		    print(f"position:{pos}")
        elif pos in ladder:
    	    print("Ladder encountred")
    	    pos=ladder[pos]
    	    print(f"position:{pos}")
        else:
	        print(f"position{pos}")
	print("\n")	
	return pos

while True:
	A=input("player a entered to throw dice")
	pos=move(pos1)
	if pos1>=100:
		print("game over player 1 wins")
		break
B=input("player B entered to throw dice")
	pos=move(pos2)
	if pos2>=100:
		print("game over player 2 wins")
		break
C=input("player C entered to throw dice")
	pos=move(pos3)
	if pos3>=100:
		print("game over player 3 wins")
		break
