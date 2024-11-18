SELECT, FROM, WHERE, GROUP BY, HAVING и ORDER BY
DELETE
UPDATE


fetchall - all objects
fetchmany - one object
fetchmany(size) - size pack objects

COUNT |SELECT COUNT(*) FROM Users
SUM |SELECT SUM(age) FROM Users
AVG |SELECT AVG(age) FROM Users
MIN |SELECT MIN(age) FROM Users
MAX |SELECT MAX(age) FROM Users

exemple difficult query:

    SELECT username, age
    FROM Users
    WHERE age = (SELECT MAX(age) FROM Users)

convert in dict:

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
