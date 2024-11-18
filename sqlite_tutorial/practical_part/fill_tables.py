from connect import MyConnection
from random import choice
from sqlite3 import Cursor
from faker import Faker

faker = Faker()

def create_random_students(groups_ids:list[int])->tuple:
    first_name = faker.first_name()
    last_name = faker.last_name()
    enrollment = faker.date(pattern='%d-%m-%Y')
    groups_id:int = choice(groups_ids)
    return first_name, last_name, enrollment, groups_id

def create_random_teacher()->tuple[str,str]:
    first_name = faker.first_name()
    last_name = faker.last_name()
    return first_name, last_name

def create_random_grade()->int:
    return faker.random_int(0, 100)

def create_random_data():
    return faker.date(pattern='%Y-%m-%d')

name_groups = ['Group-A', 'Group-B', 'Group-C']
form_query = 'INSERT INTO Groups (name_group) VALUES (?)'

form_students = 'INSERT INTO Students (firstname, lastname, enrollment, group_id) VALUES (?, ?, ?, ?)'
form_teachers = 'INSERT INTO Teachers (firstname, lastname) VALUES (?, ?)'
form_subject = 'INSERT INTO Subjects (name, teacher_id) VALUES (?, ?)'
form_grade = 'INSERT INTO Grades ( student_id, subject_id, grade, date_registered ) VALUES (?, ?, ?, ?)'

def fill_table_groups(c:Cursor,sql_query:str, list_groups:list[str],size_table:int):
    for _ in range(size_table):
        random_group:str = choice(list_groups)
        c.execute(sql_query,(random_group,))

def fill_table_students(c:Cursor, sql_query:str, num_students:int):
    groups_ids = get_groups_id(c)
    for _ in range(num_students):
        c.execute(sql_query,create_random_students(groups_ids))


def get_groups_id(c:Cursor)->list[int]:
    c.execute('SELECT id FROM Groups')
    rows = c.fetchall()
    return [row[0] for row in rows]

def get_teachers_id(c:Cursor)->list[int]:
    c.execute('SELECT id From Teachers')
    rows = c.fetchall()
    return [row[0] for row in rows]

def get_students_id(c:Cursor)->list[int]:
    c.execute('SELECT id From Students')
    rows = c.fetchall()
    return [row[0] for row in rows]

def get_subjects_id(c:Cursor)->list[int]:
    c.execute('SELECT id From Subjects')
    rows = c.fetchall()
    return [row[0] for row in rows]

def fill_table_teachers(c:Cursor,sql_query:str, size_table:int):
    for _ in range(size_table):
        c.execute(sql_query, create_random_teacher())

def fill_table_subject(c:Cursor, sql_query:str, size_table:int):
    subjects = ['Math', 'Science', 'English', 'History', 'Geography']
    teachers_ids = get_teachers_id(c)
    for _ in range(size_table):
        subject = choice(subjects)
        teachers_id = choice(teachers_ids)
        c.execute(sql_query, (subject,teachers_id))

def fill_table_grade(c:Cursor, sql_query:str, size_table:int=20):
    student_ids = get_students_id(c)
    subjects_ids = get_subjects_id(c)
    for student_id in student_ids:
        for _ in range(size_table):
            subjects_id = choice(subjects_ids)
            c.execute(sql_query, (student_id,subjects_id, create_random_grade(),create_random_data()))

if __name__ == '__main__':

    with MyConnection() as db:
        cursor = db.get_cursor()
        fill_table_grade(cursor, form_grade)



