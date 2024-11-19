
table = 'Students'
table_2 = 'Grades'
form_a = 'Select * from {}'.format(table)
avg_form = 'Select avg(grade) as average_grade From Grades'
form_b = 'Select firstname, lastname from {}'.format(table)



form_c = 'Select id, firstname, lastname from {} order by id DESC'.format(table) # ACS-DESC
form_d = 'Select id, firstname, lastname, group_id from {} Where group_id = {}'.format(table,3)
form_e = 'Select avg(id) as avg_id from {}'.format(table)
form_values = 'Select min(id) as min_id, max(id) as max_id from {}'.format(table)
form_count = 'Select count(id) as count_id, id from {} group by id'.format(table)
form_f = 'Select * from {} Where student_id In ( Select student_id from {} Where grade > 60 )'.format(table_2,table_2)

join_a = '''Select Students.firstname, Groups.name_group
            From Students
            Join Groups On Students.group_id = Groups.id'''

join_b = '''Select Students.firstname, Grades.grade
            From Students
            Join Grades On Students.id = Grades.student_id
            '''

join_c = '''Select Students.firstname, Subjects.name as subject_name, Grades.grade
            From Students
            Join Grades On Students.id = Grades.student_id
            Join Subjects On Grades.subject_id = Subjects.id
            Where Students.id = 1 And Subjects.name = 'History'; '''


join_d = '''Select Students.id, Students.firstname, avg(Grades.grade) as average_grade
            FROM Students 
            Join Grades On Students.id = Grades.student_id
            Group by Students.firstname 
            Order by average_grade DESC
            Limit 5;'''


join_e = '''Select Students.firstname, Subjects.name as subject_name, Grades.grade
            From Students
            Join Grades On Students.id = Grades.student_id
            Join Subjects On Grades.subject_id = Subjects.id
            Where Subjects.name = 'History'
            Group By Students.id
            Order by avg(Grades.grade) Desc
            Limit 1;'''

join_ee = '''Select Groups.name_group as group_name,
            (
                Select avg(grade)
                    From Grades
                    Join Subjects On Grades.subject_id = Subjects.id
                    Join Students On Students.id = Grades.student_id
                    Where Students.group_id = Groups.id and Subjects.name = 'History'
            ) as average_grade  
            From Groups;'''

join_f = '''Select Groups.name_group as group_name, avg(Grades.grade) as average_grade
               From Groups
               Join Students On Groups.id = Students.group_id
               Join Grades On Grades.student_id = Students.id
               Join Subjects On Grades.subject_id = Subjects.id
               Where Subjects.name = 'History'
               Group By Groups.id, Groups.name_group; 
               '''

form_1 = '''SELECT
               
                Students.firstname, 
                Students.lastname,
                AVG(GRADES.grade) AS average_grade
                
            FROM Students JOIN Grades ON Students.id = Grades.student_id    
              
            GROUP BY  Students.id, Students.lastname, Students.firstname
            ORDER BY  average_grade DESC, Students.lastname, Students.firstname;
               
            '''
form_2 = '''SELECT
                Students.id AS student_id,
                Students.firstname,
                Students.lastname,
                AVG(Grades.grade) AS average_grade
            
            FROM Grades 
                JOIN Students ON Grades.student_id = Students.id
                JOIN Subjects ON Grades.subject_id = Subjects.id
                
            WHERE Subjects.name = 'History'
            
            GROUP BY Students.id, Students.firstname,Students.lastname
            ORDER BY average_grade DESC
            
            LIMIT 1;
'''
