from create import MyConnection
from data import query_insert
from faker import Faker


fake = Faker()
if __name__ == '__main__':
    with MyConnection() as db:
        cursor = db.get_cursor()
        for _ in range(50):
            username = fake.user_name()
            email = fake.email()
            age = fake.random_int(min=18, max=65)
            cursor.execute(query_insert, (username, email, age,))
