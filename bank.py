from user import User
from account import Account
import csv
from db_utils import *
import pandas as pd


class Bank():
    def __init__(self) -> None:
       self.conn=sqlite3.connect("data/bank_data.db")
       self.__last_user_id=int(select_last_id(self.conn,"users","u_id"))
       self.__last_account_id=int(select_last_id(self.conn,"accounts","acc_id"))
       if(not self.__last_user_id):
           self.__last_user_id=0
       if(not self.__last_account_id):
           self.__last_account_id=0

    

    def register_user(self,user:"User"):
        user.id=self.__last_user_id
        self.__last_user_id+=7
        add_user(self.conn,user.id,user.fname,user.lname,user.username,user.password)
        self.create_account(user)

    def verify_login(self,username,password):
        user=verify_user(self.conn,username,password)
        return user      

    def create_account(self,user:"User"):
        new_account=Account(self.__last_account_id,0)
        self.__last_account_id+=13
        add_account(self.conn,new_account.id,user.id,new_account.get_balance())
        print("Account with id {} created for user {} {} ".format(new_account.id,user.fname,user.lname))