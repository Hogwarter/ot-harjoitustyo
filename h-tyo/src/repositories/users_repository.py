from entities.user import User
from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection):
        self._connection = connection
        
    def get_username(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        return [ row["Username"] for row in rows]
    
    def create_new_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute("insert into users (username, password) values (?, ?)",
            (user.username, user.password))
        self._connection.commit()
        return user
    
    
    

user_repository = UserRepository(get_database_connection())
        
        
    
    
    
    
    
    
    
    