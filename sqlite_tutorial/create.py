import sqlite3
from sqlite3 import Connection,Cursor

class MyConnection:
    def __init__(self, name_base:str = 'chinook.db'):
        self.name_base = name_base
        self.conn: Connection = self.connect()

    def connect(self)->Connection:
        return sqlite3.connect(self.name_base)

    def get_cursor(self)->Cursor:
        return self.conn.cursor()

    def close(self)->None:
        self.conn.close()

    def commit_data(self)->None:
        self.conn.commit()

    def execute_query(self, query:str, params:tuple = ()):
        cursor = self.get_cursor()
        cursor.execute(query,params)
        return cursor.fetchall()

    def fetch_all_users(self,form_sql:str) -> list:
        return self.execute_query(form_sql)

    def process_execute(self,form:str, param:tuple=()):
        c = self.get_cursor()
        c.execute(form, param)


    def __enter__(self):
        """User for automat connection-close [with]"""
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        """User for automat connection-close [with]"""
        if exc_type or exc_value or exc_tb:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    sql_script = '''
        CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER)
    '''
    with MyConnection() as db:
        cursor = db.get_cursor()
        cursor.execute(sql_script)
        print('created TRUE')