from decimal import Decimal

print()
print("welcome to the dungeon")

def wrong_input():
	print("Wrong choice!!!")

def dead(death_message):
	print (0.2 + 0.1)
	print (Decimal("0.2") + Decimal("0.1"))

	print ("you are dead! %s" % (death_message))
	
def life(life_message):
	return ("you get a new life! %s" % (life_message))


name = input("what is your name? ")

print("HELLo %s, welcome to the dungeion!" % (name))


print ("1. open door 1 ")
print ("2. open door 2 ")

choice = input ("> ")

if choice == "1":
	print (life("Hurrah!!!"))
elif choice == "2":
	dead("TOD!!")
else :
	wrong_input()


