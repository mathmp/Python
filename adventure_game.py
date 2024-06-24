#This game is about a person who discovery himself in magic world, where he will make decisions to survive to the challenges that will come#

#About letting someone to play the game, I don't know someones here who speaks english #

import sys

print("Welcome to a new World")
start = input("You wake up in a forest, and you see two paths to follow, one on the rigth and the other on the left. Choose left or rigth:\n")
if start.lower()=="right":
    print("You found monsters on your way, you run and fall in a whole. In that whole you find a mage stuff. It give you a power of an element.")
elif start.lower()=="left":
    print("You found mosters on your way, you run and find a sword on the floor. That sword it's magic, you can use a power of an element")
else:
    print("You didn't choose a path, monsters find you, and you die")
    sys.exit()

power = input("Choose an element: Fire or lightning:\n")

if power.lower()=="fire":
    print("You received the power of the fire. With that power you blame all the monsters you find")
elif power.lower()=="lightning":
    print("You received the power of the lightning. With that power you kill all the monsters you find")
else:
    print("You are not able to use magic! The monsters are too strong for you and you die!")
    sys.exit()

print("You killed all the monsters with your weapon. Walking for your path, you find mercenaries attacking some soldiers and a carriage, you choose help the soldiers with your special abillity. The king of the land was in the carriage, and he saw you figthing, so he invite you to the castle")
king = input("In The castle he gives you a cash reward to help to save him. and he gives you an opportunitie to train to be a wizard or a soldier of the castle. Choose to become a soldier or a wizard:\n")

if king.lower()=="wizard" and start.lower()=="rigth":
    print("Now you are a wizard of the kingdom")
elif king.lower()=="wizard" and start.lower()=="left":
    print("Now you are a wizard of the kingdom and a magic swordsman")
elif king.lower()=="soldier" and start.lower()=="rigth":
    print("Now you are a soldier of the kingdom with abilities of a wizard")
elif king.lower()=="soldier" and start.lower()=="left":
    print("Now you are a soldier of the kingom")
else:
    print("You reiceved the reward and get out the castle to have a common life in the kingdom")


