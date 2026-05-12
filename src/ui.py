import tkinter as tk
from tkinter import font
import threading

class SubtitleWindow:
    def __init__(self, title="Subtitle Translator"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("800x200")
        self.root.configure(bg="#1e1e1e")

        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.95)

        font_large = font.Font(family="Arial", size=14, weight="bold")
        font_small = font.Font(family="Arial", size=12)

        self.english_label = tk.Label(
            self.root,
            text="",
            font=font_large,
            fg="#00d4ff",
            bg="#1e1e1e",
            wraplength=780,
            justify=tk.CENTER
        )
        self.english_label.pack(pady=10)

        separator = tk.Label(self.root, text="─" * 50, fg="#666666", bg="#1e1e1e")
        separator.pack()

        self.russian_label = tk.Label(
            self.root,
            text="",
            font=font_small,
            fg="#00ff00",
            bg="#1e1e1e",
            wraplength=780,
            justify=tk.CENTER
        )
        self.russian_label.pack(pady=10)

        self.status_label = tk.Label(
            self.root,
            text="Listening...",
            font=("Arial", 10),
            fg="#888888",
            bg="#1e1e1e"
        )
        self.status_label.pack(side=tk.BOTTOM, pady=5)

    def update_subtitles(self, english_text, russian_text):
        self.english_label.config(text=english_text)
        self.russian_label.config(text=russian_text)
        self.root.update()

    def update_status(self, status_text):
        self.status_label.config(text=status_text)
        self.root.update()

    def run(self):
        self.root.mainloop()

    def close(self):
        self.root.quit()
