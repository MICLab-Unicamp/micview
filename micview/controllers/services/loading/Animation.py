import tkinter as tk
from threading import Thread, Event
from time import sleep


class Animation(Thread):
    def __init__(self, master: tk.Canvas, event: Event):
        super().__init__()
        self.master = master
        self.event = event

    def run(self):
        self.radius = 50
        self.angle = 360
        self.speed = 10
        self.create_forms()
        while not self.event.is_set():
            sleep(0.05)
            self.update()
        del self.arc

    def create_forms(self):
        self.master.create_oval(
            self.master.center_x - self.radius, self.master.center_y - self.radius,
            self.master.center_x + self.radius, self.master.center_y + self.radius,
            outline="#EA2027", width=10,
        )
        self.master.create_oval(
            self.master.center_x - self.radius, self.master.center_y - self.radius,
            self.master.center_x + self.radius, self.master.center_y + self.radius,
            outline="#EA2027", width=10,
        )

        self.arc = self.master.create_arc(
            self.master.center_x - self.radius, self.master.center_y - self.radius,
            self.master.center_x + self.radius, self.master.center_y + self.radius,
            start=180, extent=0, outline="#EA2027", width=10, style=tk.ARC
        )

    def draw_arc(self):
        self.master.itemconfig(
            self.arc,
            extent=self.angle,
            outline="#f1f2f6"
        )

    def update(self):
        self.angle -= self.speed
        if self.angle <= 0:
            self.angle = 360
        self.draw_arc()
