from tkinter import *
import customtkinter as ctk
from datetime import datetime

class MainFrame(ctk.CTkFrame):
    def __init__(self, master, width=500, height=500):
        super().__init__(master, width=width, height=height)

        self.seconds = 60
        self.after_id = None

        now = datetime.now()

        self.current_date = ctk.CTkLabel(self, 
                                         text=now.strftime("%d/%m/%Y"), 
                                         font=ctk.CTkFont(family="Tahoma", size=30)
                                         )
        self.current_date.pack(pady=(150, 0))

        self.current_time = ctk.CTkLabel(self, 
                                         text=now.strftime("%H:%M:%S"), 
                                         font=ctk.CTkFont(family="Tahoma", size=30, weight='bold')
                                         )
        self.current_time.pack(pady=(30, 0))

        self.configure(fg_color='black')
        self.pack_propagate(False)

        self.update_current_datetime()

    def update_current_datetime(self):
        """
        This function updates and displays on the root current date and current time (hh:mm:ss format)
        """

        now = datetime.now()

        current_date = now.strftime("%d/%m/%Y")
        current_time = now.strftime("%H:%M:%S")

        self.current_date.configure(text=current_date)
        self.current_time.configure(text=current_time)

        self.after(1000, self.update_current_datetime)



