import random


while True:
    user_input=input("Roll the dice y/n : ").lower()
    if(user_input == "y"):
        r1=random.randint(1,6)
        r2=random.randint(1,6)
        print(f'({r1},{r2})')
    elif (user_input == "n"):
        print("Thankyou for Playing")
        break
    else:

      print("Invalid Input!")
