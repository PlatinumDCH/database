SELECT, FROM, WHERE, HAVING и 
DELETE
UPDATE
GROUP BY

fetchall - all objects
fetchmany - one object
fetchmany(size) - size pack objects

---aggregate---functions------

    COUNT |SELECT COUNT(*) FROM Users
    SUM   |SELECT SUM(age) FROM Users
    AVG   |SELECT AVG(age) FROM Users
    MIN   |SELECT MIN(age) FROM Users
    MAX   |SELECT MAX(age) FROM Users


--clean--Select---

    SELECT track_id, name, composer,unit_price
    FROM tracks;
	
	Select * From tracks;
    
    SELECT DISTINCT	select_list  - убирает дубликаты 
    FROM table;

--Order by - sorting columns --- 

    SELECT select_list
    FROM table
    ORDER BY 
        column_1 ASC, --восходящий
        column_2 DESC; --нисходящий
    
    SELECT name, milliseconds, albumid
    FROM tracks
    ORDER BY albumid, milliseconds;
    сначала строки сортируются по столбцу albumid в порядке возрастания
    затем строки с одинаковыми значениями в столбце albumid сортируются по столбце milliseconds
    

---Where---

    Select column_list
    From table
    Where search_condition;       <left_expression COMPARISON_OPERATOR right_expression>
                            WHERE      column_1             =                100;
                            WHERE      column_2            IN              (1,2,3);
                            WHERE      column_3           LIKE              'An%';
                            WHERE      column_4          BETWEEN          10 AND 20;
    
    SELECT name,milliseconds, bytes,albumid
    FROM   tracks
    WHERE  albumid = 1;
    
    SELECT  name,milliseconds, bytes,albumid
    FROM tracks
    WHERE albumid = 1 AND milliseconds > 250000;
    
    SELECT name,albumid,composer
    From tracks
    Where composer Liker '%Smith%'
    Order by albumid;
    
    SELECT BillingAddress, BillingCity, Total
    FROM invoices
    WHERE BillingCity = 'New York' AND Total > 5
    ORDER BY Total;

    SELECT BillingAddress, BillingCity, Total
    FROM invoices
    WHERE Total > 5 AND (BillingCity = 'New York' OR BillingCity = 'Chicago')
    ORDER BY Total;

    SELECT username, age
    FROM Users
    WHERE age = (SELECT MAX(age) FROM Users)

--Limit-- ограничения количества строк
    
    Select culumn_list
    From table
    Limin row_count:int;
    
    Select culumn_list
    From table
    Limit offset:int, row_count:int;

--Like--Glob--
Glob - чувствителен к регистру
    
    Select traking, name
    From tracks
    Where name Glob 'Man*';  находит треки, названия которых начинаются со строки Man
    Where name Glob '*Man'; находит треки, названия которых заканчиваются строкой Man
    Where name Glob '?ere*'; находит треки, которые начинаются с любого символа за которым следуем ere, далее любое количество символов
    Where name Glob '*[0-9]*' найти треки в которых есть числа
    Where name GLOB '*[^1-9]*'; найти треки в названии которых нету цифр
    Where name GLOB '*[1-9]'; найти треки название которых заканчивается на цифру

--Join---
    
    Select Title, Name
    From alnums
    Join artists on artists.ArtistId = albums.AtrtistId;

    SELECT l.Title, r.Name
    From albums as l
    Join artists as r on r.ArtistId  = l.ArtistId;
    convert in dict:
    
    SELECT a.Title, ar.Name
    From albums as a
    Join artists as ar Using(ArtistID)
    
    Select  title, name
    from artists 
    left join albums on artists.ArtistId = albums.ArtistId
    where title is null

    #обединит все колонки с дух таблиц
    Select fill
    from table1
    cross join table2

    cursor.execute(SELECT * FROM Users)
    users = cursor.fetchall()
    
    user_list = []
    for use in users:
        user_dict = {
            id: user[0],
            username: user[1],
            email: user[2],
            age: user[3]}
        }
        user_list.append(user_dict)

NULL |SELECT * FROM Users WHERE age IS NULL
NULL First - поля в который будет значения NULL будут показаны в начале 
NuLL Last - поля в который будет значения NULL будут показаны в конце

BEGIN COMMIT ROLLBACK:
    
    try:
        cursor.execute('BEGIN')
        cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user1', 'user1@example.com'))
        cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user2', 'user2@example.com'))
        cursor.execute('COMMIT')
    except:
        cursor.execute('ROLLBACK')

with constructions:

    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()
        try:
           with connection: 
                cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user3', 'user3@example.com'))
                cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user4', 'user4@example.com'))
        except:
            # Ошибки будут приводить к автоматическому откату транзакции
            pass

--created_table

    CREATE TABLE students (
        student_id INTEGER PRIMARY KEY,
        student_name TEXT NOT NULL
    );
    
    CREATE TABLE courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL
    );
    
    CREATE TABLE enrollments (
        enrollment_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY(student_id) REFERENCES students(student_id),
        FOREIGN KEY(course_id) REFERENCES courses(course_id)
    );

--fill_table

     INSERT INTO students (student_name)
     VALUES   ('John'), ('Jane'), ('Doe'),('Alice'),('Bob');

     INSERT INTO courses (course_name)
     VALUES ('Math'),('Science'),('History');

     INSERT INTO enrollments (student_id, course_id)
     VALUES  (1, 1),(2, 2),(3, 3),(4, NULL),(NULL, 3);
      

--select students

    select students.studentname, courses.coursename 
    from students 
    full join enrollments on students.studentid = enrollments.student_id
    full join courses on enrollments.course_id = courses.coursei