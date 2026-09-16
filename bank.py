import json
import random
from pathlib import Path

class Bank():
    dummy_data = []
    database = Path('data.json')
    
    try:
        if database.exists():
            with open(database) as fs:
                dummy_data = json.loads(fs.read())
        else:
            print("No such file exists.")
    except Exception as err:
        print(f"an exception occured {err}.")
        
    def update(self):
        with open(self.database, "w") as fs:
            fs.write(json.dumps(self.dummy_data, indent=3))
            
    def generate_account_no(self):
        # ensure generated account number is not already used
        while True:
            acc = random.randrange(10000, 999999)
            if not any(d.get("account_no") == acc for d in self.dummy_data):
                return acc
    def age(self):
        while True:
            try:
                return int(input("Enter your age: "))
                
            except ValueError:
                print("Age must be a valid integer.")
                
    def pin(self):
        while True:
            try:
                pin = int(input("Create a 4 digit pin code: "))
                if 1000 <= pin <= 9999:
                    return pin
                else:
                    print("PIN must be a 4-digit number.")
            except ValueError:
                print("PIN must be a valid integer.")
            
        
    def create_account(self):
        user_details = {
            "name": input("Enter your name: "),
            "age": self.age(),
            "email": input("Enter your email: "),
            "pin": self.pin(),
            "account_no": self.generate_account_no(),
            "balance": 0
        }
        
        if user_details["age"] <= 17:
            print("sorry you are not eligible to make an account.")
        else:
            print("Account successfully created......")
            print("Here's the summary: \n")
            for key, value in user_details.items():
                print(f"{key}: {value}")
        
        
            self.dummy_data.append(user_details)
            self.update()
        
        
        
    def deposit_money(self):
        try:
            account_num = int(input("Enter your account number: "))
        except ValueError:
            print("Account number must be numeric.")
            return
        try:
            pincode = int(input("Enter your pin: "))
        except ValueError:
            print("PIN must be numeric.")
            return

        for i in self.dummy_data:
            if i.get('account_no') == account_num and i.get('pin') == pincode:
                print(f"Details Matched. Welcome {i.get('name')}\n")
                while True:
                    try:
                        deposit_amount = float(input("Enter deposit amount: "))
                        if deposit_amount <= 0:
                            print("Deposit must be a positive amount.")
                            continue
                        i['balance'] = i.get('balance', 0) + deposit_amount
                        print("Deposit Successful")
                        print(f"Your current balance: {i['balance']} ")
                        self.update()
                        return
                    except ValueError:
                        print("Please enter a valid number for the amount.")
        print("Account not found.")
                
        
    def withdraw_money(self):
        try:
            account_num = int(input("Enter your account number: "))
        except ValueError:
            print("Account number must be numeric.")
            return
        try:
            pincode = int(input("Enter your pin: "))
        except ValueError:
            print("PIN must be numeric.")
            return

        for i in self.dummy_data:
            if i.get('account_no') == account_num and i.get('pin') == pincode:
                print(f"Details Matched. Welcome {i.get('name')}\n")
                while True:
                    try:
                        withdraw_amount = float(input("Enter withdraw amount: "))
                        if withdraw_amount <= 0:
                            print("withdraw must be a positive amount.")
                            continue
                        if i.get('balance', 0) < withdraw_amount:
                            print("Insufficient funds.")
                            return
                        i['balance'] = i.get('balance', 0) - withdraw_amount
                        print("withdraw Successful")
                        print(f"Your current balance: {i['balance']} ")
                        self.update()
                        return
                    except ValueError:
                        print("Please enter a valid number for the amount.")
        print("Account not found.")
    def update_details(self):
        try:
            account_num = int(input("Enter your account number: "))
        except ValueError:
            print("Account number must be numeric.")
            return
        try:
            pincode = int(input("Enter your pin: "))
        except ValueError:
            print("PIN must be numeric.")
            return
        for i in self.dummy_data:
            if i.get("account_no") == account_num and i.get('pin') == pincode:
                print(f"Details Matched. Welcome {i.get('name')}.\n")
                print("What would you like to update?")
                print("1) Name\n2) Email\n3) PIN\n4) Cancel")
                choice = input("Choose (1-4): ")
                if choice == "1":
                    new_name = input("Enter new name: ")
                    i['name'] = new_name
                    print("Name updated.")
                elif choice == "2":
                    new_email = input("Enter new email: ")
                    i['email'] = new_email
                    print("Email updated.")
                elif choice == "3":
                    while True:
                        try:
                            new_pin = int(input("Enter new 4-digit PIN: "))
                            if 1000 <= new_pin <= 9999:
                                i['pin'] = new_pin
                                print("PIN updated.")
                                break
                            else:
                                print("PIN must be a 4-digit number.")
                        except ValueError:
                            print("PIN must be a valid integer.")
                else:
                    print("Update cancelled.")
                self.update()
                return
        print("Account not found.")
                
        
    def delete_account(self):
        try:
            account_num = int(input("Enter your account number: "))
        except ValueError:
            print("Account number must be numeric.")
            return
        try:
            pincode = int(input("Enter your pin: "))
        except ValueError:
            print("PIN must be numeric.")
            return

        for index, i in enumerate(self.dummy_data):
            if i.get('account_no') == account_num and i.get('pin') == pincode:
                print(f"Details Matched. Account belongs to {i.get('name')}.")
                confirm = input("Are you sure you want to delete this account? (y/n): ")
                if confirm.lower() == 'y':
                    self.dummy_data.pop(index)
                    self.update()
                    print("Account deleted.")
                    return
                else:
                    print("Deletion cancelled.")
                    return
        print("Account not found.")
        