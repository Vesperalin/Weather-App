import tkinter as tk
from tkinter import messagebox as msb


import app.utils.forecast_for_days as forecast
import app.utils.api_error as error
import app.gui.weather_window as weather_window


DEFAULT_AMOUNT_OF_DAYS = 7


# TODO - add docs
class MainFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, bg='#6BC0EE', height=100, width=100)
        self.pack()

        # values
        self.__city_name = tk.StringVar()
        self.__chosen_temperature = tk.StringVar()
        self.__chosen_wind = tk.StringVar()
        self.__temperature_radiobuttons = []
        self.__wind_radiobuttons = []

        # frames for components
        self.__title_frame = tk.Frame(self, bg='#6BC0EE')
        self.__title_frame.pack()
        self.__search_frame = tk.Frame(self, bg='#6BC0EE')
        self.__search_frame.pack(pady=0)
        self.__wind_frame = tk.Frame(self, bg='#6BC0EE')
        self.__wind_frame.pack(pady=0)
        self.__temperature_frame = tk.Frame(self, bg='#6BC0EE')
        self.__temperature_frame.pack()

        # init components in their frames
        self.__init_app_logo()
        self.__init_entry_field()
        self.__init_search_button()
        self.__init_wind_radiobuttons()
        self.__init_temperature_radiobuttons()

        # bind clicking enter with clicking search button
        self.__entry.bind('<Return>', lambda event: self.__search_button_clicked(self.__city_name.get(),
                                                                                 self.__chosen_temperature.get(),
                                                                                 self.__chosen_wind.get()))

    def __init_app_logo(self):
        self.__logo = tk.Label(self.__title_frame, text="Weather Forecast", bg='#6BC0EE', fg='white',
                               font=("Microsoft YaHei", 38))
        self.__logo.pack(pady=(80, 10))

    def __init_entry_field(self):
        self.__city_name.set("")
        self.__entry = tk.Entry(self.__search_frame, textvariable=self.__city_name, width=35,
                                font=("Microsoft YaHei", 15))
        self.__entry.grid(row=0, column=0, padx=(0, 5))

    def __init_search_button(self):
        self.__search_button = tk.Button(self.__search_frame, text="Search", bg='#32a7e7', font=("Microsoft YaHei", 11),
                                         fg='white', activeforeground='white', activebackground='#188ecd', bd=1,
                                         command=lambda: self.__search_button_clicked(self.__city_name.get(),
                                                                                      self.__chosen_temperature.get(),
                                                                                      self.__chosen_wind.get()))
        self.__search_button.grid(row=0, column=1)

    def __init_temperature_radiobuttons(self):
        symbols = [u'\u2103', 'K', u'\u2109']
        for i in range(0, len(symbols)):
            r_button = tk.Radiobutton(self.__temperature_frame, text=symbols[i], variable=self.__chosen_temperature,
                                      value=symbols[i], bg='#6BC0EE', font=("Microsoft YaHei", 11),
                                      activebackground='#6BC0EE')
            r_button.grid(row=0, column=i)
            self.__temperature_radiobuttons.append(r_button)
        self.__chosen_temperature.set(symbols[0])

    def __init_wind_radiobuttons(self):
        symbols = ['km/h', 'm/s', 'mph', 'kn']
        for i in range(0, len(symbols)):
            r_button = tk.Radiobutton(self.__wind_frame, text=symbols[i], variable=self.__chosen_wind,
                                      value=symbols[i], bg='#6BC0EE', font=("Microsoft YaHei", 11),
                                      activebackground='#6BC0EE')
            r_button.grid(row=0, column=i)
            self.__wind_radiobuttons.append(r_button)
        self.__chosen_wind.set(symbols[0])

    def __search_button_clicked(self, city_name, temp_sign, wind_sign):
        try:
            forecast_for_city = forecast.ForecastForDays(DEFAULT_AMOUNT_OF_DAYS)
            forecast_for_city.get_data_for_city(city_name)
            weather_toplevel_window = weather_window.WeatherWindow(self, temp_sign, wind_sign, forecast_for_city)
        except error.ApiError as err:
            if err.error_code == 401:
                msb.showerror(f'{err.error_code} ERROR',
                              'An application error has occurred. Contact administrator immediately!')
            elif err.error_code == 400:
                msb.showerror(f'{err.error_code} ERROR', 'You did not give a city name')
            elif err.error_code == 404:
                msb.showerror(f'{err.error_code} ERROR',
                              'This city does not exist or you gave incorrect city name!')
            elif err.error_code == 429:
                msb.showerror(f'{err.error_code} ERROR', 'You did to many requests!')
            else:
                msb.showerror(f'{err.error_code} ERROR', 'Unknown error occurred!')
