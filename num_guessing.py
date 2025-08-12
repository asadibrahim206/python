import random


number_toguess = random.randint(1,100)
while True:
    choice = int(input("enter the number : "))
    if choice == number_toguess:
        print("wohooo! you have guessed the right number")
        break
    elif choice != number_toguess and choice > number_toguess:
        print("you are to high")
        
    elif choice != number_toguess and choice < number_toguess:
        print("you are low")
        
    else:
        print("invalid choice")
        