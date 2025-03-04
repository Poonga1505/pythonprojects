import random


while(True):
    user_choice=int(input(" enter a number "))
    comp_choice= random.randint(1,10)

    if user_choice == comp_choice:
        print(" you won the game")
    elif user_choice > comp_choice:
        print(" your guess is too high")
    elif user_choice < comp_choice:
        print(" your choice is too low")
    else:
        print(" Please enter a number between 1-100")




              
