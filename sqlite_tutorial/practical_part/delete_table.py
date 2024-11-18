from connect import MyConnection


def del_table(table_name:str):
    with MyConnection() as db:
        cursor = db.get_cursor()
        drop_table_query = f'DROP TABLE IF EXISTS {table_name}'
        try:
            cursor.execute(drop_table_query)
            print('Table successfully dropped')
        except:
            print('Failed to drop table')

if __name__ == '__main__':
    name_table = 'Users'
    del_table(name_table)

