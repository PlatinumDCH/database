from connect import MyConnection
from faker import Faker

faker = Faker()
form_student_create = '''
    CREATE TABLE IF NOT EXISTS Students(
    id INTEGER PRIMARY KEY,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    email TEXT,
    phone_number TEXT NOT NULL, 
    enrolment_date TEXT NOT NULL -- Дата как строка в формате YYYY-MM-DD
    )
'''
insert_student_query = '''
    INSERT INTO Students (
    firstname, lastname, email, phone_number, enrolment_date)
    VALUES (?, ?, ?, ?, ?)
'''
def get_fake_param():
    firstname = faker.first_name()
    lastname = faker.last_name()
    email = faker.email()
    phone_number = faker.phone_number()
    enrolment_date = faker.date(pattern='%d-%m-%Y')
    return firstname, lastname, email, phone_number, enrolment_date

def fill_student_table():
    with MyConnection() as db:
        cursor = db.get_cursor()
        cursor.execute(form_student_create) # create table

        for i in range(50):
            cursor.execute(insert_student_query,  get_fake_param()) # insert data

if __name__ == '__main__':
    fill_student_table()


