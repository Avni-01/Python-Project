import tkinter as tk
from tkinter import messagebox
import random
import string


# === Global color palette and settings ===
colors = ["#e91e63", "#f44336", "#2196f3", "#4caf50",
          "#ffeb3b", "#9c27b0", "#ff9800"]
side_bg = "#1c1c28"
center_bg = "#1e1f28"
banner_height = 40
side_width = 120


root = tk.Tk()
root.title("🎮 PyArcade - Mini Game Hub")

# === FULLSCREEN MODE ===
root.state("zoomed")           # Open window in full-screen (Windows)
root.attributes("-fullscreen", True)  # set to True for true fullscreen
root.resizable(True, True)
root.config(bg=side_bg)

# --- Gradient background canvas ---
bg_canvas = tk.Canvas(root, highlightthickness=0)
bg_canvas.pack(fill="both", expand=True)

def draw_gradient(canvas, height, width, color1, color2):
    (r1, g1, b1) = canvas.winfo_rgb(color1)
    (r2, g2, b2) = canvas.winfo_rgb(color2)
    r_ratio = float(r2 - r1) / height
    g_ratio = float(g2 - g1) / height
    b_ratio = float(b2 - b1) / height
    for i in range(height):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = f"#{nr>>8:02x}{ng>>8:02x}{nb>>8:02x}"
        canvas.create_line(0, i, width, i, fill=color)

gradient_phase = 0
def animate_gradient():
    global gradient_phase
    width = root.winfo_width()
    height = root.winfo_height()
    c1_pos = gradient_phase % len(colors)
    c2_pos = (gradient_phase + 3) % len(colors)
    bg_canvas.delete("all")
    draw_gradient(bg_canvas, height, width, colors[c1_pos], colors[c2_pos])
    gradient_phase = (gradient_phase + 1) % len(colors)
    root.after(100, animate_gradient)

animate_gradient()

# Handle ESC key to exit fullscreen and F11 to toggle it
def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))
def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)
root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", exit_fullscreen)


# Side panels with animated icons
left_side = tk.Canvas(root, width=side_width, height=650, bg=side_bg, highlightthickness=0)
left_side.place(x=0, y=0)
right_side = tk.Canvas(root, width=side_width, height=650, bg=side_bg, highlightthickness=0)
right_side.place(x=780, y=0)


ICON_SIZE = 22
LEFT_ICONS_COUNT = 10
RIGHT_ICONS_COUNT = 14
smiley_unicode = "☺"
def create_star(canvas, x, y, color):
    size = ICON_SIZE
    coords = [
        x + 0, y - size / 2,
        x + size * 0.35, y - size * 0.35,
        x + size, y - size * 0.3,
        x + size * 0.5, y + size * 0.1,
        x + size * 0.6, y + size,
        x + 0, y + size * 0.5,
        x - size * 0.6, y + size,
        x - size * 0.5, y + size * 0.1,
        x - size, y - size * 0.3,
        x - size * 0.35, y - size * 0.35,
    ]
    return canvas.create_polygon(coords, fill=color, outline="")


def create_smiley(canvas, x, y, color):
    return canvas.create_text(x, y, text=smiley_unicode, fill=color, font=("Segoe UI Emoji", 24, "bold"))


def create_heart(canvas, x, y, color):
    size = ICON_SIZE * 0.7
    id1 = canvas.create_oval(x - size / 2, y - size / 2, x, y, fill=color, outline="")
    id2 = canvas.create_oval(x, y - size / 2, x + size / 2, y, fill=color, outline="")
    id3 = canvas.create_polygon(x - size / 2, y, x + size / 2, y, x, y + size, fill=color, outline="")
    return (id1, id2, id3)
def create_icon(canvas, kind, x, y, color):
    if kind == "star":
        return create_star(canvas, x, y, color)
    elif kind == "smiley":
        return create_smiley(canvas, x, y, color)
    elif kind == "heart":
        return create_heart(canvas, x, y, color)


def generate_icons(canvas, count):
    icon_list = []
    kinds = ["star", "smiley", "heart"]
    width = int(canvas["width"])
    for _ in range(count):
        x = random.randint(30, width - 30)
        y = random.randint(0, 650)
        kind = random.choice(kinds)
        color = random.choice(colors)
        id_ = create_icon(canvas, kind, x, y, color)
        icon_list.append({"id": id_, "kind": kind, "x": x, "y": y, "color": color})
    return icon_list


