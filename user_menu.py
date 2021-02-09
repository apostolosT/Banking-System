from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from user import User
    from bank import Bank
    from account import Account

from db_utils import *
class UserMenu():
    def __init__(self,current_user:"User",bank:"Bank") -> None:
        self.current_user=current_user
        self.bank=bank
        self.current_account:"Account"=self.current_user.current_account()
        self.choices={
            "1": self.deposit_handler,
            "2": self.withdraw_handler,
            "3": self.check_balance_handler,
            "4": self.add_account_handler,
            "5": self.view_accounts_handler,
            "6":self.select_account_handler,
            "7": self.remove_account_handler,
            "8": self.change_addess_handler,
            "9": self.exit_handler
        }

    def run(self):
        print("Welcome {} {}".format(self.current_user.fname,self.current_user.lname))
        user_menu="""
                        User Menu

            1. Deposit              2. Withdraw
            3. Check Balance        4. Add new bank account
            5. View accounts        6. Select account
            7. Remove account       8. Change address
            9. Exit
            """   
        while(True):
            print(user_menu)
            choice=input("Enter Option from the User Menu: ")
            action=self.choices.get(choice)
            if action:
                action()
            else:
                print("{} is not a valid choice".format(choice))
        



    def add_account_handler(self):
        self.bank._open_account(self.current_user)
    
    def remove_account_handler(self):
        pass

    def select_account_handler(self):
        pass

    def view_accounts_handler(self):
        pass
    
    def change_addess_handler(self):
        pass
    
    def withdraw_handler(self):
        withdraw=int(input("Enter amount to be withdrawn "))
        self.current_account.withdraw(withdraw)
        self.check_balance_handler()

    
    def deposit_handler(self):

        deposit=int(input("Enter amount to be deposited "))
        self.current_account.deposit(deposit)
        self.check_balance_handler()
    
    def check_balance_handler(self):
    
        print("Your current balance is "+str(self.current_account.get_balance()))

    def exit_handler(self):
        pass