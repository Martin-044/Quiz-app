import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
import random
import pygame  # Import pygame for audio

class SpellingQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fun Spelling quiz")
        self.root.geometry("450x500")
        self.root.config(bg="#59897E")  # background for bright contrast and focus

        # Initialize pygame mixer for audio
        pygame.mixer.init()
        
        # Load background music 
        self.background_music = "background_music.mp3"
        pygame.mixer.music.load(self.background_music)
        
        # Define the questions, answers, and choices
        self.all_questions = [
            {
                "definition": "A person who writes books, articles, or other written works.",
                "correct_answer": "author",
                "options": ["author", "auther", "othor", "autur"]
            },
            {
                "definition": "A machine that is used for printing documents.",
                "correct_answer": "printer",
                "options": ["printer", "printrer", "printter", "priter"]
            },
            {
                "definition": "The ability to do something well or to achieve a desired result.",
                "correct_answer": "skill",
                "options": ["skill", "skil", "skille", "skilz"]
            },
            {
                "definition": "A type of weather where there is little to no sunlight and it is cloudy or foggy.",
                "correct_answer": "overcast",
                "options": ["overcast", "overcastt", "ovrcast", "overkast"]
            },
            {
                "definition": "A feeling of extreme happiness or joy.",
                "correct_answer": "ecstasy",
                "options": ["ecstasy", "extacy", "exstacy", "ecstacy"]
            }
        ]

        self.reset_quiz()

        # Define fonts for a friendly look
        self.title_font = Font(family="Comic Sans MS", size=20, weight="bold")
        self.button_font = Font(family="Comic Sans MS", size=14)
        self.score_font = Font(family="Comic Sans MS", size=16, weight="bold")

        # Create UI elements
        self.title_label = tk.Label(self.root, text="Fun Spelling Quiz!", font=self.title_font, bg="#37DBB5", fg="#3D5AFE")
        self.title_label.pack(pady=20)

        self.definition_label = tk.Label(self.root, text="", wraplength=350, font=self.title_font, bg="#37DBB5")
        self.definition_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", font=self.button_font, width=20, height=2, bg="#37DBB5", fg="white", command=lambda i=i: self.check_answer(i))
            button.pack(pady=10)
            self.option_buttons.append(button)

        self.score_label = tk.Label(self.root, text="Score: 0/5", font=self.score_font, bg="#37DBB5", fg="#3D5AFE")
        self.score_label.pack(pady=20)

        # Start the first question
        self.load_question()

    def reset_quiz(self):
        # Shuffle the questions every time the quiz is restarted
        self.questions = random.sample(self.all_questions, len(self.all_questions))
        self.score = 0
        self.current_question = 0

    def load_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.definition_label.config(text=question["definition"])
            for i, option in enumerate(question["options"]):
                self.option_buttons[i].config(text=option)
        else:
            self.show_end_screen()

    def check_answer(self, selected_index):
        question = self.questions[self.current_question]
        
        if question["options"][selected_index] == question["correct_answer"]:
            self.score += 1
            messagebox.showinfo("Correct!", "Great job! You're doing awesome!")
        else:
            messagebox.showerror("Oops!", f"The correct spelling is: {question['correct_answer']}")

        # Move to the next question
        self.current_question += 1

        # Update score label
        self.score_label.config(text=f"Score: {self.score}/{len(self.questions)}")

        # Load the next question or show the end screen if quiz is over
        self.load_question()

    def show_end_screen(self):
        messagebox.showinfo("Quiz Over", f"Your final score is: {self.score}/{len(self.questions)}")
        
        # Hide quiz UI elements
        for widget in self.root.winfo_children():
            widget.pack_forget()

        # Show end screen with the final score and play again button
        end_title = tk.Label(self.root, text="Congratulations!", font=self.title_font, bg="#37DBB5", fg="#3D5AFE")
        end_title.pack(pady=20)

        final_score_label = tk.Label(self.root, text=f"Your Score: {self.score}/{len(self.questions)}", font=self.score_font, bg="#37DBB5", fg="#3D5AFE")
        final_score_label.pack(pady=20)

        play_again_button = tk.Button(self.root, text="Play Again", font=self.button_font, bg="#37DBB5", fg="white", width=20, height=2, command=self.restart_quiz)
        play_again_button.pack(pady=20)

        # Stop the background music when quiz ends
        pygame.mixer.music.stop()

    def restart_quiz(self):
        # Reset the quiz and show the questions again
        self.reset_quiz()

        # Hide end screen elements
        for widget in self.root.winfo_children():
            widget.pack_forget()

        # Show quiz UI elements again
        self.title_label.pack(pady=20)
        self.definition_label.pack(pady=20)
        for button in self.option_buttons:
            button.pack(pady=10)
        self.score_label.pack(pady=20)

        # Reload the first question
        self.load_question()

        # Restart the background music when quiz restarts
        pygame.mixer.music.play(-1, 0.0)  # Loop the music indefinitely

if __name__ == "__main__":
    root = tk.Tk()
    app = SpellingQuizApp(root)
    # Start playing background music when the app starts
    pygame.mixer.music.play(-1, 0.0)  # Loop the music indefinitely
    root.mainloop()
