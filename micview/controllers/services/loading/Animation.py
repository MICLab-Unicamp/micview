import tkinter as tk
from threading import Thread, Event
from time import sleep


class Animation(Thread):
    def __init__(self, master: tk.Canvas, event: Event) -> None:
        super().__init__()
        self.master: tk.Canvas = master
        self.event: Event = event

    def run(self) -> None:
        self.radius = 50
        self.angle = 360
        self.speed = 10
        self.create_forms()
        while not self.event.is_set():
            sleep(0.05)
            self.update()
        del self.arc

    def create_forms(self) -> None:
        self.master.create_oval(
            self.master.centerX - self.radius, self.master.centerY - self.radius,
            self.master.centerX + self.radius, self.master.centerY + self.radius,
            outline="#EA2027", width=10,
        )
        self.master.create_oval(
            self.master.centerX - self.radius, self.master.centerY - self.radius,
            self.master.centerX + self.radius, self.master.centerY + self.radius,
            outline="#EA2027", width=10,
        )

        self.arc = self.master.create_arc(
            self.master.centerX - self.radius, self.master.centerY - self.radius,
            self.master.centerX + self.radius, self.master.centerY + self.radius,
            start=180, extent=0, outline="#EA2027", width=10, style=tk.ARC
        )

    def draw_arc(self) -> None:
        self.master.itemconfig(
            tagOrId=self.arc,
            extent=self.angle,
            outline="#f1f2f6"
        )

    def update(self) -> None:
        self.angle -= self.speed
        if self.angle <= 0:
            self.angle = 360
        self.draw_arc()
