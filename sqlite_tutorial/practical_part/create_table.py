import sqlite3

from connect import MyConnection
from pathlib import Path


def read_sql_file(file_path):
    try:
        with open(file_path,'r' ) as file:
            return file.read()
    except FileNotFoundError:
        print(f'Error: file "{file_path}" not found')
        return None
    except IOError as err:
        print(f'Error input/output become read file "{file_path}": {err}')
        return None

if __name__ == '__main__':
    sql_file_path = Path('form_create_table.sql')
    sql_queries = read_sql_file(sql_file_path)
    if sql_queries:
        with MyConnection() as db:
            if db is not None:
                cursor = db.get_cursor()

                try:
                    cursor.executescript(sql_queries)
                    print('table successfully created')
                except sqlite3.Error as e:
                    print('Error for processing SQL queries')


