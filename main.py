import json
import random
from pathlib import Path
from bank import Bank



print(r"""
       _              _                
|_) _.._ |   __|_ |/    _|_  _.| 
|_)(_|| ||< (_)|  |\|_|_>| |(_|| 
                                 
      """)

user = Bank()

while True:    
    choice = (input("""
What would you like to do today:
1) Create Account
2) Deposit
3) Withdraw
4) Update your details
5) Delete your account
your answer:- """))

    if choice not in ("1", "2", "3", "4", "5"):
        print("Please give a valid input.")
        continue
    else:
        break    

if choice == "1": 
    user.create_account()
elif choice == "2":
    user.deposit_money()
elif choice == "3":
    user.withdraw_money()
elif choice == "4":
    user.update_details()
else:
    user.delete_account()
    
    
        
        
        
        





    
    
    
    