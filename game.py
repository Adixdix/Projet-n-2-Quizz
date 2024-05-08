import tkinter as tk
from tkinter import messagebox, ttk, Toplevel
from ttkbootstrap import Style
#from master_card_program import Master_card
#from Database import Database
#BY joshua LERAS IRIARTE

#MAIN BUG TO FIXE :
class Game(Toplevel):
    """Create a quizz with x questions and y players"""
    def __init__(self, nb_questions, master = None):
        super().__init__(master = master)
        #self.Card_Master = Master_card()²²²²²²
        self.Database_quizz = Database()
        self.microbit_answer = []
        self.n_series = []
        #test, waiting for those juicy SQL methods 
        self.nb_questions =  nb_questions
        self.current_question = 0
        self.score = 0
        self.players_list = []
        self.choice_btns = []
        self.quiz_data = self.Database_quizz.get_questions(self.nb_questions)
        #[{
        #"question": "What is the capital of France?",
        #"choices": ["Paris", "London", "Berlin", "Madrid"],
        #"answer": "Paris"
    #}]
        #Tkinter thingys
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
            print(self.choice_btns)
            self.choice_btns[i].config(text=choices[i], state="normal") # Reset button state

    # Clear the feedback label and disable the next button
        self.feedback_label.config(text="")
        self.next_btn.config(state="disabled")
    
    
    def check_answer(self,choice)->None:
        """Check if correct answer"""
        print(choice == int, choice == float)
    # Get the current question from the quiz_data list
        question = self.quiz_data[self.current_question]
        selected_choice = self.choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
        if selected_choice == question["answer"]:
        # Update the score and display it
            self.score += 1
            self.score_label.config(text="Score: {}/{}".format(self.score, len(self.quiz_data)))
            self.feedback_label.config(text="Correct!", foreground="green")
        else:
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
        
    def run(self)->None:
        """Run the quizz"""
        #Tkinter parameters
        self.window_parameters()
        
        self.define_style()
        
        self.qs_label.pack(pady=10)

# Create the choice buttons + microbit 
        for i in range(len(self.quiz_data[self.current_question]['choices'])):
            button = ttk.Button(
                self,
                command=lambda i=i: (self.check_answer(i))
            )
            button.pack(pady=5)
            self.choice_btns.append(button)
        
# Create the feedback label
        
        self.feedback_label.pack(pady=10)

# Initialize the score
        self.score = 0

# Create the score label
        print(self.quiz_data)
        self.score_label.pack(pady=10)

# Create the next button
        self.next_btn = ttk.Button(
            self,
            text="Next",
            command=lambda :self.next_question(),
            state="disabled"
        )
        self.next_btn.pack(pady=10)

# Initialize the current question index
        self.current_question = 0

# Show the first question
        self.show_question()
        
