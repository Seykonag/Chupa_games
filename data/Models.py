import sqlite3 as sq


async def database_start():
    global database, cur

    database = sq.connect('data/Chupa_games.db')
    cur = database.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, balance INT)")
    database.commit()


async def create_profile(user_id):
    user = check_user(user_id)

    if not user:
        cur.execute("INSERT INTO profile VALUES(?, ?)",
                    (user_id, 0))
        database.commit()


async def edit_profile(user_id, value):
    cur.execute("UPDATE profile SET balance = (balance + ?) WHERE user_id == ? ",
                (value, user_id))
    database.commit()


def return_value(user_id):
    result = cur.execute(f"SELECT * FROM profile WHERE user_id='{userпше_id}'").fetchone()
    return result[1]


def check_user(user_id):
    return cur.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()
