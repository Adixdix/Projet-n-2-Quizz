# Created by Lukas

import pymysql.cursors
from questions import Database
# from interrogation_BD import affiche_table
import hashlib

class Users():
    def __init__(self, user, password):
        self.user = user
        # Stores the hashed version of the password
        temp = hashlib.new('sha256')
        temp.update(password.encode())
        self.password = temp.hexdigest()
        self.connection = pymysql.connect(host='nsijoliotcurie.fr',
                                    user='admin_user_Quiz2024',
                                    password=###HIDDEN###,
                                    database='admin_Quiz2024',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

    def get_users(self):
        '''Will return all users in the database in a list of tuples'''
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = "SELECT username, password FROM users"
                cursor.execute(sql)
                result = cursor.fetchall()
                final_list = []
                # Basically converts the list of dictionnaries as a list of tuples
                for element in result:
                    final_list.append((element['username'], element['password']))
                return final_list
            
    
    def _get_next_id(self):
        '''Returns an id that isn't already in the database'''
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = "SELECT COUNT(user_id) AS 'count' FROM users"
                cursor.execute(sql)
                result = cursor.fetchone()
                # Each user will have the id of the previous one + 1
                return result['count'] + 1
                
        
    def _add_user(self):
        '''Will add the specified user when calling the class if they are not in the database'''
        if (self.user, self.password) not in self.get_users():
            next_id = Users(self.user, self.password)._get_next_id()
            # Requires another connection to the database as the previous one has been closed
            self.connection = pymysql.connect(host='nsijoliotcurie.fr',
                                        user='admin_user_Quiz2024',
                                        password='Uy0*9za59)C3',
                                        database='admin_Quiz2024',
                                        charset='utf8mb4',
                                        cursorclass=pymysql.cursors.DictCursor)
            with self.connection:
                with self.connection.cursor() as cursor:
                    sql = f"INSERT INTO users VALUES ({str(next_id)},'{self.user}','{self.password}')"
                    cursor.execute(sql)
                self.connection.commit()
            print("Successfully updated the USERS table.")
        else:
            # Raises the following exception in order to not add the same user twice (or more)
            raise NameError('The specified username and password already exist in the database.')
                
        
        
if __name__ == '__main__':
    Users('Arcfayur', 'Aph3li0s')._add_user()
