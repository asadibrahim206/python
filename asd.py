import random

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'


computer_count = 3
user_count = 3

    
def choice():
    choice = [ROCK,PAPER,SCISSOR]
    computer_choice = random.choice(choice)
    user_choice = input("PCIK YOUR CHOICE (r,p,s) :")
    print(f"Computer choice is {computer_choice}")
    print(f"User Choice is :{user_choice}")

    return user_choice,computer_choice


choices = choice()
print(choices)