import sys
import pathlib

current_path = pathlib.Path(__file__).parent.parent.resolve()
sys.path.append(f'{current_path}')

from sql_cfg import DATABASE_PATH
import sqlite3 as sq
from states.UserClass import User
import pandas as pd
from dacite import from_dict


database = sq.connect(DATABASE_PATH)
cursor = database.cursor()

def sql_get_user_data(user_id: str) -> User:

    sql_request = f'SELECT * FROM users WHERE id = {user_id}'
    df = pd.read_sql(sql_request, database)

    if df.empty:
        return False
    
    df = df.to_dict('records')[0]
    user = from_dict(data_class = User, data = df)
    return user


def sql_get_all_users_ids() -> list[str]:

    sql_request = 'SELECT id FROM users'
    ids = cursor.execute(sql_request).fetchall()
    ids = [i[0] for i in ids]
    return ids


def sql_add_user(user: User) -> None:

    sql_request = 'INSERT INTO users VALUES (?, ?, ?)'
    data = user.unpack()
    print(data)
    cursor.execute(sql_request, data)
    database.commit()


def sql_delete_user(user_id: str) -> None:

    sql_request = f'DELETE FROM users WHERE id = {user_id}'
    cursor.execute(sql_request)
    database.commit()


if __name__ == '__main__':
    
    user = User('1234','ltt','coffee')
    user1 = User('871623', 'john')
    user2 = User('17269387', 'alex', 'uber')
    
    users = [user,user1,user2]
    for i in users:
        sql_add_user(i)

    data = sql_get_user_data(1234)
    if data:
        print(data)
    print(sql_get_all_users_ids())
    sql_delete_user(1234)
