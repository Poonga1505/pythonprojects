import random
comp_input= random.randint(1,101)
while True:
    try:
      user_input=int(input("Enter the guess number"))
      if user_input >comp_input:
          print(" Its too high")
      elif user_input <comp_input:
          print(" Its too low ")
      else:
          print(" you won the game")
          break
    except ValueError:
         print(" enter a valid number")
        
