from connect import MyConnection
from sqlite3 import Cursor
def list_tables(cursor:Cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return [table[0] for table in tables]

if __name__ == '__main__':
    with MyConnection() as db:
        cursor = db.get_cursor()
        tables = list_tables(cursor)
        for table in tables:
            print(table)
