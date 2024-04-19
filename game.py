import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style

class Game():
    def __init__(self):
        #test, waiting for those juicy SQL methods
        self.quiz_data = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["Jupiter", "Saturn", "Mars", "Earth"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["Go", "Au", "Ag", "Gd"],
        "answer": "Au"
    },
    {
        "question": "Which country is known as the 'Land of the Rising Sun'?",
        "choices": ["China", "Japan", "South Korea", "Thailand"],
        "answer": "Japan"
    }

]
        #Tkinter thingys
        self.root = tk.Tk()
        self.current_question = 0
        self.score = 0
        self.choice_btns = []
        self.qs_label = ttk.Label(
            self.root,
            anchor="center",
            wraplength=500,
            padding=10
        )
        self.feedback_label = ttk.Label(
            self.root,
            anchor="center",
            padding=10
        )
        self.score_label = ttk.Label(
            self.root,
            text="Score: 0/{}".format(len(list(self.quiz_data))),
            anchor="center",
            padding=10
        )
        self.next_btn = ttk.Button(
            self.root,
            text="Next",
            state="disabled"
        )
        
        
    def show_question(self):
    # Get the current question from the quiz_data list
        question = self.quiz_data[self.current_question]
        self.qs_label.config(text=str(question["question"])) #bug, overload to fix, pain in the ass

    # Display the choices on the buttons
        choices = question["choices"]
        for i in range(4):
            print(self.choice_btns)
            self.choice_btns[i].config(text=choices[i], state="normal") # Reset button state

    # Clear the feedback label and disable the next button
        self.feedback_label.config(text="")
        self.next_btn.config(state="disabled")
    
    
    def check_answer(self,choice):
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
    
    
    def next_question(self):
        self.current_question +=1

        if self.current_question < len(self.quiz_data):
        # If there are more questions, show the next question
            self.show_question()
        else:
        # If all questions have been answered, display the final score and end the quiz
            messagebox.showinfo("Quiz Completed",
                                "Quiz Completed! Final score: {}/{}".format(self.score, len(self.quiz_data)))
            self.root.destroy()
            
            
    def run(self):
        print(self.quiz_data)
        self.root.title("Quiz App")
        self.root.geometry("600x500")
        style = Style(theme="flatly")

        self.qs_label.pack(pady=10)
# Configure the font size for the question and choice buttons
        style.configure("TLabel", font=("Helvetica", 20))
        style.configure("TButton", font=("Helvetica", 16))

# Create the choice buttons
        for i in range(4):
            button = ttk.Button(
                self.root,
                command=lambda i=i: (self.check_answer(i))
            )
            button.pack(pady=5)
            self.choice_btns.append(button)
        print(self.choice_btns)

# Create the feedback label
        
        self.feedback_label.pack(pady=10)

# Initialize the score
        self.score = 0

# Create the score label
        print(self.quiz_data)
        self.score_label.pack(pady=10)

# Create the next button
        self.next_btn = ttk.Button(
            self.root,
            text="Next",
            command=self.next_question(),
            state="disabled"
        )
        self.next_btn.pack(pady=10)

# Initialize the current question index
        self.current_question = 0

# Show the first question
        self.show_question()

# Start the main event loop
        self.root.mainloop()
game = Game()
game.run()
