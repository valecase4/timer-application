from tkinter import *
import customtkinter as ctk
from .timer import TimerFrame
from .main import MainFrame
from .stopwatch import StopwatchFrame

class Root(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.title("Timer App")
        self.geometry("500x500+300+300")
        self.resizable(width=False, height=False)

        self.update_idletasks()

        tab_view = ctk.CTkTabview(self, width=500, height=500)

        tab_view.add("Home")
        tab_view.add("Timer")
        tab_view.add("Stopwatch")

        tab_view.pack()

        main_frame = MainFrame(master=tab_view.tab("Home"))
        main_frame.pack()

        timer_frame = TimerFrame(master=tab_view.tab("Timer"))
        timer_frame.pack()

        stopwatch_frame = StopwatchFrame(master=tab_view.tab("Stopwatch"))
        stopwatch_frame.pack()
