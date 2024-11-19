from connect import MyConnection
from sqlite3 import Cursor


def form_1(c:Cursor):
    """
    :param c: Database cursor object used to execute SQL queries
    :return: List of tuples containing student ID, first name, and average grade of the top 5 students, ordered by descending average grade
    """
    sql_form = '''
                Select Students.id, Students.firstname, avg(Grades.grade) as average_grade
                From Students
                Join Grades on Students.id = Grades.student_id
                Group by Students.firstname
                Order by average_grade DESC
                Limit 5;'''
    c.execute(sql_form)
    return c.fetchall()

def form_2(c:Cursor,subject:str,limit:int=1):
    """
    :param c: Database cursor object used to execute SQL queries.
    :param subject: The name of the subject to filter student grades.
    :param limit: The maximum number of students to return, ordered by highest average grade in the specified subject. Default is 1.
    :return: A list of tuples containing student names, subject name, and their average grade in the specified subject, limited by the given number.
    """
    sql_form = '''
            Select Students.firstname, Subjects.name as sub_name, avg(Grades.grade)
            From Students
            Join Grades on Students.id = Grades.student_id
            Join Subjects on Grades.subject_id
            Where Subjects.name = '{}'
            Group by Students.id
            Order by avg(Grades.grade) Desc
            Limit {};      
    '''.format(subject, limit)
    c.execute(sql_form)
    return c.fetchall()


def form_3(c:Cursor,subject:str):
    """
    :param c: The database cursor used to execute the SQL query.
    :param subject: The name of the subject for which the average grade per group is to be calculated.
    :return: A list of tuples where each tuple contains the group name and the corresponding average grade.
    """
    sql_form = '''Select Groups.name_group as group_name, ROUND(avg(Grades.grade), 2) as average_grade
                   From Groups
                   Join Students On Groups.id = Students.group_id
                   Join Grades On Grades.student_id = Students.id
                   Join Subjects On Grades.subject_id = Subjects.id
                   Where Subjects.name = '{}'
                   Group By Groups.id, Groups.name_group; 
                   '''.format(subject)
    c.execute(sql_form)
    return c.fetchall()

def form_4(c:Cursor):
    """
    :param c: Database cursor object used to execute SQL commands.
    :return: List of tuples containing the average grade from the Grades table.
    """
    sql_form = '''Select avg(Grades.grade) as average_grades
               From Grades
               Order by average_grades'''
    c.execute(sql_form)
    return c.fetchall()

def form_5(c:Cursor):
    """
    Finds and returns the courses taught by each teacher.

    :param c: Database cursor to execute the query.
    :return: A list of tuples containing subject names and the corresponding teacher's first name.
    """
    sql_form = '''Select Subjects.name, Teachers.firstname
                   From Subjects
                   Join Teachers on Subjects.teacher_id = Teachers.id;
                   '''
    c.execute(sql_form)
    return c.fetchall()

def form_6(c:Cursor,name_group:str='Group-A'):
    """
    :param c: Database cursor used to execute SQL queries.
    :param name_group: Name of the group to filter students by. Defaults to 'Group-A'.
    :return: List of students in the specified group.
    """
    sql_form = '''Select Students.firstname, Groups.name_group as group_name
                 From Students
                 Join Groups on Students.group_id = Groups.id
                 Where Groups.name_group = '{}';
                 '''.format(name_group)
    c.execute(sql_form)
    return c.fetchall()

def form_7(c:Cursor,subject:str='History',name_group:str='Group-A'):
    """
    :param c: Database cursor object to execute SQL queries.
    :param subject: The subject to filter the grades, default is 'History'.
    :param name_group: The group name to filter students, default is 'Group-A'.
    :return: List of tuples containing students' first names, group names, grades, and subject names.
    """
    sql_form = '''Select Students.firstname, Groups.name_group, Grades.grade, Subjects.name
                  From Students
                  Join Groups on Students.group_id = Groups.id
                  Join Grades on Students.id = Grades.student_id
                  Join Subjects on Grades.subject_id = Subjects.id
                  Where Groups.name_group = '{}' and Subjects.name = '{}';
                  '''.format(name_group,subject)
    c.execute(sql_form)
    return c.fetchall()

def form_8(c:Cursor,teacher_name:str='James'):
    """
    :param c: Database cursor used to execute SQL queries.
    :param teacher_name: Name of the teacher whose average grade is to be found. Default is 'James'.
    :return: List of tuples containing the teacher's name and the average grade they have awarded.
    """
    sql_form = '''Select Teachers.firstname, avg(Grades.grade)
                  From Teachers
                  Join Subjects on Teachers.id = Subjects.teacher_id
                  Join Grades on Subjects.id = Grades.subject_id
                  Where Teachers.firstname ='{}'
                  Group by Teachers.firstname;
                  '''.format(teacher_name)
    c.execute(sql_form)
    return c.fetchall()

def form_9(c:Cursor,student_name:str='James'):
    """
    :param c: The database cursor used to execute SQL queries.
    :param student_name: The name of the student to find the list of courses for. Defaults to 'James'.
    :return: A list of tuples containing the student's last name and the subjects they are enrolled in.
    """
    sql_form = ''''
                Select Students.lastname, Subjects.name
                From Students
                Join Grades on Students.id = Grades.student_id
                Join Subjects on Grades.subject_id = Subjects.id
                Where Students.lastname = '{}'
                Group by Subjects.name;'''.format(student_name)
    c.execute(sql_form)
    return c.fetchall()

def form_10(c:Cursor,student_name:str='Julie',teacher_name:str='Timothy'):
    """
    :param c: Database connection cursor object
    :param student_name: Name of the student whose courses are being queried, defaults to 'Julie'
    :param teacher_name: Name of the teacher associated with the courses, defaults to 'Timothy'
    :return: List of courses attended by the student taught by the specific teacher
    """
    sql_form = '''
            Select Students.firstname, Subjects.name, Teachers.firstname
            From Students
            Join Grades on Students.id = Grades.student_id
            Join Subjects on Grades.subject_id = Subjects.id
            Join Teachers on Subjects.teacher_id = Teachers.id
            Where Students.firstname = '{}' and Teachers.firstname = '{}'
'''.format(student_name,teacher_name)
    c.execute(sql_form)
    return c.fetchall()

def print_result(rows):
    for row in rows:
        print(row)

def main():
    with MyConnection() as db:
        cursor = db.get_cursor()
        print_result(form_5(cursor))

if __name__ == '__main__':
   main()