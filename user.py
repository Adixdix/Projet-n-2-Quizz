# Created by Lukas

import pymysql.cursors
from questions import Database
from users import Users
import hashlib
# from interrogation_BD import affiche_table

class User():
    def __init__(self, user, password):
        self.user = user
        temp = hashlib.new('sha256')
        temp.update(password.encode())
        self.password = temp.hexdigest()
    
    def verifies_password(self):
        '''Returns True if the username and password stated correspond
           to a user stored in the database'''
        return (self.user, self.password) in Users(self.user, self.password).get_users()
    
    
    
if __name__ == '__main__':
    print(User('Arcfayur', 'Aph3li0s').verifies_password())
    
