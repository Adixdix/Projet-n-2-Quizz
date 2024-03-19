import pygame
#Joshua LERAS IRIARTE 
class Game():
    def __init__ (game_on, player_response, question, reponse):
        self.in_menu = True
        self.menu = Menu("Super QUIZZ")
        self.button = self.menu.play_button
        
        self.game_on = True
        self.players_list = []
        self.player_response = ''
        self.question = ''
        self.response = []
    
    def get_question(self):
        """Get the question from the database"""
        #TODO
        
    def get_response(self):
        """Get the response from the question in the database"""
        #TODO
        
    def get_player_response(self):
        """Get the response from the player at the main microbit"""
        #TODO

    def update_playerlist(self):
        """Update the number of players"""
        #TODO
        
    def run(self):
        """Run the game"""
        while game_on :
            if self.in_menu:
                self.menu.update_menu(self.screen)
                self.button.update(self.screen)
                if self.menu.check_button_input():
                    self.in_menu = False
