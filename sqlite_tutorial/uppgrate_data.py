from create import MyConnection
from data import update_data

update_param = (29, 'new_user')

if __name__ == '__main__':

    with MyConnection() as db:
        cursor = db.get_cursor()
        cursor.execute(update_data,update_param)
