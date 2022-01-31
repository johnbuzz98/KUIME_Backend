from flask_login import UserMixin
from config.flask_config import CRUD

class User(UserMixin):

    def __init__(self, user_id):
        self.user_id = user_id

    def get_id(self):
        return str(self.user_id)

    @staticmethod
    def get_user_info(user_id, user_pw=None):
        result = dict()
        try:
            sql = f"SELECT customer_id, customer_name, phone FROM Customer"
            if user_pw:
                sql += f"WHERE customer_id = '{user_id}' AND password = '{user_pw}'; "
            else:
                sql += f"WHERE customer_id = '{user_id}'; "

            result = CRUD.readDB(sql)

        except:
            result['result'] = 'fail'
            result['data'] = 'fail'

        finally:
            return result