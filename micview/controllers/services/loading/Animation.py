##
# @brief: This class is responsible for creating the animation of the loading screen.
#

# Imports
import tkinter as tk
from threading import Thread, Event
from time import sleep

# Classes
class Animation(Thread):
    """!
    @brief: This class is responsible for creating the animation of the loading screen.
    """
    def __init__(self, master: tk.Canvas, event: Event) -> None:
        """!
        @brief: The constructor of the class.
        @param: master: tk.Canvas - The canvas of the loading screen.
        @param: event: Event - The event of the loading screen.
        """
        super().__init__()
        self.master: tk.Canvas = master
        self.event: Event = event

    def run(self) -> None:
        """!
        @brief: The run method of the class.
        @return: None
        """
        self.radius = 50
        self.angle = 360
        self.speed = 10
        self.createForms()
        while not self.event.is_set():
            sleep(0.05)
            self.update()
        del self.arc

    def createForms(self) -> None:
        """!
        @brief: This method is responsible for creating the forms of the animation.
        @return: None
        """
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

    def drawArc(self) -> None:
        """!
        @brief: This method is responsible for drawing the arc of the animation.
        @return: None
        """
        self.master.itemconfig(
            tagOrId=self.arc,
            extent=self.angle,
            outline="#f1f2f6"
        )

    def update(self) -> None:
        """!
        @brief: This method is responsible for updating the animation.
        @return: None
        """
        self.angle -= self.speed
        if self.angle <= 0:
            self.angle = 360
        self.drawArc()
