import tkinter as tk
from tkinter import messagebox
import random, string

# --- Window Setup ---
root = tk.Tk()
root.title("🎮 PyArcade - Mini Game Hub")
root.geometry("700x600")
root.config(bg="#1e1f28")  # Dark background for modern look

title_label = tk.Label(
    root, text="🎮 PyArcade - Mini Game Hub",
    font=("Comic Sans MS", 26, "bold"),
    bg="#304FFE", fg="white",
    pady=16,
    relief="raised",
    bd=4
)
title_label.pack(fill="x")

def clear_frame():
    for widget in root.winfo_children():
        if widget not in (title_label,):
            widget.destroy()

# Utility: Styled Button with hover effect
class HoverButton(tk.Button):
    def __init__(self, master=None, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
    def on_enter(self, e):
        self['background'] = '#ff7043'  # bright orange on hover
        self['foreground'] = 'white'
    def on_leave(self, e):
        self['background'] = self.defaultBackground
        self['foreground'] = 'black'

def number_guess_game():
    clear_frame()
    container = tk.Frame(root, bg="#ffd54f", bd=5, relief="ridge")
    container.pack(pady=15, padx=20, fill="both", expand=True)

    tk.Label(container, text="🔢 Number Guessing Game", font=("Arial Black", 22), bg="#ffd54f", fg="#bf360c").pack(pady=12)
    number = random.randint(1, 20)
    
    tk.Label(container, text="Guess a number (1–20):", font=("Arial", 14), bg="#ffd54f", fg="#3e2723").pack(pady=5)
    entry = tk.Entry(container, font=("Arial", 16), justify="center")
    entry.pack(pady=5)
    result = tk.Label(container, text="", bg="#ffd54f", fg="green", font=("Arial", 14))
    result.pack(pady=5)

    def check_guess():
        try:
            guess = int(entry.get())
            if guess < number:
                result.config(text="⬇️ Too low!")
            elif guess > number:
                result.config(text="⬆️ Too high!")
            else:
                result.config(text="🎉 Correct! You guessed it!", fg="#2e7d32")
        except:
            result.config(text="⚠️ Enter a valid number!", fg="#d32f2f")
    
    btn_frame = tk.Frame(container, bg="#ffd54f")
    btn_frame.pack(pady=15)
    check_btn = HoverButton(btn_frame, text="Check", command=check_guess, bg="#fbc02d", font=("Arial", 14), width=12)
    check_btn.pack(side="left", padx=12)
    back_btn = HoverButton(btn_frame, text="Back", command=main_menu, bg="#ff8a65", font=("Arial", 14), width=12)
    back_btn.pack(side="left", padx=12)

def rps_game():
    clear_frame()
    container = tk.Frame(root, bg="#81d4fa", bd=5, relief="groove")
    container.pack(pady=15, padx=20, fill="both", expand=True)
    tk.Label(container, text="✊✋✌ Rock Paper Scissors", font=("Arial Black", 24), bg="#81d4fa", fg="#01579b").pack(pady=15)
    options = ["Rock", "Paper", "Scissors"]
    result = tk.Label(container, text="", bg="#81d4fa", font=("Arial", 16), fg="#0d47a1")
    result.pack(pady=20)
    
    def play(choice):
        comp = random.choice(options)
        if choice == comp:
            res = "It's a tie!"
        elif (choice == "Rock" and comp == "Scissors") or (choice == "Paper" and comp == "Rock") or (choice == "Scissors" and comp == "Paper"):
            res = "🎉 You win!"
        else:
            res = "😢 You lose!"
        result.config(text=f"Computer chose: {comp}\n{res}")

    btn_frame = tk.Frame(container, bg="#81d4fa")
    btn_frame.pack(pady=10)
    for opt in options:
        b = HoverButton(btn_frame, text=opt, bg="#4fc3f7", font=("Arial Black", 16), width=12,
                          command=lambda o=opt: play(o))
        b.pack(side="left", padx=10)
    back_btn = HoverButton(container, text="Back", command=main_menu, bg="#ff8a65", font=("Arial", 16), width=14)
    back_btn.pack(pady=20)

def dice_roll():
    clear_frame()
    container = tk.Frame(root, bg="#b9f6ca", bd=5, relief="sunken")
    container.pack(pady=20, padx=20, fill="both", expand=True)

    tk.Label(container, text="🎲 Dice Roll Simulator", font=("Arial Black", 26), bg="#b9f6ca", fg="#1b5e20").pack(pady=20)
    label = tk.Label(container, text="🎲", font=("Arial Black", 120), bg="#b9f6ca", fg="#388e3c")
    label.pack(pady=15)
    
    def roll():
        last_num = None
        for _ in range(6):
            last_num = random.randint(1, 6)
            label.config(text=str(last_num))
            root.update()
            root.after(70)
        label.config(text=str(last_num))
    
    btn_frame = tk.Frame(container, bg="#b9f6ca")
    btn_frame.pack(pady=20)
    roll_btn = HoverButton(btn_frame, text="Roll Dice", bg="#66bb6a", font=("Arial Black", 16), width=16, command=roll)
    roll_btn.pack(side="left", padx=15)
    back_btn = HoverButton(btn_frame, text="Back", bg="#ff8a65", font=("Arial", 16), width=12, command=main_menu)
    back_btn.pack(side="left", padx=15)

def calculator():
    clear_frame()
    container = tk.Frame(root, bg="#ffccbc", bd=6, relief="ridge")
    container.pack(pady=15, padx=20, fill="both", expand=True)

    tk.Label(container, text="🧮 Calculator", font=("Arial Black", 28), bg="#ffccbc", fg="#bf360c").pack(pady=15)
    tk.Label(container, text="Enter numbers separated by space (e.g., 10 5 2):", bg="#ffccbc", fg="#3e2723", font=("Arial", 14)).pack(pady=5)
    entry = tk.Entry(container, font=("Arial", 18), justify="center")
    entry.pack(pady=8, ipadx=10, ipady=4)
    result = tk.Label(container, text="", bg="#ffccbc", fg="green", font=("Arial Black", 18))
    result.pack(pady=12)
    
    def calculate(op):
        try:
            nums = list(map(float, entry.get().split()))
            if not nums:
                raise ValueError
            if op == '+':
                res = sum(nums)
            elif op == '-':
                if len(nums) == 1:
                    res = nums[0]
                else:
                    res = nums[0] - sum(nums[1:])
            elif op == '*':
                res = 1
                for n in nums:
                    res *= n
            elif op == '/':
                res = nums[0]
                for n in nums[1:]:
                    if n == 0:
                        raise ZeroDivisionError
                    res /= n
            result.config(text=f"Result: {res}", fg="#2e7d32")
        except ZeroDivisionError:
            result.config(text="Error: Divide by zero", fg="#d32f2f")
        except:
            result.config(text="Invalid input!", fg="#d32f2f")
    
    btn_frame = tk.Frame(container, bg="#ffccbc")
    btn_frame.pack(pady=12)
    for idx, symbol in enumerate(['+', '-', '*', '/']):
        btn = HoverButton(btn_frame, text=symbol, width=8, font=("Arial Black", 18), bg="#ff8a65", command=lambda s=symbol: calculate(s))
        btn.grid(row=0, column=idx, padx=8)

    clear_btn = HoverButton(container, text="Clear All", bg="#f06292", fg="white", font=("Arial Black", 18), command=lambda: (entry.delete(0, 'end'), result.config(text="", fg="green")))
    clear_btn.pack(pady=15, ipadx=5, ipady=5)

    back_btn = HoverButton(container, text="Back", bg="#ff8a65", font=("Arial Black", 20), command=main_menu)
    back_btn.pack(pady=10, ipadx=5, ipady=5)

def password_generator():
    clear_frame()
    container = tk.Frame(root, bg="#b3e5fc", bd=6, relief="sunken")
    container.pack(pady=15, padx=20, fill="both", expand=True)

    tk.Label(container, text="🔐 Password Generator", font=("Arial Black", 26), bg="#b3e5fc", fg="#01579b").pack(pady=16)
    tk.Label(container, text="Enter password length:", font=("Arial", 16), bg="#b3e5fc", fg="#003c8f").pack(pady=8)
    
    entry = tk.Entry(container, font=("Arial", 20), justify="center")
    entry.pack(pady=6)
    
    output = tk.Entry(container, font=("Courier New", 18, "bold"), justify="center", width=40, bg="#e1f5fe", fg="#01579b", bd=4, relief="ridge")
    output.pack(pady=12)
    
    def generate():
        try:
            length = int(entry.get())
            if length <= 0: raise ValueError
            chars = string.ascii_letters + string.digits + "!@#$%^&*()"
            password = ''.join(random.choice(chars) for _ in range(length))
            output.delete(0, tk.END)
            output.insert(0, password)
        except:
            messagebox.showerror("Error", "Please enter a valid positive number")
    
    btn_frame = tk.Frame(container, bg="#b3e5fc")
    btn_frame.pack(pady=10)
    gen_btn = HoverButton(btn_frame, text="Generate", bg="#0288d1", fg="white", font=("Arial Black", 20), width=20, command=generate)
    gen_btn.pack()
    
    back_btn = HoverButton(container, text="Back", bg="#ff8a65", font=("Arial Black", 22), command=main_menu)
    back_btn.pack(pady=15)

def tictactoe():
    clear_frame()
    container = tk.Frame(root, bg="#d1c4e9", bd=5, relief="groove")
    container.pack(pady=15, padx=20, fill="both", expand=True)

    tk.Label(container, text="⭕❌ Tic Tac Toe", font=("Arial Black", 28), bg="#d1c4e9", fg="#311b92").pack(pady=20)
    current = ["X"]
    buttons = []
    
    def check_winner():
        wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for a,b,c in wins:
            if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
                messagebox.showinfo("Game Over", f"{buttons[a]['text']} wins!")
                for btn in buttons: btn.config(state="disabled")
                return True
        if all(btn["text"] != "" for btn in buttons):
            messagebox.showinfo("Game Over", "It's a tie!")
            return True
        return False
    
    def click(i):
        if buttons[i]["text"] == "":
            buttons[i].config(text=current[0], fg="#4527a0", font=("Arial Black", 24))
            if not check_winner():
                current[0] = "O" if current[0]=="X" else "X"
    
    frame = tk.Frame(container, bg="#d1c4e9")
    frame.pack()
    for i in range(9):
        b = tk.Button(frame, text="", width=6, height=3, bg="#ede7f6", relief="raised", bd=4, command=lambda i=i: click(i))
        b.grid(row=i//3, column=i%3, padx=8, pady=8)
        buttons.append(b)
    back_btn = HoverButton(container, text="Back", bg="#7e57c2", fg="white", font=("Arial Black", 20), command=main_menu)
    back_btn.pack(pady=15)

def balloon_pop():
    clear_frame()
    container = tk.Frame(root, bg="#c8e6c9", bd=6, relief="ridge")
    container.pack(pady=20, padx=20, fill="both", expand=True)
    
    tk.Label(container, text="🎈 Balloon Pop Game - 30 seconds", font=("Arial Black", 24), bg="#c8e6c9", fg="#1b5e20").pack(pady=15)
    canvas = tk.Canvas(container, width=600, height=380, bg="#a5d6a7", bd=4, relief="sunken")
    canvas.pack(pady=10)
    score = [0]
    time_left = [30]
    score_label = tk.Label(container, text=f"Score: {score[0]} | Time: {time_left[0]}s", bg="#c8e6c9", fg="#2e7d32", font=("Arial Black", 14))
    score_label.pack()

    balloons = {}

    def pop_balloon(evt):
        items = canvas.find_withtag("current")
        for it in items:
            if "balloon" in canvas.gettags(it):
                group = balloons.get(it, [])
                for item_id in group:
                    try:
                        canvas.delete(item_id)
                    except:
                        pass
                for key in list(balloons.keys()):
                    if it in balloons[key]:
                        del balloons[key]
                        break
                score[0] += 1
                score_label.config(text=f"Score: {score[0]} | Time: {time_left[0]}s")
                break

    def spawn_balloon():
        if time_left[0] > 0:
            x, y = random.randint(20, 540), random.randint(20, 320)
            color = random.choice(["#e57373","#81c784","#64b5f6","#ffb74d","#fff176"])
            b1 = canvas.create_oval(x, y, x+40, y+55, fill=color, outline="", tags=("balloon",))
            b2 = canvas.create_line(x+20, y+55, x+20, y+75, fill=color, width=2, tags=("balloon",))
            balloons[b1] = [b1, b2]
            canvas.tag_bind(b1, "<Button-1>", pop_balloon)
            canvas.tag_bind(b2, "<Button-1>", pop_balloon)
            root.after(random.randint(600, 1200), spawn_balloon)

    def countdown():
        if time_left[0] > 0:
            time_left[0] -= 1
            score_label.config(text=f"Score: {score[0]} | Time: {time_left[0]}s")
            root.after(1000, countdown)
        else:
            canvas.delete("all")
            messagebox.showinfo("Time Up!", f"🎯 Final Score: {score[0]}")
            main_menu()

    spawn_balloon()
    countdown()
    back_btn = HoverButton(container, text="Back", bg="#81c784", fg="white", font=("Arial Black", 20), command=main_menu)
    back_btn.pack(pady=15)

def main_menu():
    clear_frame()
    options = [
        ("🔢 Number Guessing", number_guess_game),
        ("✊✋✌ Rock Paper Scissors", rps_game),
        ("🎲 Dice Roll Simulator", dice_roll),
        ("🧮 Calculator", calculator),
        ("🔐 Password Generator", password_generator),
        ("⭕❌ Tic Tac Toe", tictactoe),
        ("🎈 Balloon Pop Game", balloon_pop),
    ]
    frame = tk.Frame(root, bg="#1e1f28")
    frame.pack(pady=70)
    header = tk.Label(frame, text="Select a Game", font=("Comic Sans MS", 32, "bold"), fg="#00bcd4", bg="#1e1f28")
    header.pack(pady=20)
    for (text, cmd) in options:
        b = HoverButton(frame, text=text, command=cmd, bg="#03a9f4", fg="white", font=("Comic Sans MS", 20), width=30, height=2)
        b.pack(pady=12)
    exit_btn = HoverButton(root, text="Exit", command=root.destroy, bg="#d32f2f", fg="white", font=("Arial Black", 22), width=20, height=2)
    exit_btn.pack(pady=18)

main_menu()
root.mainloop()

