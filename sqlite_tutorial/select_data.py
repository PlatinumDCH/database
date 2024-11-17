from create import MyConnection
from data import select_form_age, select_form_avg
from data import select_form_group
from data import select_from_avg_age

def print_all(poll:list[tuple]):
    for user in poll:
        print(user)

def fetch_users_by_age(age:int)->None:
    """print all users with age >=25"""
    with MyConnection() as db:
        users:list[tuple] = db.execute_query(select_form_age, (age,))
        print_all(users)

def fetch_users_values()->None:
    with MyConnection() as db:
        users:list[tuple] = db.execute_query(select_form_avg)
        print_all(users)

def fetch_grouped_users(age:int)->None:
    with MyConnection() as db:
        users:list[tuple] = db.execute_query(select_form_group, (age,))

def get_avg_age()->None:
    with MyConnection() as db:
        users:list[tuple] = db.execute_query(select_from_avg_age)
        print(users)
        print_all(users)

if __name__ == '__main__':
    get_avg_age()
