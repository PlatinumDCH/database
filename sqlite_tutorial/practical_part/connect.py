import sqlite3
from sqlite3 import Connection,Cursor

class MyConnection:
    def __init__(self, name_base:str='my_database.db'):
        self.name_base = name_base
        self.conn:Connection = None

    def connect(self)->Connection:
        return sqlite3.connect(self.name_base)

    def get_cursor(self)->Cursor:
        if self.conn is None:
            self.conn = self.connect()
        return self.conn.cursor()

    def close(self)->None:
        if self.conn:
            print('Connection closed')
            self.conn.close()
            self.conn = None

    def commit_data(self)->None:
        """save changes"""
        if self.conn:
            print('Changes committed')
            self.conn.commit()

    def rollback_data(self)->None:
        if self.conn:
            print('Changes rolled back')
            self.conn.rollback()


    def __enter__(self):
        try:
            self.conn = self.connect()
            self.cursor = self.conn.cursor()
            print('Connection TRUE')
            return self
        except sqlite3.Error as err:
            print('Error connection', err)
            return None

    def  __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type  is not None:
            print('rollback transaction, error', exc_value)
            self.rollback_data()
        else:
            self.commit_data()
            print ('transaction completed')

        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
            print('Cursor closes')

        self.close()
