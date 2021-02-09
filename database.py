import sqlite3

connection=sqlite3.connect("data/bank_data.db")

create_users_table= "CREATE TABLE users (u_id INTEGER PRIMARY KEY,first_name TEXT, last_name TEXT, username TEXT, password TEXT);"
create_accounts_table= "CREATE TABLE accounts (acc_id INTEGER PRIMARY KEY,u_id INTEGER NOT NULL,balance INTEGER, FOREIGN KEY (u_id) REFERENCES users (u_id));"
create_transactions_table= "CREATE TABLE transactions (t_id INTEGER PRIMARY KEY,amount INTEGER, type TEXT, acc_id REFERENCES accounts (acc_id));"

with connection:
    connection.execute(create_users_table)
    connection.execute(create_accounts_table)
    connection.execute(create_transactions_table)