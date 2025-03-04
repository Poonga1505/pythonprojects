import random

emoji={'r':'rock','s':'scissor','p':'paper'}
choices=('r','p','s')
while True:
    user_choice=input("Rock,Paper,Scissor ? (r/p/s)")
    if user_choice not in choices:
        print("Invalid Input");
        continue
    comp_choice=random.choice(choices)
    print(f'you chose {emoji[user_choice]}')
    print(f'computer chose {emoji[comp_choice]}')
    if user_choice==comp_choice:
        print("Its Tie")
    elif( (user_choice=='r' and comp_choice=='s')or
          (user_choice=='s' and comp_choice=='p')or
          (user_choice=='p' and comp_choice=='s')):
        print(" user Win")
    else:
        print("Computer Win")
    should_continue=input('continue(y/n):').lower()

    if should_continue == 'n':
      break
                          
                          
                          

    
    
        
