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
    df = df.to_dict('records')[0]
    df['orders_ids'] = list(df['orders_ids'])
    user = from_dict(data_class = User, data = df)
    return user


def sql_add_user(user: User) -> None:

    sql_request = 'INSERT INTO users VALUES (?)'
    data = user.unpack()
    cursor.executemany(sql_request, data)
    database.commit()


def sql_delete_user(user_id: str) -> None:

    sql_request = f'DELETE FROM users WHERE id = {user_id}'
    cursor.execute(sql_request)
    database.commit()


if __name__ == '__main__':
    
    user = User('1234','ltt',['qweqwe','oijsdofsjd'])
    data = sql_get_user_data(1234)
    print(data)
    print(user.unpack())
