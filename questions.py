# Created by Lukas 
import pymysql.cursors
class Database():
    def __init__(self):
        # Will connect to the database each time this class is accessed
        self.connection = pymysql.connect(host='localhost',
                                    user='root',
                                    # PASSWORD HIDDEN
                                    database='questions',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        
    def _add_question(self, label: str, question_type: str, difficulty: int, correct_answer: str, wrong1: str, wrong2: str, wrong3: str): 
        '''Adds a question in the database. It automatically updates both the "questions" and "answers" tables.'''        
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = "SELECT question_id FROM questions"
                cursor.execute(sql)
                result = cursor.fetchall()
                # Calculates the id of the question we're about to add
                next_id = result[-1]['question_id'] + 1
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO questions VALUES (" + str(next_id) + ",'" + label + "','"  + question_type + "'," + str(difficulty) + ");"
                cursor.execute(sql)
            self.connection.commit()
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO answers VALUES (" + str(next_id) + ",'" + correct_answer + "','" + wrong1 + "','"  + wrong2 + "','" + wrong3 + "');"
                cursor.execute(sql)

            self.connection.commit()


    def get_question(difficulty=None, theme=None):
        '''Returns a random question from the database
        in a dictionnary using the following structure :
        
        {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
        }'''
        # TODO


    def get_questions(n, difficulty=None, theme=None):
        '''Returns n questions from the database in a LIST of DICTIONNARIES
        using the same structure as the 'get_question' function'''
        list_of_questions = []
        # TODO
