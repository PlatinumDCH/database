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

update_data:str = 'UPDATE Users SET age = ? WHERE username = ?'

query_insert:str = 'INSERT INTO Users (username, email, age) VALUES (?, ?, ?)'

delete_form:str
delete_form = 'DELETE FROM Users WHERE username = ?'

select_form:str
select_form = 'SELECT * FROM Users'