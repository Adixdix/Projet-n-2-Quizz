import pygame
from menu import Menu

#Joshua LERAS IRIARTE 
class Game():
    def __init__ (self, game_on, player_response, question, reponse):
        self.in_menu = True
        self.menu = Menu("Super QUIZZ")
        self.button = self.menu.play_button
        
        self.game_on = True
        self.players_list = []
        self.player_response = ''
        self.question = ''
        self.response = []
        
    def run(self):
        """Run the game"""
        while self.game_on :
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.score.quit()
                if self.in_menu:
                    self.menu.update_menu(self.screen)
                    self.button.update(self.screen)
                    if self.menu.check_button_input():
                        self.in_menu = False
                else:
                    self.solo()

    def solo(self):
        question = #missing method (dict ex: {question:[answer1, answer2]} )
        #TODO
        
    def get_answer(self):
        #I NEED YOUR METHODS

    def set_playerid(self):
        #TODO

    def get_player(self):
        #TODO
        
        
                    
