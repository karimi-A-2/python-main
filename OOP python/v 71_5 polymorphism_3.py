# this is convention to I at first of interface name
class IUserService:
    def get_all_users(self): raise NotImplementedError
    def get_users_by_id(self): raise NotImplementedError
    def create_new_user(self): raise NotImplementedError


class UserServiceBySql(IUserService):
    def get_all_users(self):
        pass
    
    def get_users_by_id(self):
        pass
    
    def create_new_user(self):
        pass


user_service_by_sql = UserServiceBySql()
user_service_by_sql.get_all_users()
