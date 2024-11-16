import random
import tkinter as tk
from tkinter import messagebox

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.word_list = ["python", "programming", "hangman", "challenge", "developer"]
        self.word = random.choice(self.word_list)
        self.guessed_word = ["_"] * len(self.word)
        self.attempts_left = 6
        self.guessed_letters = set()

        # UI Elements
        self.word_label = tk.Label(root, text=" ".join(self.guessed_word), font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.input_label = tk.Label(root, text="Enter your guess (a single letter):", font=("Arial", 14))
        self.input_label.pack()

        self.letter_entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.letter_entry.pack(pady=10)

        self.guess_button = tk.Button(root, text="Guess", font=("Arial", 14), command=self.make_guess)
        self.guess_button.pack(pady=10)

        self.info_label = tk.Label(root, text=f"Attempts left: {self.attempts_left}", font=("Arial", 14))
        self.info_label.pack(pady=10)

        self.guessed_letters_label = tk.Label(root, text="Guessed letters: None", font=("Arial", 14))
        self.guessed_letters_label.pack(pady=10)

    def make_guess(self):
        guess = self.letter_entry.get().lower()
        self.letter_entry.delete(0, tk.END)  # Clear the input field

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Invalid Input", "Please enter a single alphabet.")
            return
        if guess in self.guessed_letters:
            messagebox.showwarning("Duplicate Guess", f"You already guessed '{guess}'.")
            return

        self.guessed_letters.add(guess)

        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.guessed_word[i] = guess
            self.word_label.config(text=" ".join(self.guessed_word))
            if "_" not in self.guessed_word:
                messagebox.showinfo("Congratulations!", f"You guessed the word: {self.word}!")
                self.reset_game()
        else:
            self.attempts_left -= 1
            self.info_label.config(text=f"Attempts left: {self.attempts_left}")
            if self.attempts_left == 0:
                messagebox.showerror("Game Over", f"You've run out of attempts. The word was: {self.word}.")
                self.reset_game()

        self.guessed_letters_label.config(
            text=f"Guessed letters: {', '.join(sorted(self.guessed_letters))}"
        )

    def reset_game(self):
        self.word = random.choice(self.word_list)
        self.guessed_word = ["_"] * len(self.word)
        self.attempts_left = 6
        self.guessed_letters = set()
        self.word_label.config(text=" ".join(self.guessed_word))
        self.info_label.config(text=f"Attempts left: {self.attempts_left}")
        self.guessed_letters_label.config(text="Guessed letters: None")

# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGame(root)
    root.mainloop()
