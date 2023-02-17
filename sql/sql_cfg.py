import pathlib, sys

current_path = pathlib.Path(__file__).parent.parent.resolve()

DATABASE_PATH = f'{current_path}/databases/users.db'