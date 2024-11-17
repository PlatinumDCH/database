from create import MyConnection
from data import sql_create_table


if __name__ == '__main__':
    with MyConnection() as db:
        cursor = db.get_cursor()
        cursor.execute(sql_create_table)
