import tkinter as tk
from tkinter import messagebox
from Questio_option import *

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("General Science Quiz Game")

        # Set a fixed window size
        self.root.geometry("900x255")  # Adjust the size as needed

        # Prevent the window from resizing
        self.root.pack_propagate(False)

        # Welcome message and rules
        self.welcome_label = tk.Label(root, text="Welcome to the General Science Quiz Game!", font=("Arial", 14))
        self.welcome_label.pack(pady=10)

        self.rules_label = tk.Label(root, text="Rules:\n1. There are 20 questions in total.\n2. Choose the correct answer by clicking the buttons below.\n3. Your score will be displayed at the end.", font=("Arial", 12))
        self.rules_label.pack(pady=10)

        # Start Quiz button
        self.start_button = tk.Button(root, text="Start Quiz", font=("Arial", 12), command=self.start_quiz)
        self.start_button.pack(pady=10)

        # Initialize other components
        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            option_button = tk.Button(root, text="", font=("Arial", 12), command=lambda i=i: self.check_answer(i))
            option_button.pack(pady=5)
            self.option_buttons.append(option_button)

        self.current_question = 0
        self.correct_guesses = 0
        self.incorrect_guesses = 0

        self.correct_answer_label = tk.Label(root, text="", font=("Arial", 12))
        self.correct_answer_label.pack(pady=5)
        self.correct_answer_label.pack_forget()

        self.answer_feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.answer_feedback_label.pack(pady=5)

        self.play_again_button = tk.Button(root, text="Play Again", font=("Arial", 12), command=self.restart_quiz)
        self.play_again_button.pack_forget()

    def start_quiz(self):
        # Hide welcome message, rules, and start button
        self.welcome_label.pack_forget()
        self.rules_label.pack_forget()
        self.start_button.pack_forget()

        # Load the first question
        self.load_question(self.current_question)


        self.load_question(self.current_question)

    def load_question(self, question_num):
        question = list(questions.keys())[question_num]
        options_text = options[question_num]

        self.question_label.config(text=question)
        for i in range(4):
            self.option_buttons[i].config(text=options_text[i])

    def check_answer(self, guess_index):
        guess = chr(97 + guess_index)  # Convert index to letter (a, b, c, d)
        correct_answer = questions[list(questions.keys())[self.current_question]]
        feedback_message = ""
        if guess == correct_answer:
            self.correct_guesses += 1
            feedback_message = "Correct!"
        else:
            self.incorrect_guesses += 1
            feedback_message = "Incorrect. The correct answer is: " + correct_answer
        self.answer_feedback_label.config(text=feedback_message)

        if self.current_question < len(questions) - 1:
            self.current_question += 1
            self.load_question(self.current_question)
        else:
            self.show_results()

    def show_results(self):
        score = int((self.correct_guesses / len(questions)) * 10)
        result_message = f"Your score is: {score}\nCorrect Answers: {self.correct_guesses}\nIncorrect Answers: {self.incorrect_guesses}"

        messagebox.showinfo("Results", result_message)

        # Show the "Play Again" button
        self.play_again_button.pack(pady=10)

    def restart_quiz(self):
        # Reset quiz state
        self.current_question = 0
        self.correct_guesses = 0

        # Hide the "Play Again" button
        self.play_again_button.pack_forget()

        # Load the first question
        self.load_question(self.current_question)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
