import tkinter as tk
from tkinter import messagebox
import random

# --- Game Data ---
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Venus", "Mars", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote the National Anthem of India?",
        "options": ["Rabindranath Tagore", "Lata Mangeshkar", "Bankim Chandra", "Subhash Chandra Bose"],
        "answer": "Rabindranath Tagore"
    },
    {
        "question": "Which is the largest mammal?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
        "answer": "Blue Whale"
    }
]

prizes = [1000, 5000, 10000, 20000]

# --- Main Game Class ---
class KBCGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Kaun Banega Crorepati")
        self.master.geometry("1920x1080")
        self.question_index = 0
        self.total_won = 0
        self.lifeline_used = False

        self.question_label = tk.Label(master, text="", wraplength=450, font=("Arial", 14), justify="center")
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(master, text="", width=40, font=("Arial", 12), command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.lifeline_button = tk.Button(master, text="50:50 Lifeline", command=self.use_lifeline, bg="orange", font=("Arial", 12))
        self.lifeline_button.pack(pady=10)

        self.quit_button = tk.Button(master, text="Quit", command=self.quit_game, bg="red", fg="white", font=("Arial", 12))
        self.quit_button.pack(pady=10)

        self.next_question()

    def next_question(self):
        if self.question_index < len(questions):
            self.current_q = questions[self.question_index]
            self.question_label.config(text=f"Q{self.question_index + 1}: {self.current_q['question']}")
            for i, opt in enumerate(self.current_q["options"]):
                self.buttons[i].config(text=opt, state="normal", bg="SystemButtonFace")
            self.lifeline_button.config(state="normal" if not self.lifeline_used else "disabled")
        else:
            messagebox.showinfo("🏆 Winner!", f"You won ₹{self.total_won}!")
            self.master.destroy()

    def check_answer(self, i):
        selected = self.buttons[i]["text"]
        correct = self.current_q["answer"]
        if selected == correct:
            self.total_won = prizes[self.question_index]
            messagebox.showinfo("Correct!", f"✅ You won ₹{self.total_won}")
            self.question_index += 1
            self.next_question()
        else:
            messagebox.showerror("Wrong!", f"❌ Wrong answer! Correct was: {correct}\nYou won ₹{self.total_won}")
            self.master.destroy()

    def quit_game(self):
        messagebox.showinfo("Quit", f"You quit the game.\nTotal won: ₹{self.total_won}")
        self.master.destroy()

    def use_lifeline(self):
        if self.lifeline_used:
            return
        self.lifeline_used = True
        correct = self.current_q["answer"]
        correct_index = self.current_q["options"].index(correct)

        wrong_indices = [i for i in range(4) if i != correct_index]
        to_remove = random.sample(wrong_indices, 2)

        for i in to_remove:
            self.buttons[i].config(state="disabled")
        self.lifeline_button.config(state="disabled")

# --- Start Game ---
root = tk.Tk()
game = KBCGame(root)
root.mainloop()