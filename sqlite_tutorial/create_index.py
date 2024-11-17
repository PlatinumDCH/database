from create import MyConnection

if __name__ == '__main__':
    with MyConnection() as db:
        cursor = db.get_cursor()
        cursor.execute('CREATE INDEX idx_email ON Users (email)')
