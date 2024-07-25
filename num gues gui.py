import random
import tkinter as tk
from tkinter import messagebox


class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("400x300")
        self.master.configure(bg='pink')  # Set the main window background to pink
        self.center_window()  # Center the window

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master, bg='white')  # Set background to white
        self.entry.pack(pady=5)
        self.entry.focus()
        self.entry.bind('<Return>', self.check_guess)

        self.submit_button = tk.Button(self.master, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=5)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=5)

        self.new_game_button = tk.Button(self.master, text="New Game", command=self.new_game)
        self.new_game_button.pack(pady=5)

    def center_window(self):
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()
            x = (screen_width // 2) - (400 // 2)
            y = (screen_height // 2) - (300 // 2)
            self.master.geometry(f'400x300+{x}+{y}')

    def check_guess(self, event=None):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.secret_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.secret_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts!")
                self.new_game()

        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

        self.entry.delete(0, tk.END)

    def new_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)
        self.entry.focus()


def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()