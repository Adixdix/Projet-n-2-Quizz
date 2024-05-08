import tkinter as tk
from tkinter import ttk, Menu
from ttkbootstrap import Style
from quizz_v3 import Game
from master_card_program import Master_card
#BY JOSHUA LERAS IRIARTE

class Start():
    def __init__(self):
        self.root = tk.Tk()
        self.style = Style(theme="flatly")
        self.microbits = Master_card()
        self.window_list = []
        self.player_list = []
        self.nb_questions = 0 #default total questions
        self.quizz_label = ttk.Label(
            self.root, 
            text = "Quizz",
            anchor="center",  
            wraplength=500,
            padding=10
            )
        self.player_number = ttk.Label(
            self.root,
            anchor="center",
            wraplength=500,
            padding=10
            )
        self.label_nb_questions = ttk.Label(
            self.root,
            anchor="center",
            wraplength=500,
            padding=10
            )
        self.play_btn = ttk.Button(
            self.root,
            text = "PLAY",
            command = lambda: Game(self.microbits, self.nb_questions, self.root).run()
        )
        self.add_player = ttk.Button(
            self.root,
            text="ADD PLAYER",
            command = lambda: self.choose_player()
        )
    
    def choose_player(self)->None:
        """Add a single player to the game"""
        self.microbits.get_player()
        self.player_list.append(1)
        self.player_number.config(text=f"{len(self.player_list)} players")
    
    def position(self)->None:
        """Define the position of each label/button"""
        self.quizz_label.pack(pady=10)
        self.play_btn.pack(pady=5)
        self.add_player.pack(pady=5)
        self.player_number.pack(pady=5)
        self.label_nb_questions.pack(pady=5)
        
    def define_style(self)->None:
        """Define the font of the writings"""
        self.style.configure("TLabel", font=("Helvetica", 20))
        self.style.configure("TButton", font=("Helvetica", 16))
    
    def window_paramaters(self)->None:
        """Configure the main parameters of the window"""
        self.root.title("Quiz App")
        self.root.geometry("600x500")
        self.root.resizable(height = True, width = True)
    
    def questions_modifier(self, nb_modifier:int)->None:
        """Replace the total question numbers"""
        self.nb_questions = nb_modifier
        self.label_nb_questions.config(text=f"questions : {self.nb_questions}")
        print("questions:", self.nb_questions)
        
    def menu_quizz(self)->None:
        """Create the tab above the window"""
        #create menu
        menu_obj = Menu(self.root)
        
        #Add command to tab
        questions_menu = Menu(menu_obj, tearoff=0)
        
        for i in range(10):
            questions_menu.add_command(label =str(i+1), command =lambda i=i :self.questions_modifier(i+1))
        
        #Create each tab
        menu_obj.add_cascade(label ="questions", menu=questions_menu)
        
        #update
        self.root.config(menu = menu_obj)
        
    def run(self)->None:
        """Run the main menu"""
        self.window_paramaters()
        
        self.position()
        
        self.define_style()
        
        self.menu_quizz()
        
        self.player_number.config(text=f"{len(self.player_list)} players")
        self.label_nb_questions.config(text=f"questions : {self.nb_questions}")
        
        self.root.mainloop()
        
test = Start()
test.run()     
        
