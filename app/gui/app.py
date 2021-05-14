import tkinter as tk


from main_frame import MainFrame

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Weather Forecast")
    root.minsize(500, 300)
    root.geometry('700x433')
    root.config(background='#6BC0EE')
    app = MainFrame(master=root)
    app.mainloop()
