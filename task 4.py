import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

class RockPaperScissorsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0
        
        self.user_choice_label = tk.Label(master, text="Your choice:")
        self.user_choice_label.grid(row=0, column=0, padx=5, pady=5)

        self.user_choice_var = tk.StringVar()
        self.user_choice_entry = tk.Entry(master, textvariable=self.user_choice_var, width=20)
        self.user_choice_entry.grid(row=0, column=1, padx=5, pady=5)

        self.play_button = tk.Button(master, text="Play", command=self.play)
        self.play_button.grid(row=0, column=2, padx=5, pady=5)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.computer_choice_label = tk.Label(master, text="")
        self.computer_choice_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        self.scores_label = tk.Label(master, text="Scores - You: 0  Computer: 0")
        self.scores_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        self.play_again_button = tk.Button(master, text="Play Again", command=self.play_again)
        self.play_again_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
        self.play_again_button.grid_remove()

    def play(self):
        user_choice = self.user_choice_var.get().lower()
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            messagebox.showerror("Error", "Invalid choice. Please choose rock, paper, or scissors.")
            return
        
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        self.computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        
        self.result_label.config(text=result)
        
        if result == "You win!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1
        
        if result != "Draw":
            self.scores_label.config(text=f"Scores - You: {self.user_score}  Computer: {self.computer_score}")
        
        self.play_button.grid_remove()
        self.play_again_button.grid()

    def play_again(self):
        self.user_choice_var.set("")
        self.result_label.config(text="")
        self.computer_choice_label.config(text="")
        
        self.play_again_button.grid_remove()
        self.play_button.grid()
    
root = tk.Tk()
app = RockPaperScissorsApp(root)
root.mainloop()
