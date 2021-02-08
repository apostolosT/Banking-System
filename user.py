from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from account import Account
    from bank import Bank



class User():
    def __init__(self,) -> None:
        self.fname:str=None
        self.lname:str=None
        self.username:str=None
        self.password:str=None
        self.login_logs:'list(str)'=[]
        self.id:int=0
        self.accounts:'list(Account)'=[]
        self.current_account:"Account"=None
       
       
    
    def login(self,username:str,password:str):
        if (self.username==username and password==self.password):
            print("Login Succesful")
            return True
        else:
            print("Please Retry") 
            return False



    def register(self)->bool:
        self.fname = input("Enter first name: ")
        self.lname = input("Enter last name: ")
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        pass_check = input("Enter password again: ")

        if self.password == pass_check:
            print("Password match, you can login")
            print("Registration succesfull")
            # assign as primary account the first account is user accounts list
            return True
            
        else:
            print("Something Went Wrong")
            return False

    def add_account(self,account:'Account'):
        self.accounts.append(account)

    def logout(self):
        pass

