import tkinter as tk


class MainFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, bg='#6BC0EE', height=100, width=100)
        self.pack()
        self.__title_frame = tk.Frame(self, bg='#6BC0EE')
        self.__title_frame.pack()
        self.__search_frame = tk.Frame(self, bg='#6BC0EE')
        self.__search_frame.pack(pady=(0, 10))
        self.__wind_frame = tk.Frame(self, bg='#6BC0EE')
        self.__wind_frame.pack(pady=(0, 5))
        self.__temperature_frame = tk.Frame(self, bg='#6BC0EE')
        self.__temperature_frame.pack()

        # init components in frames
        self.__init_app_logo()
        self.__init_entry_field()
        self.__init_search_button()
        self.__init_wind_radiobuttons()
        self.__init_temperature_radiobuttons()

    def __init_app_logo(self):
        self.__logo = tk.Label(self.__title_frame, text="Weather Forecast", bg='#6BC0EE', fg='white',
                               font=("Calibri", 38))
        self.__logo.pack(pady=(80, 10))

    def __init_entry_field(self):
        self.__city_name = tk.StringVar()
        self.__city_name.set("")
        self.__entry = tk.Entry(self.__search_frame, textvariable=self.__city_name, width=35, font=("Calibri", 15))
        self.__entry.grid(row=0, column=0, padx=(0, 5))

    def __init_search_button(self):
        self.__search_button = tk.Button(self.__search_frame, text="Search", bg='#32a7e7', font=("Calibri", 11),
                                         fg='white', activeforeground='white', activebackground='#188ecd',
                                         relief='groove', bd=1)
        self.__search_button.grid(row=0, column=1)

    def __init_temperature_radiobuttons(self):
        symbols = [u'\u2103', 'K', u'\u2109']
        self.__temperature_radiobuttons = []
        self.__chosen_temperature = tk.StringVar()
        for i in range(0, len(symbols)):
            r_button = tk.Radiobutton(self.__temperature_frame, text=symbols[i], variable=self.__chosen_temperature,
                                      value=symbols[i], bg='#6BC0EE', font=("Calibri", 11), activebackground='#6BC0EE')
            r_button.grid(row=0, column=i)
            self.__temperature_radiobuttons.append(r_button)
        self.__chosen_temperature.set(symbols[0])

    def __init_wind_radiobuttons(self):
        symbols = ['km/h', 'm/s', 'mph', 'kn']
        self.__wind_radiobuttons = []
        self.__chosen_wind = tk.StringVar()
        for i in range(0, len(symbols)):
            r_button = tk.Radiobutton(self.__wind_frame, text=symbols[i], variable=self.__chosen_wind,
                                      value=symbols[i], bg='#6BC0EE', font=("Calibri", 11), activebackground='#6BC0EE')
            r_button.grid(row=0, column=i)
            self.__wind_radiobuttons.append(r_button)
        self.__chosen_wind.set(symbols[0])
