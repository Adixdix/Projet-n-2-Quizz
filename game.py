import tkinter as tk
from tkinter import messagebox, ttk, Toplevel
from ttkbootstrap import Style
from time import sleep
from master_card_program import Master_card
from Database import Database
#BY joshua LERAS IRIARTE

#MAIN BUG TO FIXE :
class Game(Toplevel):
    """Create a quizz with x questions and y players"""
    def __init__(self, nb_questions, nb_players = 0, microbits = None, master = None):
        super().__init__(master = master)
        
        self.microbits = microbits
        self.nb_questions =  nb_questions
        self.nb_players = nb_players 
        self.Database_quizz = Database()
        
        self.players_answer= {} #dict of player:answer(int)
        self.players_list = {}#dict of player:score
        self.choice_btns = [] #all buttons for the questions
        
        self.current_question = 0 #index 
        self.score = 0 #score in solo
        
        self.quiz_data = self.Database_quizz.get_questions(self.nb_questions)
        #[{
        #"question": "What is the capital of France?",
        #"choices": ["Paris", "London", "Berlin", "Madrid"],
        #"answer": "Paris"
    #}]
        #Tkinter label/buttons
        self.qs_label = ttk.Label(
            self,
            anchor="center",
            wraplength=500,
            padding=10
        )
        self.feedback_label = ttk.Label(
            self,
            anchor="center",
            padding=10
        )
        self.score_label = ttk.Label(
            self,
            text="Score: 0/{}".format(len(list(self.quiz_data))),
            anchor="center",
            padding=10
        )
        self.next_btn = ttk.Button(
            self,
            text="Next",
            state="disabled"
        )
        
        
    def show_question(self)->None:
        """Display the current question and the answer"""
    # Get the current question from the quiz_data list
        question = self.quiz_data[self.current_question]
        self.qs_label.config(text=str(question["question"])) #bug, overload to fix, pain in the ass

    # Display the choices on the buttons
        choices = question["choices"]
        for i in range(len(self.quiz_data[self.current_question]['choices'])):
            self.choice_btns[i].config(text=choices[i], state="normal") # Reset button state

    # Clear the feedback label and disable the next button
        self.feedback_label.config(text="")
        self.next_btn.config(state="disabled")
    
    
    def update_score(self, player_answered = None )->None:
        """Update the score"""
        
        #Will add +1 to the player who answered correctly
        if self.nb_players > 0:
            if len(self.players_list) == 0: #create the list of score if None exist
                for player in self.players_answer:
                    self.players_list[str(player)] = 0
            self.players_list[str(player_answered)] += 1
                
        else:
            #Add 1 and display the score if solo
            self.score += 1
            self.score_label.config(text="Score: {}/{}".format(self.score, len(self.quiz_data)))
        
            
    def check_answer(self, choice, player = None)->None:
        """Check if correct answer"""
    # Get the current question from the quiz_data list
        question = self.quiz_data[self.current_question]
        selected_choice = self.choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
        if selected_choice == question["answer"]:
        # Update the score and display it
            self.update_score(choice)
            if self.nb_players > 0:
                self.feedback_label.config(text="Correct!", foreground="green")
        else:
            if self.nb_players > 0:
                self.feedback_label.config(text="Incorrect!", foreground="red")
    
    # Disable all choice buttons and enable the next button
        for button in self.choice_btns:
            button.config(state="disabled")
        self.next_btn.config(state="normal")
    
    
    def next_question(self)->None:
        """Pass to the next question until the end"""
        self.current_question +=1

        if self.current_question < len(self.quiz_data):
        # If there are more questions, show the next question
            self.show_question()
        else:
        # If all questions have been answered, display the final score and end the quiz
            if self.nb_players > 0:
                mesage = ""
                for score in self.players_list: #Display all the scores in a row
                    message += f"{score} got {self.players_list[str(score)]}/{self.nb_questions} /n"
                    messagebox.showinfo("Quizz Completed",
                                        message).format()
            else:
                messagebox.showinfo("Quiz Completed",
                                    "Quiz Completed! Final score: {}/{}".format(self.score, len(self.quiz_data)))
            self.destroy()
        
    def window_parameters(self)->None:
        """Configure the main window parameters"""
        self.title("Quiz App")
        self.geometry("600x500")
        self.resizable(height = True, width = True)
        
    def define_style(self)->None:
        """Configure the font size for the question and choice buttons"""
        style = Style(theme="flatly")
        style.configure("TLabel", font=("Helvetica", 20))
        style.configure("TButton", font=("Helvetica", 16))
    
    def update_next_button(self)->None:
        """Update the next button to disabled"""
        self.next_btn = ttk.Button(
            self,
            text="Next",
            command=lambda :self.next_question(),
            state="disabled"
        )
        self.next_btn.pack(pady=10)
    
    def create_buttons(self)->None:
        """Create all buttons / can't interact in multiplayer"""
        for i in range(len(self.quiz_data[self.current_question]['choices'])):
            if self.nb_players > 0:
                button = ttk.Button(
                self,
                )
            else:
                button = ttk.Button(
                self,
                command=lambda i=i: (self.check_answer(i)),
                )
            
            button.pack(pady=5)
            self.choice_btns.append(button)
    
    def countdown(num_of_secs)->None:
        """Create a countdown of n seconds"""
        while num_of_secs:
            time.sleep(1)
            num_of_secs -= 1
        
    def run_solo(self)->None:
        """Run the quizz"""
        self.window_parameters()
        
        self.define_style()
        
        self.qs_label.pack(pady=10)
        
        self.create_buttons()
        
        if self.nb_players > 0:
            self.update_next_button()
        
# Initialize the current question index
            self.current_question = 0
        
# Show the first question
            self.show_question()
            
#wait for players to answer and verify their answers        
            self.players_answer = self.microbits.set_answer_mode()
        
        for player in self.players_answer:
            self.check_answer(self.players_answer[str(player), player])
            
        else:   
#Create the feedback label
            self.feedback_label.pack(pady=10)

# Initialize the score
            self.score = 0

# Create the score label
            self.score_label.pack(pady=10)

# Create the next button
            self.update_next_button()

# Initialize the current question index
            self.current_question = 0

# Show the first question
            self.show_question()
            
        
