import tkinter as tk
from tkinter import messagebox
import random

# Number Guessing Game with its own window and UI
def number_guessing():
    def check_guess():
        nonlocal attempts
        try:
            guess_num = int(entry.get())
        except ValueError:
            info_label.config(text="Please enter a valid integer", fg="red")
            return
        attempts += 1
        if guess_num < number:
            info_label.config(text="Too low! Try again.", fg="orange")
        elif guess_num > number:
            info_label.config(text="Too high! Try again.", fg="orange")
        else:
            messagebox.showinfo("Congrats!", f"You guessed it in {attempts} tries!")
            window.destroy()
        entry.delete(0, tk.END)

    number = random.randint(1, 20)
    attempts = 0
    window = tk.Toplevel()
    window.title("Number Guessing Game")
    window.geometry("350x200")
    window.configure(bg="#101010")

    title = tk.Label(window, text="Guess the number (1-20)", font=("Arial Bold", 16), bg="#101010", fg="cyan")
    title.pack(pady=10)

    entry = tk.Entry(window, font=("Arial", 14), justify="center")
    entry.pack(pady=5)
    entry.focus()

    check_btn = tk.Button(window, text="Check", font=("Arial", 14), bg="#00bfff", fg="white", command=check_guess)
    check_btn.pack(pady=10)

    info_label = tk.Label(window, text="", font=("Arial", 12), bg="#101010")
    info_label.pack()

# Rock Paper Scissors with buttons and result label
def rock_paper_scissors():
    def play(choice):
        comp_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        result_text = f"Computer chose: {comp_choice}\nYou chose: {choice}\n"
        wins = {
            'Rock': 'Scissors',
            'Scissors': 'Paper',
            'Paper': 'Rock'
        }
        if comp_choice == choice:
            result_text += "It's a Tie!"
        elif wins[choice] == comp_choice:
            result_text += "You Win!"
        else:
            result_text += "You Lose!"
        result_label.config(text=result_text)

    window = tk.Toplevel()
    window.title("Rock Paper Scissors")
    window.geometry("400x300")
    window.configure(bg="#222222")

    label = tk.Label(window, text="Choose Rock, Paper, or Scissors", font=("Helvetica", 16, "bold"), fg="white", bg="#222222")
    label.pack(pady=15)

    frame = tk.Frame(window, bg="#222222")
    frame.pack()

    for option in ['Rock', 'Paper', 'Scissors']:
        btn = tk.Button(frame, text=option, width=10, height=2, font=("Arial", 14),
                        command=lambda ch=option: play(ch),
                        bg="#5dade2", fg="white", activebackground="#2e86c1")
        btn.pack(side="left", padx=10)

    result_label = tk.Label(window, text="", font=("Arial", 14), fg="yellow", bg="#222222")
    result_label.pack(pady=20)

# Dice Roll Simulator with a rolling animation
def dice_roll():
    window = tk.Toplevel()
    window.title("Dice Roll Simulator")
    window.geometry("300x250")
    window.configure(bg="#2c3e50")

    label = tk.Label(window, text="Click Roll to roll the dice", font=("Courier", 14), fg="white", bg="#2c3e50")
    label.pack(pady=20)

    dice_label = tk.Label(window, text="", font=("Helvetica", 100), fg="white", bg="#2c3e50")
    dice_label.pack()

    def roll():
        last_num = None
        for _ in range(5):
            num = random.randint(1, 6)
            dice_label.config(text=str(num))
            window.update()
            window.after(100)
            last_num = num
        dice_label.config(text=str(last_num))

    roll_btn = tk.Button(window, text="Roll", font=("Arial", 16), bg="#2980b9", fg="white", command=roll)
    roll_btn.pack(pady=20)

# Simple Calculator with input fields and operation buttons
def calculator():
    def calculate():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            op = operation.get()
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    result_label.config(text="Error: Divide by zero", fg="red")
                    return
                result = num1 / num2
            else:
                result_label.config(text="Invalid Operation", fg="red")
                return
            result_label.config(text=f"Result: {result}", fg="lightgreen")
        except ValueError:
            result_label.config(text="Invalid Input", fg="red")

    window = tk.Toplevel()
    window.title("Simple Calculator")
    window.geometry("350x300")
    window.configure(bg="#34495e")

    label = tk.Label(window, text="Enter numbers and select operation", font=("Arial", 14), fg="white", bg="#34495e")
    label.pack(pady=10)

    entry1 = tk.Entry(window, font=("Arial", 16), justify="center")
    entry1.pack(pady=5)
    entry2 = tk.Entry(window, font=("Arial", 16), justify="center")
    entry2.pack(pady=5)

    operation = tk.StringVar(value='+')
    ops_frame = tk.Frame(window, bg="#34495e")
    ops_frame.pack(pady=5)

    for op in ['+', '-', '*', '/']:
        tk.Radiobutton(ops_frame, text=op, variable=operation, value=op,
                       font=("Arial", 14), bg="#34495e", fg="white",
                       selectcolor="#2980b9", activebackground="#2980b9").pack(side="left", padx=8)

    calc_btn = tk.Button(window, text="Calculate", font=("Arial", 14), bg="#27ae60", fg="white", command=calculate)
    calc_btn.pack(pady=10)

    result_label = tk.Label(window, text="", font=("Arial Bold", 16), bg="#34495e")
    result_label.pack()

