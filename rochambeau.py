rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
rochambeau = round(random.random() * 3)
begin = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))

if begin == 0 and rochambeau == 0:
  print((rock) + "\n" + "Computer also chose: \n" + (rock) + "\n" + "It's a draw")
elif begin == 1 and rochambeau == 0:
  print((paper) + "\n" + "Computer chose: \n" + (rock) + "\n" + "You win")
elif begin == 2 and rochambeau == 0:
  print((scissors) + "\n" + "Computer chose: \n" + (rock) + "\n" + "You lose")
elif begin == 0 and rochambeau == 1:
  print((rock) + "\n" + "Computer chose: \n" + (paper) + "\n" + "You lose")
elif begin == 0 and rochambeau == 2:
  print((rock) + "\n" + "Computer chose: \n" + (scissors) + "\n" + "You win")
elif begin == 1 and rochambeau == 1:
  print((paper) + "\n" + "Computer also chose: \n" + (paper) + "\n" +"It's a draw")
elif begin == 1 and rochambeau == 2:
  print((paper) + "\n" + "Computer chose: \n" + (scissors) + "\n" + "You lose")
elif begin == 2 and rochambeau == 1:
  print((scissors) + "\n" + "Computer chose: \n" + (paper) + "\n" + "You win")
elif begin == 2 and rochambeau == 2:
  print((scissors) + "\n" + "Computer also chose: \n" + (scissors) + "\n" + "It's a draw")
else:
  print("Invalid choice. Please try again")
