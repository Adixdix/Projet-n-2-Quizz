import tkinter as tk
from tkinter import ttk, Toplevel
from ttkbootstrap import Style
from quizz_v3 import Game


class New_window(Toplevel):
     
    def __init__(self, root=None):
         
        super().__init__(root = root)
        self.title("New Window")
        self.geometry("200x200")

        
class Start():
    def __init__(self):
        self.root = tk.Tk()
        self.window_list = []
        self.player_list = []
        self.quizz_label = ttk.Label(
            self.root,
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
        )
        self.add_player = ttk.Button(
            self.root,
            text="Add player",
            command = lambda:self.choose_player(),
        )
    
    def create_child():
        child_window = tk.Toplevel(root)
        child_window.title("Owned by Main Window")
        child_window.transient(root)  # Set to be on top of the main window
        tk.Label(child_window, text="I'm a child owned by the main window").pack()
    
    def choose_player(self):
        self.player_list.append(1)
        self.player_number.config(text=f"{len(self.player_list)} players")
        
    def run(self):
        self.root.title("Quiz App")
        self.root.geometry("600x500")
        style = Style(theme="flatly")
        self.root.resizable(height = True, width = True)
        self.quizz_label.pack(pady=10)
        self.play_btn.pack(pady=5)
        self.add_player.pack(pady=5)
        self.player_number.pack(pady=5)
        
        style.configure("TLabel", font=("Helvetica", 20))
        style.configure("TButton", font=("Helvetica", 16))
        
        self.quizz_label.config(text="QUIZZ")
        self.play_btn.config(text="PLAY")
        self.add_player.config(text="ADD PLAYER")
        self.player_number.config(text=f"{len(self.player_list)} players")
        
        #self.play_btn.bind("<Button>", 
         #lambda x: Game(self.root))
        self.play_btn = ttk.Button(self.root,command=self.create_child()).pack()
        self.root.mainloop()
        
        
test = Start()
test.run()     
        