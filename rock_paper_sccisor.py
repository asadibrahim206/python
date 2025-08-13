import random



    
def choices():
    ROCK = 'r'
    PAPER = 'p'
    SCISSOR = 's'

    choice = [ROCK,PAPER,SCISSOR]
    computer_choice = random.choice(choice)
    user_choice = input("PCIK YOUR CHOICE (r,p,s) :")
    print(f"Computer choice is {computer_choice}")
    print(f"User Choice is :{user_choice}")

    return user_choice,computer_choice

def main(computer_count = 3,user_count = 3):
    while True:
        if user_choice == computer_choice:
            print("tie")
        elif user_choice == 'r' and computer_choice == 'p' or user_choice == 'p' and computer_choice == 's' or  user_choice == 's' and computer_choice == 'r':    
            print("Computer Wins")
            user_count -=1
            if user_count == 0:
                print("GAME OVER , YOU LOOSE") 
            
                break
        elif user_choice == 'p' and computer_choice == 'r' or user_choice == 's' and computer_choice == 'p' or  user_choice == 'r' and computer_choice == 's':
            print("USER Wins")
            computer_count -=1
            if computer_count == 0:
                print("YOU WIN!!!") 
                break
        else:
            print("inValid Input....Please try again")

            return

# def restart():
#     inp = input("DO YOU WANT TO RESTART THE GAME? (Y/N):").lower()
#     if inp == 'y':
#         main()
#     elif inp == 'n':
#         print("thank you for playing")


user_choice,computer_choice = choices()
main()
   
    
        
