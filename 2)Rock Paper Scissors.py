import random

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

image = [rock, paper, scissors]

user = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(image[user])

computer = random.randint(0, 2)
print("Computer chose:")
print(image[computer])
if user>=3 or user<0:
  print("select from what i asked ")
elif user==0 and computer==2:
  print("You Win!")
elif computer==0 and user==2:
  print("You Lost!")
elif user>computer:
 print("You Win!")
elif computer>user:
  print("You Lost!")
elif user==computer:
  print("It's a Draw")
