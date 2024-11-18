from create import MyConnection

#создать индекс если он не существует на таблице Users по таким полям(email)
create_index_form = 'CREATE INDEX IF NOT EXISTS idx_email ON Users (email)'
select_form = 'SELECT username, age FROM Users WHERE age > ?'

T = list(tuple)

if __name__ == '__main__':
    with MyConnection() as db:
        # db.process_execute(create_index_form)
        cursor = db.get_cursor()
        cursor.execute(select_form,(25,))
        results:T = cursor.fetchall()
        print(results)
