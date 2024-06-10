from tkinter import *
import customtkinter as ctk

class Spinbox(ctk.CTkFrame):
    def __init__(self, master, controller, height=40, width=145):
        super().__init__(master, height=height, width=width)

        self.master = master
        self.controller = controller

        self.configure(fg_color='black')
        self.pack_propagate(False)

        self.value_entry = ctk.CTkEntry(self, width=65, height=40, justify='center', bg_color='black')
        self.value_entry.place(x=40, y=0)
        self.value_entry.insert(0, 0)
        self.value_entry.configure(font=ctk.CTkFont(family="Tahoma", size=15, weight='bold'))
        self.value_entry.bind("<KeyPress>", lambda event : "break")
        self.value_entry.bind("<Double-Button-1>", lambda event : "break")

        self.min_btn = ctk.CTkButton(self, width=40, height=40, text='-', cursor='hand2', command=self.decrease)
        self.min_btn.configure(state='disabled')
        self.min_btn.configure(fg_color='gray', text_color='white', text_color_disabled='white', font=ctk.CTkFont(family="Tahoma", size=15, weight='bold'))
        self.min_btn.place(x=0, y=0)

        self.plus_btn = ctk.CTkButton(self, width=40, height=40, text='+', cursor='hand2', command=self.increase)
        self.plus_btn.configure(font=ctk.CTkFont(family="Tahoma", size=15, weight='bold'))
        self.plus_btn.place(x=105, y=0)

        self.plus_btn.bind('<Button-1>', self.controller.reset_circle_progress)
        self.min_btn.bind('<Button-1>', self.controller.reset_circle_progress)

    def all_disabled(self):
        """
        When timer is running, it is impossible to use spinboxes. Both plus and min btns are disabled
        """
        self.min_btn.configure(state='disabled')
        self.plus_btn.configure(state='disabled')

        self.min_btn.unbind('<Button-1>')
        self.plus_btn.unbind('<Button-1>')

    def reset(self):
        """
        When timer is not running, the spinboxes return to the initial state
        """

        self.min_btn.configure(state='disabled')
        self.plus_btn.configure(state='normal')

        self.min_btn.bind('<Button-1>', self.controller.reset_circle_progress)
        self.plus_btn.bind('<Button-1>', self.controller.reset_circle_progress)

    def increase(self):
        """
        This function manages the click on plus button made by user to increase the value in the spinbox
        """

        current_value = self.get_value()

        self.value_entry.delete(0, END)
        self.value_entry.insert(0, current_value+1)

        if current_value >= 58:
            self.plus_btn.configure(state='disabled')

        self.min_btn.configure(state='normal')

        self.master.update_timer()

    def decrease(self):
        """
        This function manages the click on minus button made by user to decrease the value in the spinbox
        """

        current_value = self.get_value()

        if current_value <= 1:
            self.min_btn.configure(state='disabled')

        self.value_entry.delete(0, END)
        self.value_entry.insert(0, current_value-1)

        self.plus_btn.configure(state='normal')

        self.master.update_timer()

    def get_value(self) -> int:
        """
        Getting the value entered into the spinbox
        """
        
        return int(self.value_entry.get())


