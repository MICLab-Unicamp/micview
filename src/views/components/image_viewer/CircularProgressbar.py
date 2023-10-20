'''
import tkinter as tk
from threading import Thread

class CircularProgressbar(tk.Canvas):
    def __init__(self, root):
        self.root = root
        super().__init__(self.root, height=200, width=200)
        self.width = 200
        self.height = 200
        self.center_x = self.width // 2
        self.center_y = self.height // 2
        self.radius = min(self.center_x, self.center_y) - 5
        self.angle = 360
        self.speed = 10

        self.configure(bg="lightblue", highlightthickness=0)
        self.create_oval(
            self.center_x - self.radius, self.center_y - self.radius,
            self.center_x + self.radius, self.center_y + self.radius,
            outline="blue", width=4
        )

        self.arc = self.create_arc(
            self.center_x - self.radius, self.center_y - self.radius,
            self.center_x + self.radius, self.center_y + self.radius,
            start=180, extent=0, outline="blue", width=5, style=tk.ARC
        )
        self.after(50, self.update)

    def update(self):
        self.angle -= self.speed
        if self.angle <= 0:
            self.angle = 360
        self.draw_arc()
        self.after(50, self.update)

    def draw_arc(self):
        self.itemconfig(
            self.arc,
            extent=self.angle,
            outline="gray"
        )

    def close(self):
        self.destroy()
        self.update_idletasks()
'''