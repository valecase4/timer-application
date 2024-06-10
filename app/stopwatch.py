from tkinter import *
import customtkinter as ctk
from .functions import converter
from .buttons import PlayBtn, PauseBtn, ResetBtn

class StopwatchFrame(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkTabview, width: int = 500, height: int = 500):
        super().__init__(master, width=width, height=height)

        self.stopwatch_seconds = 0
        self.stopwatch_on = False
        self.after_id = None

        self.configure(fg_color='black')
        self.pack_propagate(False)

        self.stopwatch = ctk.CTkLabel(self, text="00:00:00", font=ctk.CTkFont(family="Tahoma", size=35, weight='bold'))
        self.stopwatch.pack(pady=(150, 0))

        self.play_icon = PlayBtn(master=self, controller=self)
        self.play_icon.place(x=180, y=275)

        self.pause_icon = PauseBtn(master=self, controller=self)
        self.pause_icon.place(x=265, y=275)

        self.reset_icon = ResetBtn(master=self, controller=self)
        self.reset_icon.place(x=350, y=275)

    def start(self, event: Event) -> None:
        """
        This function initiates the stopwatch calling counter function
        """

        self.stopwatch_on = True
        self.update_btns()
        self.counter()

    def pause(self, event: Event) -> None:
        """
        This function manages the pauses for stopwatch
        When it is called, the stopwatch is temporarliy stopped
        """

        self.stopwatch_on = False
        self.update_btns()

        if self.after_id:
            self.after_cancel(self.after_id)

    def reset(self, event: Event) -> None:
        """
        This function resets the settings for stopwatch by default
        """

        self.stopwatch_on = False
        self.update_btns()
        self.stopwatch_seconds = 0
        self.stopwatch.configure(text="00:00:00")

        if self.after_id:
            self.after_cancel(self.after_id)

    def counter(self) -> None:
        """
        This function actually manages the stopwatch flow increasing the total amount of seconds by 1 every seconds and
        visually updating the state of stopwatch
        """

        self.stopwatch_seconds += 1
        time_string = converter(self.stopwatch_seconds)
        self.stopwatch.configure(text=time_string)
        self.after_id = self.after(1000, self.counter)

    def update_btns(self) -> None:
        """
        This function updates the states for the three buttons that user use to manage the stopwatch (play, pause, restart)
        - If the stopwatch is running: 
            - play button disabled
            - pause button normal 
            - restart button disabled
        If the stopwatch is not running: 
            - play button normal
            - pause button disabled
            - restart button normal 
        """
        if self.stopwatch_on:
            self.play_icon.disable()
            self.pause_icon.enable()
            self.reset_icon.disable()
        else:
            self.play_icon.enable()
            self.pause_icon.disable()
            self.reset_icon.enable()



