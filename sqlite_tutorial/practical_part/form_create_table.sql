-- table Students
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    enrollment TEXT NOT NULL,
    group_id INTEGER NOT NULL,
    FOREIGN KEY (group_id) REFERENCES Groups (id)
);

-- table groups
CREATE TABLE IF NOT EXISTS Groups (
    id INTEGER PRIMARY KEY,
    name_group TEXT NOT NULL
);

-- table Teachers
CREATE TABLE IF NOT EXISTS Teachers (
    id INTEGER PRIMARY KEY,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL
);

-- table Subjects
CREATE TABLE IF NOT EXISTS Subjects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    teacher_id INTEGER NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(id)
);

-- table Grades
CREATE TABLE IF NOT EXISTS Grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER NOT NULL,
    date_registered TEXT NOT NULL, -- format YYYY-MM-DD
    FOREIGN KEY (student_id) REFERENCES Students(id),
    FOREIGN KEY (subject_id) REFERENCES Subjects(id)
);

-- table ContactsStudent
CREATE TABLE IF NOT EXISTS ContactsStudent (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    student_email TEXT,
    student_phone TEXT,
    FOREIGN KEY (student_id) REFERENCES Students(id)
);

-- table ContactsTeacher
CREATE TABLE IF NOT EXISTS ContactsTeacher (
    id INTEGER PRIMARY KEY,
    teacher_id INTEGER,
    teacher_email TEXT,
    teacher_phone TEXT,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(id)
);