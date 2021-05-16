import tkinter as tk


import app.gui.main_frame as main_frame


def main():
    root = tk.Tk()
    root.title("Weather Forecast")
    root.minsize(500, 300)
    root.geometry('700x433')
    root.config(background='#6BC0EE')
    app = main_frame.MainFrame(master=root)
    app.mainloop()


if __name__ == '__main__':
    pass
