from create import MyConnection
from data import delete_form

del_param='new_user'

if __name__ == '__main__':
    with MyConnection() as db:
        cursor = db.get_cursor()
        #use tuple for parameters
        cursor.execute(delete_form, (del_param,))