# Password Generator with length input and display box
def password_generator():
    def generate():
        length = entry.get()
        if not length.isdigit() or int(length) <= 0:
            output.configure(state='normal')
            output.delete('1.0', tk.END)
            output.insert(tk.END, "Enter a positive integer for length.")
            output.configure(state='disabled')
            return
        length_val = int(length)
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
        passwd = "".join(random.choice(chars) for _ in range(length_val))
        output.configure(state='normal')
        output.delete('1.0', tk.END)
        output.insert(tk.END, passwd)
        output.configure(state='disabled')

    window = tk.Toplevel()
    window.title("Password Generator")
    window.geometry("400x220")
    window.configure(bg="#1b2631")

    label = tk.Label(window, text="Enter password length:", font=("Helvetica", 14), fg="white", bg="#1b2631")
    label.pack(pady=10)

    entry = tk.Entry(window, font=("Arial", 16), justify="center")
    entry.pack()

    gen_btn = tk.Button(window, text="Generate Password", font=("Arial", 14), bg="#e67e22", fg="white", command=generate)
    gen_btn.pack(pady=15)

    output = tk.Text(window, height=2, font=("Consolas", 16), bg="#17202a", fg="lime", state='disabled')
    output.pack(padx=10, fill="both")

# Tic Tac Toe with grid of buttons
def tic_tac_toe():
    window = tk.Toplevel()
    window.title("Tic Tac Toe")
    window.geometry("350x400")
    window.configure(bg="#1c2833")

    turn = ['X']  # Use list to allow inner func to modify

    board = [''] * 9
    buttons = []

    def check_winner():
        wins = [
            (0,1,2),(3,4,5),(6,7,8),  # rows
            (0,3,6),(1,4,7),(2,5,8),  # cols
            (0,4,8),(2,4,6)           # diagonals
        ]
        for a,b,c in wins:
            if board[a] == board[b] == board[c] != '':
                return board[a]
        if '' not in board:
            return 'Tie'
        return None

    def click(i):
        if board[i] == '':
            board[i] = turn[0]
            buttons[i].config(text=turn[0], state='disabled',
                              disabledforeground="#f7dc6f" if turn[0] == 'X' else "#85c1e9")
            winner = check_winner()
            if winner:
                if winner == 'Tie':
                    messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                else:
                    messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
                window.destroy()
            turn[0] = 'O' if turn[0] == 'X' else 'X'

    title = tk.Label(window, text="Tic Tac Toe", font=("Arial Black", 20), fg="white", bg="#1c2833")
    title.pack(pady=10)

    frame = tk.Frame(window, bg="#1c2833")
    frame.pack()

    for i in range(9):
        b = tk.Button(frame, text="", width=5, height=2, font=("Arial Black", 24), command=lambda i=i: click(i), bg="#34495e", fg="white")
        b.grid(row=i//3, column=i%3, padx=5, pady=5)
        buttons.append(b)

# Main launcher window with buttons and styling for each game
class GameCollectionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Python Games Collection")
        self.geometry("450x500")
        self.configure(bg="#121212")

        title = tk.Label(self, text="Simple Python Games", font=("Comic Sans MS", 22, "bold"), fg="#f39c12", bg="#121212")
        title.pack(pady=25)

        btn_style = {
            "font": ("Arial", 14, "bold"),
            "bg": "#34495e",
            "fg": "white",
            "relief": "raised",
            "bd": 4,
            "activebackground": "#f39c12",
            "activeforeground": "black",
            "width": 30,
            "pady": 8
        }

        games = [
            ("Number Guessing", number_guessing),
            ("Rock Paper Scissors", rock_paper_scissors),
            ("Dice Roll Simulator", dice_roll),
            ("Calculator", calculator),
            ("Password Generator", password_generator),
            ("Tic Tac Toe", tic_tac_toe),
        ]

        for (text, func) in games:
            btn = tk.Button(self, text=text, command=func, **btn_style)
            btn.pack(pady=8)

        quit_btn = tk.Button(self, text="Exit", command=self.destroy, font=("Arial", 14, "bold"),
                             bg="#c0392b", fg="white", width=30, pady=8)
        quit_btn.pack(pady=20)

if __name__ == "__main__":
    app = GameCollectionApp()
    app.mainloop()
