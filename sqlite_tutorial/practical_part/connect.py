import sqlite3
from sqlite3 import Connection,Cursor

class MyConnection:
    def __init__(self, name_base:str='my_database.db'):
        self.name_base = name_base
        self.conn:Connection = self.connect()

    def connect(self)->Connection:
        return sqlite3.connect(self.name_base)
    def get_cursor(self)->Cursor:
        return self.conn.cursor()
    def close(self)->None:
        return self.conn.close()
    def commit_data(self)->None:
        self.conn.commit()
    def __enter__(self):
        return self
    def  __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type or exc_value or exc_tb:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()