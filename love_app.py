import tkinter as tk
from tkinter import messagebox
import math
import random

PASSWORD = "190625"
BG = "#fff0f5"
PINK = "#e85d8f"
DARK = "#79334f"

class LoveApp:
    def __init__(self, root):
        self.root = root
        root.title("Для самой особенной 🌷")
        root.geometry("760x560")
        root.minsize(620, 480)
        root.configure(bg=BG)
        root.resizable(True, True)

        self.canvas = tk.Canvas(root, bg=BG, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.petals = []
        self.draw_intro()
        self.animate()

    def flower(self, x, y, size, color, center="#ffd166"):
        # Пять мягких лепестков и серединка
        for i in range(5):
            a = i * 2 * math.pi / 5
            px = x + math.cos(a) * size * 0.58
            py = y + math.sin(a) * size * 0.58
            self.canvas.create_oval(px-size*.42, py-size*.42,
                                    px+size*.42, py+size*.42,
                                    fill=color, outline="")
        self.canvas.create_oval(x-size*.27, y-size*.27,
                                x+size*.27, y+size*.27,
                                fill=center, outline="")

    def draw_intro(self):
        self.canvas.delete("all")
        w = max(self.root.winfo_width(), 620)
        h = max(self.root.winfo_height(), 480)

        # Нежные цветочные уголки
        palette = ["#f4a6c1", "#f7c5d8", "#d98ab0", "#ffd1dc"]
        for _ in range(26):
            x = random.randint(18, w-18)
            y = random.randint(25, h-25)
            s = random.randint(5, 13)
            self.flower(x, y, s, random.choice(palette))

        self.canvas.create_text(w/2, h*.25, text="🌸  Для тебя  🌸",
                                font=("Segoe UI", 30, "bold"), fill=DARK)
        self.canvas.create_text(w/2, h*.39,
                                text="Немного цветов и много-много любви",
                                font=("Segoe UI", 16), fill="#a34d70")
        self.canvas.create_text(w/2, h*.52, text="🌷   🌹   💐   🌹   🌷",
                                font=("Segoe UI Emoji", 34), fill=PINK)
        self.canvas.create_text(w/2, h*.64,
                                text="У меня для тебя кое-что особенное…",
                                font=("Segoe UI", 15), fill=DARK)

        btn = tk.Button(self.root, text="Открыть сюрприз 💗",
                        command=self.ask_password, font=("Segoe UI", 14, "bold"),
                        bg=PINK, fg="white", activebackground="#d94b7e",
                        activeforeground="white", relief="flat",
                        padx=24, pady=10, cursor="hand2")
        self.canvas.create_window(w/2, h*.79, window=btn)

    def animate(self):
        # Небольшие сердечки-пылинки движутся по экрану
        if self.root.winfo_exists():
            w = max(self.root.winfo_width(), 620)
            h = max(self.root.winfo_height(), 480)
            if len(self.petals) < 18:
                x = random.randint(0, w)
                y = -10
                item = self.canvas.create_text(x, y, text=random.choice(["♥", "✿", "❀"]),
                                               fill=random.choice(["#f2a4bf", "#e88bad", "#f7c5d8"]),
                                               font=("Segoe UI", random.randint(10, 18)))
                self.petals.append((item, random.uniform(0.7, 1.8), random.uniform(-.5, .5)))
            updated = []
            for item, speed, drift in self.petals:
                self.canvas.move(item, drift, speed)
                x1, y1, x2, y2 = self.canvas.bbox(item) or (0, h+1, 0, h+1)
                if y1 < h + 20:
                    updated.append((item, speed, drift))
                else:
                    self.canvas.delete(item)
            self.petals = updated
            self.root.after(55, self.animate)

    def ask_password(self):
        win = tk.Toplevel(self.root)
        win.title("Маленький секрет 💌")
        win.configure(bg=BG)
        win.geometry("390x250")
        win.resizable(False, False)
        win.transient(self.root)
        win.grab_set()

        tk.Label(win, text="💌 Маленький секрет 💌", bg=BG, fg=DARK,
                 font=("Segoe UI", 18, "bold")).pack(pady=(24, 8))
        tk.Label(win, text="Введи пароль, чтобы открыть послание",
                 bg=BG, fg="#a34d70", font=("Segoe UI", 11)).pack(pady=5)
        entry = tk.Entry(win, show="●", justify="center",
                         font=("Segoe UI", 18), width=16, relief="flat",
                         highlightthickness=2, highlightbackground="#f3b5ca",
                         highlightcolor=PINK)
        entry.pack(pady=14, ipady=7)
        entry.focus_set()

        def check(event=None):
            if entry.get() == PASSWORD:
                win.destroy()
                self.show_message()
            else:
                messagebox.showinfo("Почти! 🌷", "Попробуй ещё раз, любимая 💗", parent=win)
                entry.delete(0, tk.END)
                entry.focus_set()

        tk.Button(win, text="Проверить 💗", command=check,
                  font=("Segoe UI", 11, "bold"), bg=PINK, fg="white",
                  activebackground="#d94b7e", relief="flat",
                  padx=22, pady=8, cursor="hand2").pack(pady=4)
        entry.bind("<Return>", check)

    def show_message(self):
        self.canvas.delete("all")
        w = max(self.root.winfo_width(), 620)
        h = max(self.root.winfo_height(), 480)
        self.canvas.configure(bg="#fff4f7")
        self.flower(w*.18, h*.22, 34, "#f2a4bf")
        self.flower(w*.82, h*.22, 34, "#e9a0bb")
        self.flower(w*.20, h*.78, 27, "#f7bfd2")
        self.flower(w*.80, h*.78, 27, "#f7bfd2")
        self.canvas.create_text(w/2, h*.28, text="❤️  Для тебя  ❤️",
                                font=("Segoe UI", 25, "bold"), fill="#c44570")
        msg = ("Ты самая лучшая девушка на свете,\n"
               "я очень сильно тебя люблю,\n"
               "спасибо что ты есть!")
        self.canvas.create_text(w/2, h*.51, text=msg,
                                font=("Segoe UI", 23, "bold"),
                                fill="#873653", justify="center", width=w*.82,
                                spacing3=12)
        self.canvas.create_text(w/2, h*.74, text="🌹  Обнимаю крепко-крепко  🌹",
                                font=("Segoe UI Emoji", 17), fill="#c44570")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoveApp(root)
    root.mainloop()
