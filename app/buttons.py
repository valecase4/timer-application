from tkinter import *
import customtkinter as ctk

class PlayBtn(Canvas):
    """
    Play button
    """

    def __init__(self, master: Canvas, controller:  ctk.CTkFrame, width: int = 70, height: int = 70):
        super().__init__(master, width=width, height=height)

        self.controller = controller

        self.config(cursor='hand2', background='black', highlightthickness=0)
        
        self.background_btn = self.create_oval(5, 5, 65, 65, fill='#1f538d', outline='')
        self.create_polygon(22.5, 17.5, 22.5, 52.5, 52.5, 35, fill='white', outline='')

        self.bind("<Button-1>", self.controller.start)

    def disable(self) -> None:
        """
        This functions disables the play button changing its color to gray and making imposssible to click it
        """

        self.itemconfig(self.background_btn, fill='gray')
        self.bind('<Button-1>', lambda event : "break")

    def enable(self) -> None:
        """
        This functions enables the play button changing its color to #1f538d
        """

        self.itemconfig(self.background_btn, fill='#1f538d')
        self.bind('<Button-1>', self.controller.start)


class PauseBtn(Canvas):
    """
    Pause button
    """
    
    def __init__(self, master: Canvas, controller:  ctk.CTkFrame, width: int = 70, height: int = 70):
        super().__init__(master, width=width, height=height)

        self.controller = controller

        self.config(cursor='hand2', background='black', highlightthickness=0)
        
        self.background_btn = self.create_oval(5, 5, 65, 65, fill='#1f538d', outline='')
        self.create_rectangle(20, 20, 30, 55, fill='white', outline='')
        self.create_rectangle(40, 20, 50, 55, fill='white', outline='')

        self.bind("<Button-1>", controller.pause)

    def disable(self) -> None:
        """
        This functions disables the pause button changing its color to gray and making imposssible to click it
        """

        self.itemconfig(self.background_btn, fill='gray')
        self.bind('<Button-1>', lambda event : "break")

    def enable(self) -> None:
        """
        This functions enables the pause button changing its color to #1f538d
        """

        self.itemconfig(self.background_btn, fill='#1f538d')
        self.bind('<Button-1>', self.controller.pause)
        
class ResetBtn(Canvas):
    """
    Reset button
    """
    
    def __init__(self, master: Canvas, controller:  ctk.CTkFrame, width: int = 70, height: int = 70):
        super().__init__(master, width=width, height=height)

        self.controller = controller

        self.config(cursor='hand2', background='black', highlightthickness=0)
        
        self.background_btn = self.create_oval(5, 5, 65, 65, fill='#FF0000', outline='')
        self.create_rectangle(20, 20, 50, 50, fill='white', outline='')

        self.bind("<Button-1>", controller.reset)

    def disable(self) -> None:
        """
        This functions disables the reset button changing its color to gray and making imposssible to click it
        """

        self.itemconfig(self.background_btn, fill='gray')
        self.bind('<Button-1>', lambda event : "break")

    def enable(self) -> None:
        """
        This functions enables the reset button changing its color to #FF0000
        """

        self.itemconfig(self.background_btn, fill='#FF0000')
        self.bind('<Button-1>', self.controller.reset)