
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from user import User

from db_utils import update_balance
class Account():
    def __init__(self,id:int,balance:int) -> None:
        self.id=id
        self.__balance=balance

    def get_balance(self)->int:
        return self.__balance

    def deposit(self,amount:int)->bool:
        if(amount>0): 
            self.__balance+=amount
            update_balance(self.__balance,self.id)
            return True
        else:
            False
            
    
    def withdraw(self,amount:int)->bool:
        if(amount>0 & amount<=self.__balance): 
            self.__balance-=amount
            update_balance(self.__balance,self.id)
            return True
        else:
            False
    