left_icons = generate_icons(left_side, LEFT_ICONS_COUNT)
right_icons = generate_icons(right_side, RIGHT_ICONS_COUNT)
def animate_side_icons():
    for canvas, icon_data in [(left_side, left_icons), (right_side, right_icons)]:
        height = 650
        for icon in icon_data:
            icon["y"] += 1.5
            if icon["y"] > height + 30:
                icon["y"] = -30
                icon["color"] = random.choice(colors)
                if icon["kind"] == "star":
                    canvas.itemconfig(icon["id"], fill=icon["color"])
                elif icon["kind"] == "smiley":
                    canvas.itemconfig(icon["id"], fill=icon["color"])
                else:
                    for item in icon["id"]:
                        canvas.itemconfig(item, fill=icon["color"])
            if icon["kind"] == "star":
                x = icon["x"]
                y = icon["y"]
                size = ICON_SIZE
                coords = [
                    x + 0,
                    y - size / 2,
                    x + size * 0.35,
                    y - size * 0.35,
                    x + size,
                    y - size * 0.3,
                    x + size * 0.5,
                    y + size * 0.1,
                    x + size * 0.6,
                    y + size,
                    x + 0,
                    y + size * 0.5,
                    x - size * 0.6,
                    y + size,
                    x - size * 0.5,
                    y + size * 0.1,
                    x - size,
                    y - size * 0.3,
                    x - size * 0.35,
                    y - size * 0.35,
                ]
                canvas.coords(icon["id"], *coords)
            elif icon["kind"] == "smiley":
                canvas.coords(icon["id"], icon["x"], icon["y"])
            else:
                x = icon["x"]
                y = icon["y"]
                size = ICON_SIZE * 0.7
                canvas.coords(icon["id"][0], x - size / 2, y - size / 2, x, y)
                canvas.coords(icon["id"][1], x, y - size / 2, x + size / 2, y)
                canvas.coords(icon["id"][2], x - size / 2, y, x + size / 2, y, x, y + size)
    root.after(50, animate_side_icons)


animate_side_icons()


# Center content
center_frame = tk.Frame(root, bg=center_bg)
center_frame.place(x=side_width, y=0, width=660, height=650)


# Banner in center_frame
banner = tk.Canvas(center_frame, height=banner_height, bg="#121212", highlightthickness=0)
banner.pack(fill="x")


