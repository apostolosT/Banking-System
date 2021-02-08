
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from user import User

class Account():
    def __init__(self,user:'User',id:str) -> None:
        # self.customer=user
        self.id=id
        self.__balance:int=0

        #  we're adding the current account, to the list for that customer.
        #  Any time an account gets created, the customer will have it on its list

        user.add_account(self)
    
    def balance(self)->str:
        return str(self.__balance)

    def deposit(self,amount:int)->bool:
        if(amount>0): 
            self.__balance+=amount
            return True
        else:
            False
            
    
    def withdraw(self,amount:int)->bool:
        if(amount>0 & amount<=self.__balance): 
            self.__balance-=amount
            return True
        else:
            False
    
