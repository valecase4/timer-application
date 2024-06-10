from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from .functions import converter
from .buttons import PlayBtn, PauseBtn, ResetBtn
from .spinbox import Spinbox

class TimerFrame(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkTabview, width: int = 500, height: int = 500):
        super().__init__(master, width=width, height=height)

        self.timer_seconds = 0
        self.timer_on = False
        self.after_id = None
        self.circle_decrease = None

        self.hours_spinbox = Spinbox(self, controller=self)
        self.hours_spinbox.place(x=20, y=75)

        self.minutes_spinbox = Spinbox(self, controller=self)
        self.minutes_spinbox.place(x=173, y=75)

        self.seconds_spinbox = Spinbox(self, controller=self)
        self.seconds_spinbox.place(x=326, y=75)
        
        self.configure(fg_color='black')
        self.pack_propagate(False)

        self.timer_canvas = Canvas(self, width=350, height=350, background='black', highlightthickness=0)
        self.timer_canvas.pack(pady=(175, 0))

        self.circle_progress = self.timer_canvas.create_arc(10, 10, 340, 340, width=5, outline='white', start=90, extent=-359.9, style='arc')

        self.timer = self.timer_canvas.create_text(175, 135, text='00:00:00', fill='white', font=ctk.CTkFont(family="Tahoma", size=35, weight='bold'))

        self.play_icon = PlayBtn(master=self.timer_canvas, controller=self)
        self.play_icon.place(x=60, y=170)

        self.pause_icon = PauseBtn(master=self.timer_canvas, controller=self)
        self.pause_icon.place(x=140, y=170)

        self.reset_icon = ResetBtn(master=self.timer_canvas, controller=self)
        self.reset_icon.place(x=220, y=170)

    def update_btns(self) -> None:
        """
        This function updates the states for the three buttons that user uses to manage the timer (play, pause, restart)
        - If the timer is running: 
            - play button disabled
            - pause button normal 
            - restart button disabled
        If the timer is not running: 
            - play button normal
            - pause button disabled
            - restart button normal 
        """

        if self.timer_on:
            self.play_icon.disable()
            self.pause_icon.enable()
            self.reset_icon.disable()

            for f in (self.hours_spinbox, self.minutes_spinbox, self.seconds_spinbox):
                f.all_disabled()

        else:
            self.play_icon.enable()
            self.pause_icon.disable()
            self.reset_icon.enable()

            for f in (self.hours_spinbox, self.minutes_spinbox, self.seconds_spinbox):
                f.reset()
        
    def update_timer(self) -> None:
        """
        This function automatically updates the timer that is 
        displayed to the user when the user uses spinbox
        """

        hours = int(self.hours_spinbox.get_value())
        minutes = int(self.minutes_spinbox.get_value())
        seconds = int(self.seconds_spinbox.get_value())

        self.timer_seconds = self.get_seconds(hours, minutes, seconds)
        time_string = converter(self.timer_seconds)
        self.timer_canvas.itemconfig(self.timer, text=time_string)

    def reset_circle_progress(self, event: Event) -> None:
        """
        When user modifies time for timer, the circle progress is reset
        """

        self.timer_canvas.itemconfig(self.circle_progress, extent=-359.9)

    def get_seconds(self, hours: int, minutes: int, seconds: int) -> int:
        """
        This function takes number of hours, minutes and seconds and computes the corresponding total amount
        of seconds

        :param hours: hours value
        :param minutes: minutes value
        :param seconds: seconds value
        :return: total amount of seconds
        """

        return hours * 3600 + minutes * 60 + seconds
    
    def start(self, event: Event) -> None:
        """
        This function checks the validity of the user input
        - If the input is valid:
            Timer starts (counter function is called)
        - If the input is not valid:
            An error occurs and is displayed
        """

        hours, minutes, seconds = map(int, self.timer_canvas.itemcget(self.timer, 'text').split(':'))

        if hours == 0 and minutes == 0 and seconds == 0:
            messagebox.showerror('Error', 'Invalid time. Please set a duration greater than zero')
        else:
            self.timer_on = True

            for spinbox in (self.hours_spinbox, self.minutes_spinbox, self.seconds_spinbox):
                spinbox.value_entry.delete(0, END)
                spinbox.value_entry.insert(0, 0)

            self.circle_decrease = 360 / self.timer_seconds

            self.timer_seconds = self.get_seconds(hours, minutes, seconds)

            self.update_btns()

            self.counter()

    
    
    def counter(self) -> None:
        """
        This function actually manages the timer flow decreasing the total amount of seconds by 1 every seconds and
        visually updating the state of timer and the state of progress circle representing the time flow
        When timer reaches time zero, an info will be displayed to the user
        """

        self.timer_seconds -= 1
        time_string = converter(self.timer_seconds)
        self.timer_canvas.itemconfig(self.timer, text=time_string)

        current_extent = float(self.timer_canvas.itemconfig(self.circle_progress)['extent'][4])

        self.timer_canvas.itemconfig(self.circle_progress, extent=current_extent + self.circle_decrease)

        if self.timer_seconds >= 1:
            self.after_id = self.after(1000, self.counter)
        else:
            self.timer_canvas.itemconfig(self.circle_progress, extent=360)

            res = messagebox.showinfo('Info', 'Time\'s up! Your timer has finished')

            if res == 'ok':
                self.reset()

    def pause(self, event: Event) -> None:
        """
        This function manages the pauses for timer
        When it is called, the timer flow is temporarliy stopped
        """

        self.timer_on = False
        self.update_btns()
        
        if self.after_id:
            self.after_cancel(self.after_id)

    def reset(self, *event: Event) -> None:
        """
        This function resets the settings for timer by default
        """

        self.timer_on = False

        self.timer_canvas.itemconfig(self.timer, text='00:00:00')
        self.timer_canvas.itemconfig(self.circle_progress, extent=-359.9)
        self.update_btns()

        for spinbox in (self.hours_spinbox, self.minutes_spinbox, self.seconds_spinbox):
            spinbox.value_entry.delete(0, END)
            spinbox.value_entry.insert(0, 0)

        self.timer_seconds = 0
        self.circle_decrease = None

        if self.after_id:
            self.after_cancel(self.after_id)
        
