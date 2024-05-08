# Created by Lukas

import pymysql.cursors
from random import randint, sample
# from interrogation_BD import affiche_table

class Database():
    def __init__(self):
        # Will connect to the database each time this class is accessed
        self.connection = pymysql.connect(host='nsijoliotcurie.fr',
                                    user='admin_user_Quiz2024',
                                    password=####HIDDEN#####,
                                    database='admin_Quiz2024',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        
    def _add_question(self, label: str, question_type: str, difficulty: int, correct_answer: str, wrong1: str, wrong2: str, wrong3: str) -> None: 
        '''Adds a question in the database. It automatically updates both the "questions" and "answers" tables.'''        
        with self.connection:
            # All the following commands will require an individual connection
            # so that previous changes can be saved even if an exception occurs
            with self.connection.cursor() as cursor:
                sql = "SELECT question_id FROM questions"
                cursor.execute(sql)
                result = cursor.fetchall()
                # Calculates the id of the question we're about to add
                next_id = result[-1]['question_id'] + 1
            with self.connection.cursor() as cursor:
                # Adds the values in the "questions" table
                sql = "INSERT INTO questions VALUES (" + str(next_id) + ",'" + label + "','"  + question_type + "'," + str(difficulty) + ");"
                cursor.execute(sql)
            self.connection.commit()
            print('Successfully updated the QUESTIONS table.')
            with self.connection.cursor() as cursor:
                # Adds the values in the "answers" table
                sql = "INSERT INTO answers VALUES (" + str(next_id) + ",'" + correct_answer + "','" + wrong1 + "','"  + wrong2 + "','" + wrong3 + "');"
                cursor.execute(sql)
            self.connection.commit()
            print('Successfully updated the ANSWERS table.')


    def get_question(self, question_id: int = None, difficulty: int = '', theme: str = '') -> dict:
        '''Returns a question from the database (random if id not
        specified) in a dictionnary using the following structure :
        
        {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
        }'''
        with self.connection:
            dictionnary = {}
            with self.connection.cursor() as cursor:
                if question_id is None:
                    # Gets a random question_id from the database
                    sql = "SELECT COUNT(question_id) AS 'reponse' FROM questions"
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    question_id = randint(1, result['reponse'])
                    
                # Gets the question_label corresponding to the question_id chosen by the randint function
                sql = "SELECT question_label AS 'question' FROM questions WHERE question_id =" + str(question_id)
                cursor.execute(sql)
                # Adds the result to the final dictionnary
                dictionnary['question'] = cursor.fetchone()['question']
                
                # Gets all the answers in a list and shuffles all the possible answers
                sql = "SELECT correct_answer, wrong_answer_1, wrong_answer_2, wrong_answer_3 FROM answers WHERE question_id =" + str(question_id)
                cursor.execute(sql)
                result = cursor.fetchone()
                # Adds the shuffled list in the final dictionnary
                dictionnary['choices'] = sample(list(result.values()), 4)
                # Adds the correct answer in the final dictionnary with a different key
                dictionnary['answer'] = result['correct_answer']
                
        return dictionnary
                           

    def get_questions(self, n: int, difficulty: int = '', theme:str = '') -> list:
        '''Returns n random questions from the database in a LIST of DICTIONNARIES
        using the same structure as the 'get_question' method'''
        list_of_questions = []
        with self.connection:
            with self.connection.cursor() as cursor:
                
                if difficulty != '':
                    difficulty = "WHERE difficulty =" + str(difficulty)
                if theme != '':
                    if difficulty != '':
                        theme = " AND question_type = '" + str(theme) + "'"
                    else:
                        theme = "WHERE question_type ='" + str(theme) + "'"
                
                # Counts the amount of ids stored in the database
                sql = "SELECT COUNT(question_id) AS 'count' FROM questions " + difficulty + theme
                cursor.execute(sql)
                result = cursor.fetchone()['count']
                
            
            if difficulty == '' and theme == '':   
                # The following variable will basically contain a shuffled list of n integers that will refer to the questions' ids
                list_ids = sample(list(range(1, result+1)), result)[:n]
            else:
                with self.connection.cursor() as cursor:
                    sql = "SELECT question_id FROM questions " + difficulty + theme
                    cursor.execute(sql)
                    list_ids = cursor.fetchall()
                    for i in range(len(list_ids)):
                        list_ids[i] = list_ids[i]['question_id']
                    print(list_ids := sample(list_ids, len(list_ids))[:n])
            if len(list_ids) < n:
                # Raises an exception if the number of questions asked is greater than the number of questions in the database
                raise ValueError('You asked for too many questions compared to the amount of ones available in the database')
            # For each id in our shuffled list of ids, we call the previous method to fill our soon-to-be returned
            # list with its label and answers
            for element in list_ids:
                list_of_questions.append(Database().get_question(element, difficulty, theme))
            return list_of_questions
    
    
# TESTS    
if __name__ == '__main__':        
    for i in range(2):
        affiche_table(Database().get_questions(5))
        affiche_table(Database().get_questions(2, 2))
        affiche_table(Database().get_questions(3, '', 'Histoire'))
        affiche_table(Database().get_questions(1, 1, 'Maths'))
    
