import random

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'
choice = [ROCK,PAPER,SCISSOR]

computer_choice = random.choice(choice)


user_choice = input("PCIK YOUR CHOICE (r,p,s) :")
print(f"Computer choice is {computer_choice}")
print(f"User Choice is :{user_choice}")

if user_choice == computer_choice:
    print("tie")
elif user_choice == 'r' and computer_choice == 'p' or user_choice == 'p' and computer_choice == 's' or  user_choice == 's' and computer_choice == 'r':    
    print("Computer Wins")
else:
    print("USER Wins")