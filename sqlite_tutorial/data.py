user_1:tuple
user_1 = ('new_user', 'newuser@example.com', 28)

sql_create_table:str
sql_create_table = '''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER)
'''

update_form:str = 'UPDATE Users SET age = ? WHERE username = ?'

query_form:str = 'INSERT INTO Users (username, email, age) VALUES (?, ?, ?)'

delete_form:str
delete_form = 'DELETE FROM Users WHERE username = ?'

select_form:str
select_form_all = 'SELECT * FROM Users'
select_form_age = 'SELECT username, age FROM Users WHERE age > ?'
select_form_avg = 'SELECT age, AVG(age) FROM Users GROUP BY age'
select_form_group = 'SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ?'# Фильтруем группы по среднему возрасту больше 30
select_from_avg_age = 'SELECT AVG(age) FROM Users'