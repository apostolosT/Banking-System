import sqlite3


def delete_all_records(table_name: str):
    conn = sqlite3.connect("data/bank_data.db")
    with conn:
        conn.execute("DELETE FROM {}".format(table_name))
    del conn


def select_last_id(conn, table_name: str, id: str):
    sql = """
        SELECT {} FROM {} ORDER BY {} DESC LIMIT 1
"""
    cur = conn.cursor()
    try:
        cur.execute(sql.format(id, table_name, id))
        last_uid = cur.fetchone()
    finally:
        cur.close()

    if not last_uid:
        return False
    else:
        return last_uid[0]


def add_user(connection, u_id, fname, lname, uname, passwd):
    sql = "INSERT INTO users (u_id,first_name,last_name,username,password) VALUES(?,?,?,?,?);"
    with connection:
        connection.execute(sql, (u_id, fname, lname, uname, passwd))


def add_account(conn, acc_id, u_id, balance):
    sql = "INSERT INTO accounts (acc_id,u_id,balance) VALUES(?,?,?);"

    with conn:
        conn.execute(sql, (acc_id, u_id, balance))


def update_balance(balance, acc_id):
    sql = """
            UPDATE accounts
            SET balance= ?
            WHERE acc_id= ?;
"""
    conn = sqlite3.connect("data/bank_data.db")
    with conn:
        conn.execute(sql, (balance, acc_id))


def verify_user(conn, username, password):
    sql = """
            SELECT *
            FROM users
            WHERE username=? and password=?;
"""
    cursor = conn.cursor()
    try:
        cursor.execute(sql, (username, password))
        user = cursor.fetchone()
        return user
    except:
        print("User not found")
    finally:
        cursor.close()


def get_acc_id(u_id):
    conn = sqlite3.connect("data/bank_data.db")
    # cursor=conn.cursor()
    sql = """
        SELECT acc_id FROM accounts
        WHERE u_id={};
        """
    cursor = conn.cursor()
    with conn:
        cursor.execute(sql.format(u_id))
        return cursor.fetchone()[0]


def get_balance(acc_id):
    conn = sqlite3.connect("data/bank_data.db")
    sql = """
        SELECT balance 
        FROM accounts
        WHERE acc_id={};
        """
    cursor = conn.cursor()
    with conn:
        cursor.execute(sql.format(acc_id))
        return cursor.fetchone()[0]


def make_transaction():
    pass
