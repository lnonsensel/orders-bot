import sqlite3 as sq
from sql_cfg import DATABASE_PATH

def sql_setup():
    base = sq.connect(DATABASE_PATH)
    cur = base.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users
                (id TEXT,
                name TEXT,
                orders_ids TEXT
                )"""
                )
    
    base.commit()
    cur.close()
    base.close()
    
if __name__ == '__main__':
    sql_setup()