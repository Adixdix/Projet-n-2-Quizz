import tkinter as tk
from tkinter import ttk, Toplevel
from ttkbootstrap import Style
from quizz_v3 import Game

        
class Start():
    def __init__(self):
        self.root = tk.Tk()
        self.style = Style(theme="flatly")
        self.window_list = []
        self.player_list = []
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
        self.play_btn = ttk.Button(
            self.root,
            text = "PLAY",
            command = lambda: Game(self.root)
        )
        self.add_player = ttk.Button(
            self.root,
            text="ADD PLAYER",
            command = lambda: self.choose_player()
        )
    
    def choose_player(self)->None:
        """Add a single player to the game"""
        self.player_list.append(1)
        self.player_number.config(text=f"{len(self.player_list)} players")
    
    def position(self)->None:
        """Define the position of each label/button"""
        self.quizz_label.pack(pady=10)
        self.play_btn.pack(pady=5)
        self.add_player.pack(pady=5)
        self.player_number.pack(pady=5)
        
    def define_style(self)->None:
        """Define the font of the writings"""
        self.style.configure("TLabel", font=("Helvetica", 20))
        self.style.configure("TButton", font=("Helvetica", 16))
    
    def window_paramaters(self)->None:
        """Configure the main parameters of the window"""
        self.root.title("Quiz App")
        self.root.geometry("600x500")
        self.root.resizable(height = True, width = True)
        
    def run(self)->None:
        self.window_paramaters()
        
        self.position()
        
        self.define_style()
        
        self.player_number.config(text=f"{len(self.player_list)} players")
        
        self.root.mainloop()
        
        
test = Start()
test.run()     
        
