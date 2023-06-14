print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find Queen Mommy of Karenarnia and the treasure.") 

hero = input("Welcome advendturer! What is your name? \n")
choice1 = input(f'Welcome, {hero}! Let\'s begin! Will you go "left" or "right"? \n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
        choice3 = input("You discover a small boat and row across. You arrive at the island unharmed. There is a castle with 3 doors. One red, one yellow and one blue. Which color do you choose? \n").lower()
        if choice3 == "yellow":
            choice4 = input("You enter a hall of mirrors. Will you go left, right, or staight? \n").lower()
            if choice4 == "left":
                choice5 = input('There\'s a red button. Will you push it? Type "yes" or "no". \n').lower()
                if choice5 == "yes":
                    print(f"The mirrored wall opens up. You found Queen Mommy and treasure! Congratulations, {hero}! You Win!")
                else:
                    print("Nothing happens. Try again.")
            else:
                print("You are sucked into the Mirror Realm! Game over.")
                
        elif choice3 == "red":
            print('It\'s The DRAGON ROOM! The scaly beast burns your buns so you go jump in the lake to put out the fire. You\'re swallowed whole by a giant alligator! Game Over.')
        elif choice3 == "blue":
            print("You enter and the door slams behind you! A trap door opens and you fall to your doom into a pool of toxic wizard sweat! Game Over.")
        else:
            print("Me thinks you are not taking the mission seriously... Game over.")
    elif choice2 == "swim":

        print("Halfway across the lake, you are swallowed whole by a giant alligator! Game over.")
    else:
        print(f"There is no time for such foolishness, {hero}! Game over.")
else:
    print("Locusts swarm you and eat all of your hair! Game over.")
