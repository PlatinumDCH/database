from create import MyConnection
from sqlite3 import Cursor


def get_cursor(db) -> Cursor:
    cursor = db.get_cursor()
    return cursor


def print_row(rows):
    for row in rows:
        print(row)


def execute_query(query: str):
    with MyConnection() as db:
        cursor = get_cursor(db)
        if cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            print_row(result)


def select_all() -> None:
    form_sql = '''Select * From tracks;'''
    execute_query(form_sql)


def select_definite_field() -> None:
    form_sql = '''Select Name, Milliseconds, TrackId
                From tracks
                Limit 10;'''
    execute_query(form_sql)

def used_order()->None:
    form_sql = '''Select Name, Milliseconds, albumid
                  From tracks
                  Order by Milliseconds, albumid
                  
                  Limit 10;'''
    execute_query(form_sql)

def form_1()->None:
    form_sql = '''Select DISTINCT city From customers Order by city;'''
    execute_query(form_sql)

def form_2()->None:
    form_sql = '''Select Name, Milliseconds, TrackId
                  From tracks
                  Order by Name, TrackId;'''
    execute_query(form_sql)

def form_3()->None:
    form_sql = '''Select Title, Name
                  From albums
                  Join artists on artists.ArtistID = albums.ArtistId;'''
    execute_query(form_sql)

if __name__ == '__main__':
    form_3()