banner_shapes = []
banner_pos = []
banner_speeds = []
def create_banner():
    banner_shapes.clear()
    banner_pos.clear()
    banner_speeds.clear()
    width = banner.winfo_width() or 660
    count = max(width // 70, 12)
    for i in range(count):
        x = i * 70
        y = banner_height // 2
        r = 15
        c = random.choice(colors)
        oval = banner.create_oval(x - r, y - r, x + r, y + r, fill=c, outline="")
        banner_shapes.append(oval)
        banner_pos.append(x)
        banner_speeds.append(random.choice([2, 3, 4]))


def animate_banner():
    width = banner.winfo_width()
    for i in range(len(banner_shapes)):
        banner_pos[i] += banner_speeds[i]
        if banner_pos[i] - 15 > width:
            banner_pos[i] = -30
            banner.itemconfig(banner_shapes[i], fill=random.choice(colors))
        x = banner_pos[i]
        y = banner_height // 2
        banner.coords(banner_shapes[i], x - 15, y - 15, x + 15, y + 15)
    banner.after(50, animate_banner)
banner.bind("<Configure>", lambda e: create_banner())
create_banner()
animate_banner()


# Button with flashing rainbow text and hover effect
class HoverButton(tk.Button):
    def _init_(self, master=None, **kw):
        self.flash_colors = colors
        self.flash_index = 0
        super()._init_(master=master, **kw)
        self.defaultBackground = self["background"]
        self.defaultForeground = self["foreground"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.animate_flash()
    def animate_flash(self):
        self.flash_index = (self.flash_index + 1) % len(self.flash_colors)
        self.config(fg=self.flash_colors[self.flash_index])
        self.after(700, self.animate_flash)
    def on_enter(self, e):
        self['background'] = '#ff7043'
        self['foreground'] = 'white'
    def on_leave(self, e):
        self['background'] = self.defaultBackground
        self['foreground'] = self.defaultForeground
def clear_frame():
    # Clear all widgets in center_frame except the banner
    for w in center_frame.winfo_children():
        if w is not banner:
            w.destroy()


# --- Games Implementation ---

# Number Guessing Game
def number_guess_game():
    clear_frame()
    container = tk.Frame(center_frame, bg="#ffd54f", bd=5, relief="ridge")
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
                result.config(text="⬇ Too low!", fg="#f57c00")
            elif guess > number:
                result.config(text="⬆ Too high!", fg="#f57c32")
            else:
                result.config(text="🎉 Correct! You guessed it!", fg="#2e7d32")
        except:
            result.config(text="⚠ Enter a valid number!", fg="#d32f2f")
    btn_frame = tk.Frame(container, bg="#ffd54f")
    btn_frame.pack(pady=15)
    check_btn = HoverButton(btn_frame, text="Check", command=check_guess, bg="#fbc02d", font=("Arial", 14), width=12)
    check_btn.pack(side="left", padx=12)
    back_btn = HoverButton(btn_frame, text="Back", command=main_menu, bg="#ff8a65", font=("Arial", 14), width=12)
    back_btn.pack(side="left", padx=12)
# Rock Paper Scissors
def rps_game():
    clear_frame()
    container = tk.Frame(center_frame, bg="#81d4fa", bd=5, relief="groove")
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
        b = HoverButton(btn_frame, text=opt, bg="#4fc3f7", font=("Arial Black", 16), width=12, command=lambda o=opt: play(o))
        b.pack(side="left", padx=10)
    back_btn = HoverButton(container, text="Back", command=main_menu, bg="#ff8a65", font=("Arial", 16), width=14)
    back_btn.pack(pady=20)
# Dice Roll Simulator
def dice_roll():
    clear_frame()
    container = tk.Frame(center_frame, bg="#b9f6ca", bd=5, relief="sunken")
    container.pack(pady=20, padx=20, fill="both", expand=True)
    tk.Label(container, text="🎲 Dice Roll Simulator", font=("Arial Black", 26), bg="#b9f6ca", fg="#1b5e20").pack(pady=20)
    label = tk.Label(container, text="🎲", font=("Arial Black", 120), bg="#b9f6ca", fg="#388e3c")
    label.pack(pady=15)
    def roll():
        last_num = None
        for _ in range(6):
            last_num = random.randint(1,6)
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
# Calculator
def calculator():
    clear_frame()
    container = tk.Frame(center_frame, bg="#ffccbc", bd=6, relief="ridge")
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
# Password Generator
def password_generator():
    clear_frame()
    container = tk.Frame(center_frame, bg="#b3e5fc", bd=6, relief="sunken")
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


# Tic Tac Toe
def tictactoe():
    clear_frame()

    # === Main container ===
    outer_container = tk.Frame(center_frame, bg="#d1c4e9")
    outer_container.pack(fill="both", expand=True)

    # --- Scrollable area for the game ---
    canvas = tk.Canvas(outer_container, bg="#d1c4e9", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(outer_container, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    game_frame = tk.Frame(canvas, bg="#d1c4e9")
    canvas.create_window((0, 0), window=game_frame, anchor="nw")

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    game_frame.bind("<Configure>", on_configure)

    def _on_mousewheel(event):
        try:
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        except tk.TclError:
            pass

    canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
    canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

    # === Game Header ===
    tk.Label(game_frame, text="⭕❌ Tic Tac Toe", font=("Arial Black", 30),
             bg="#d1c4e9", fg="#311b92").pack(pady=20)

    current = ["X"]
    buttons = []
    move_history = []

    def check_winner():
        wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6)]
        for a, b, c in wins:
            if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
                messagebox.showinfo("Game Over", f"{buttons[a]['text']} wins!")
                for btn in buttons:
                    btn.config(state="disabled")
                return True
        if all(btn["text"] != "" for btn in buttons):
            messagebox.showinfo("Game Over", "It's a tie!")
            return True
        return False

    def click(i):
        if buttons[i]["text"] == "":
            buttons[i].config(text=current[0], fg="#4527a0", font=("Arial Black", 24))
            move_history.append(i)
            if not check_winner():
                current[0] = "O" if current[0] == "X" else "X"
            undo_btn.config(state="normal")

    def undo_move():
        if move_history:
            last = move_history.pop()
            buttons[last].config(text="")
            current[0] = "O" if current[0] == "X" else "X"
            for btn in buttons:
                btn.config(state="normal")
            if not move_history:
                undo_btn.config(state="disabled")

    def restart_game():
        for btn in buttons:
            btn.config(text="", state="normal")
        move_history.clear()
        current[0] = "X"
        undo_btn.config(state="disabled")

    # === Game Board ===
    board_frame = tk.Frame(game_frame, bg="#d1c4e9")
    board_frame.pack(pady=10)

    for i in range(9):
        b = tk.Button(board_frame, text="", width=6, height=3, bg="#ede7f6",
                      relief="raised", bd=4, command=lambda i=i: click(i))
        b.grid(row=i // 3, column=i % 3, padx=8, pady=8)
        buttons.append(b)

    # === Control Buttons (inside scrollable area) ===
    control_frame = tk.Frame(game_frame, bg="#d1c4e9")
    control_frame.pack(pady=25)

    undo_btn = HoverButton(control_frame, text="⬅ Undo Move", bg="#9575cd",
                           fg="white", font=("Arial Black", 16),
                           width=14, command=undo_move, state="disabled")
    undo_btn.pack(side="left", padx=10)

    restart_btn = HoverButton(control_frame, text="🔁 Restart", bg="#7e57c2",
                              fg="white", font=("Arial Black", 16),
                              width=14, command=restart_game)
    restart_btn.pack(side="left", padx=10)

    # === Fixed Main Menu Button (always visible at bottom) ===
    fixed_menu_frame = tk.Frame(center_frame, bg="#5e35b1")
    fixed_menu_frame.pack(side="bottom", fill="x")

    back_btn = HoverButton(fixed_menu_frame, text="🏠 Back to Main Menu",
                           bg="#5e35b1", fg="white",
                           font=("Arial Black", 20),
                           width=20, height=2, command=main_menu)
    back_btn.pack(pady=8)


    


# Balloon Pop
def balloon_pop():
    clear_frame()
    container = tk.Frame(center_frame, bg="#c8e6c9", bd=6, relief="ridge")
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
            color = random.choice(["#e57373", "#81c784", "#64b5f6", "#ffb74d", "#fff176"])
            b1 = canvas.create_oval(x, y, x + 40, y + 55, fill=color, outline="", tags=("balloon",))
            b2 = canvas.create_line(x + 20, y + 55, x + 20, y + 75, fill=color, width=2, tags=("balloon",))
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
# Main menu with scroll
def main_menu():
    clear_frame()

    container = tk.Frame(center_frame, bg=center_bg)
    container.pack(fill='both', expand=True)

    canvas = tk.Canvas(container, bg=center_bg, highlightthickness=0)
    canvas.pack(side='left', fill='both', expand=True)

    scrollbar = tk.Scrollbar(container, orient='vertical', command=canvas.yview)
    scrollbar.pack(side='right', fill='y')

    canvas.configure(yscrollcommand=scrollbar.set)

    frame = tk.Frame(canvas, bg=center_bg)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame.bind("<Configure>", on_frame_configure)

    # --- SAFER MOUSE SCROLL HANDLER ---
    def _on_mousewheel(event):
        try:
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        except tk.TclError:
            # Canvas was destroyed or no longer exists
            pass

    # Bind scroll events to *this* canvas only
    canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
    canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

    header = tk.Label(frame, text="Select a Game", font=("Giddyup Std", 36, "bold"),
                      fg="#00bcd4", bg=center_bg)
    header.pack(pady=20)

    options = [
        ("🔢 Number Guessing", number_guess_game),
        ("✊✋✌ Rock Paper Scissors", rps_game),
        ("🎲 Dice Roll Simulator", dice_roll),
        ("🧮 Calculator", calculator),
        ("🔐 Password Generator", password_generator),
        ("⭕❌ Tic Tac Toe", tictactoe),
        ("🎈 Balloon Pop Game", balloon_pop),
    ]

    for (text, cmd) in options:
        b = HoverButton(frame, text=text, command=cmd,
                        bg="#03a9f4", width=30, height=2,
                        font=("Segoe Print", 24, "bold"))
        b.pack(pady=12)

    exit_btn = HoverButton(center_frame, text="Exit", command=root.destroy,
                           bg="#d32f2f", fg="white",
                           font=("Arial Black", 22), width=20, height=2)
    exit_btn.pack(pady=18)



main_menu()
root.mainloop()
