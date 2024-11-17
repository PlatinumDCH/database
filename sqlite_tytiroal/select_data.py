from create import MyConnection
from data import select_form

if __name__ == '__main__':
    with MyConnection() as db:
        users = db.fetch_all_users()
        for user in users:
            print(user)