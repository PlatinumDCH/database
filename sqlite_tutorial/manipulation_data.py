from create import MyConnection
from data import query_form
from faker import Faker


fake = Faker()
if __name__ == '__main__':
    with MyConnection() as db:
        cursor = db.get_cursor()
        for _ in range(50):
            user = (fake.user_name(), fake.email(), fake.random_int(18,65),)
            cursor.execute(query_form, user)
