import pygame
import random
from menu import Menu

#Joshua LERAS IRIARTE 
class Game():
    def __init__ (self, game_on, player_response, question, reponse):
        self.DATABASE = SGBD()
        self.MICROBIT = Carte_maitre()
        
        self.in_menu = True
        self.menu = Menu("Super QUIZZ")
        self.button = self.menu.play_button
        
        self.game_on = True
        self.question = self.DATABASE.get_question_answer()
        self.question_menu = Menu(str(self.question.keys()))
        self.in_question_menu = True
        self.nb_question = 10
        self.in_question = True
        self.timer = 10000 #10 sec
        
    def run(self):
        """Run the game"""
        while self.game_on :
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.score.quit()
                if self.in_menu:
                    self.menu_fonct()
                else:
                    self.question_series()

    def question_series(self):
        for i in range(nb_question):
            self.in_question = True
            self.timer = 10000 #10 sec
            while self.in_question :
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.score.quit()
                #TODO the display
                
    def menu_fonct(self):
        self.menu.update_menu(self.screen)
                    self.button.update(self.screen)
                    if self.menu.check_button_input():
                        self.in_menu = False
        
    def get_answer(self):
        return question.values()

    def set_playerid(self):
        return random.randint(1,100)

    def get_player(self):
        #TODO
        
        
                    
