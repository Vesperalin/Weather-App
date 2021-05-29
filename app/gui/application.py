import tkinter as tk


import app.gui.main_frame as main_frame


"""
    Creates the Tk for the gui
"""


def main():
    root = tk.Tk()
    root.title("Weather Forecast")
    root.minsize(500, 400)
    root.geometry('700x433')
    root.config(background='#6BC0EE')
    icon = tk.PhotoImage(file='img\icon.png')
    root.iconphoto(False, icon)
    app = main_frame.MainFrame(master=root)
    app.mainloop()
