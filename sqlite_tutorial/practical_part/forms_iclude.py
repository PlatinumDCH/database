name_groups = ['Group-A', 'Group-B', 'Group-C']
form_groups = 'INSERT INTO Groups (name_group) VALUES (?)'

form_students = 'INSERT INTO Students (firstname, lastname, enrollment, group_id) VALUES (?, ?, ?, ?)'
form_teachers = 'INSERT INTO Teachers (firstname, lastname) VALUES (?, ?)'
form_subject = 'INSERT INTO Subjects (name, teacher_id) VALUES (?, ?)'
form_grade = 'INSERT INTO Grades ( student_id, subject_id, grade, date_registered ) VALUES (?, ?, ?, ?)'
form_contact_student = 'INSERT INTO ContactsStudent(student_id, student_email, student_phone) VALUES (?, ?, ?)'
form_contact_teacher = 'INSERT INTO ContactsTeacher(teacher_id, teacher_email, teacher_phone) VALUES (?, ?, ?)'

