import tkinter as tk
from tkinter import messagebox as msb
import requests


import app.utils.forecast_for_days as forecast
import app.utils.api_error as error
import app.gui.weather_window as weather_window
import app.utils.default_settings_manager as settings_manager
import app.gui.settings_info_window as settings_info_window


class MainFrame(tk.Frame):

    """
        Class contains main window components - main frame
    """

    DEFAULT_AMOUNT_OF_DAYS = 7
    BACKGROUND_COLOUR = '#6BC0EE'
    TEXT_COLOUR = 'white'
    FONT = "Microsoft YaHei"
    TEMPERATURE_SYMBOLS = [u'\u2103', 'K', u'\u2109']
    WIND_SYMBOLS = ['km/h', 'm/s', 'mph', 'kn']

    def __init__(self, master=None):
        # init self
        tk.Frame.__init__(self, master, bg=self.BACKGROUND_COLOUR)
        self.pack()

        # values
        self.__city_name = tk.StringVar()
        self.__chosen_temperature = tk.StringVar()
        self.__chosen_wind = tk.StringVar()
        self.__temperature_radiobuttons = []
        self.__wind_radiobuttons = []

        # frames for components
        # components are initialized in init methods
        self.__logo_frame = tk.Frame(self, bg=self.BACKGROUND_COLOUR)
        self.__logo_frame.pack()
        self.__search_frame = tk.Frame(self, bg=self.BACKGROUND_COLOUR)
        self.__search_frame.pack(pady=0)
        self.__wind_frame = tk.Frame(self, bg=self.BACKGROUND_COLOUR)
        self.__wind_frame.pack(pady=0)
        self.__temperature_frame = tk.Frame(self, bg=self.BACKGROUND_COLOUR)
        self.__temperature_frame.pack()
        self.__settings_frame = tk.Frame(self, bg=self.BACKGROUND_COLOUR)
        self.__settings_frame.pack()

        # init components in their frames
        self.__init_app_logo()
        self.__init_entry_field()
        self.__init_search_button()
        self.__init_wind_radiobuttons()
        self.__init_temperature_radiobuttons()
        self.__init_settings_buttons()
        self.__init_show_settings_button()

        # set default values in fields
        self.__default_settings_manager = settings_manager.DefaultSettingsManager()
        self.__set_default_values_in_fields()

        # bind enter with search button
        self.__entry.bind('<Return>', lambda event: self.__search_button_clicked(self.__city_name.get(),
                                                                                 self.__chosen_temperature.get(),
                                                                                 self.__chosen_wind.get()))

    def __init_app_logo(self):
        self.__logo = tk.Label(self.__logo_frame, text="Weather Forecast", bg=self.BACKGROUND_COLOUR,
                               fg=self.TEXT_COLOUR, font=(self.FONT, 38))
        self.__logo.pack(pady=(80, 10))

    def __init_entry_field(self):
        self.__entry = tk.Entry(self.__search_frame, textvariable=self.__city_name, width=35, font=(self.FONT, 15))
        self.__entry.grid(row=0, column=0, padx=(0, 5))

    def __init_search_button(self):
        self.__search_button = tk.Button(self.__search_frame, text="Search", bg='#32a7e7', font=(self.FONT, 11), bd=1,
                                         fg=self.TEXT_COLOUR, activeforeground='white', activebackground='#188ecd',
                                         command=lambda: self.__search_button_clicked(self.__city_name.get(),
                                                                                      self.__chosen_temperature.get(),
                                                                                      self.__chosen_wind.get()))
        self.__search_button.grid(row=0, column=1)

    def __init_temperature_radiobuttons(self):
        for i in range(0, len(self.TEMPERATURE_SYMBOLS)):
            r_button = tk.Radiobutton(self.__temperature_frame, text=self.TEMPERATURE_SYMBOLS[i],
                                      variable=self.__chosen_temperature, value=self.TEMPERATURE_SYMBOLS[i],
                                      bg=self.BACKGROUND_COLOUR, font=(self.FONT, 11), activebackground='#6BC0EE')
            r_button.grid(row=0, column=i)
            self.__temperature_radiobuttons.append(r_button)

    def __init_wind_radiobuttons(self):
        for i in range(0, len(self.WIND_SYMBOLS)):
            r_button = tk.Radiobutton(self.__wind_frame, text=self.WIND_SYMBOLS[i], variable=self.__chosen_wind,
                                      value=self.WIND_SYMBOLS[i], bg=self.BACKGROUND_COLOUR, font=(self.FONT, 11),
                                      activebackground=self.BACKGROUND_COLOUR)
            r_button.grid(row=0, column=i)
            self.__wind_radiobuttons.append(r_button)

    def __init_settings_buttons(self):
        self.__set_settings_button = tk.Button(self.__settings_frame, text="Set as default", bg='#32a7e7',
                                               font=(self.FONT, 9), bd=1, fg=self.TEXT_COLOUR, activeforeground='white',
                                               activebackground='#188ecd',
                                               command=lambda: self.__set_as_default_button_clicked())
        self.__set_settings_button.grid(row=0, column=0, pady=(100, 0), padx=(0, 5))

    def __init_show_settings_button(self):
        self.__show_settings_button = tk.Button(self.__settings_frame, text="Show default", bg='#32a7e7',
                                                font=(self.FONT, 9), bd=1, fg=self.TEXT_COLOUR,
                                                activeforeground='white', activebackground='#188ecd',
                                                command=lambda: self.__show_default_settings())
        self.__show_settings_button.grid(row=0, column=1, pady=(100, 0), padx=(5, 0))

    def __search_button_clicked(self, city_name, temp_sign, wind_sign):
        try:
            forecast_for_city = forecast.ForecastForDays(self.DEFAULT_AMOUNT_OF_DAYS)
            forecast_for_city.get_data_for_city(city_name)
            weather_toplevel_window = weather_window.WeatherWindow(self, temp_sign, wind_sign, forecast_for_city)
        except requests.ConnectionError:
            msb.showerror('INTERNET ERROR', 'You have no internet connection.')
        except error.ApiError as err:
            self.__show_error_info(err)

    def __set_as_default_button_clicked(self):
        try:
            self.__default_settings_manager.set_as_default(self.__city_name.get(), self.__chosen_temperature.get(),
                                                           self.__chosen_wind.get())
            msb.showinfo('INFORMATION', 'Changed default settings successfully.')
        except requests.ConnectionError:
            msb.showerror('INTERNET ERROR', 'You have no internet connection. '
                                            'We can not validate your new default city name. Changes were not saved.')
        except IOError:
            msb.showerror('ERROR', 'Problem occurred when saving default settings! '
                                   'Please, check and default settings file.')
        except error.ApiError as err:
            self.__show_error_info(err)

    def __show_default_settings(self):
        try:
            default_values = self.__default_settings_manager.read_from_default_settings()
            if None in default_values:
                msb.showinfo('ERROR', 'Problem occurred when reading default settings! '
                                      'Please, check and correct your default settings. '
                                      'Invalid data will be named as: "Invalid".')
                if default_values[0] is None:
                    default_values[0] = "Invalid"
                if default_values[1] is None:
                    default_values[1] = "Invalid"
                if default_values[2] is None:
                    default_values[2] = "Invalid"

            settings_info_window.SettingsInfoWindow(default_values, self)
        except requests.ConnectionError:
            msb.showinfo('INTERNET ERROR', 'You have no internet connection. '
                                           'We can not validate your default city name.')
            temp_and_wind_values = self.__default_settings_manager.read_from_default_settings_without_city()
            temp_and_wind_values.append("")

            if None in temp_and_wind_values:
                msb.showinfo('ERROR', 'Problem occurred when reading default settings! '
                                      'Please, check and correct your default settings. '
                                      'Invalid data will be named as: "Invalid".')
                if temp_and_wind_values[0] is None:
                    temp_and_wind_values[0] = "Invalid"
                if temp_and_wind_values[1] is None:
                    temp_and_wind_values[1] = "Invalid"

            settings_info_window.SettingsInfoWindow(temp_and_wind_values, self)
        except IOError:
            msb.showerror('ERROR', 'Problem occurred when reading default settings! '
                                   'Please, check your default settings file')

    def __set_default_values_in_fields(self):
        try:
            default_values = self.__default_settings_manager.read_from_default_settings()

            if default_values[2] is None:
                self.__city_name.set("")
            else:
                self.__city_name.set(default_values[2])

            if default_values[1] is None:
                self.__chosen_temperature.set(self.TEMPERATURE_SYMBOLS[0])
            else:
                self.__chosen_temperature.set(default_values[1])

            if default_values[0] is None:
                self.__chosen_wind.set(self.WIND_SYMBOLS[0])
            else:
                self.__chosen_wind.set(default_values[0])

            if None in default_values:
                msb.showinfo('ERROR', 'Problem occurred when reading default settings! '
                                      'Please, check and correct your default settings. '
                                      'Incorrect values were replaced with default values of application.')
        except requests.ConnectionError:
            msb.showinfo('INTERNET ERROR',
                         'You have no internet connection. We can not validate your default city name')
            self.__city_name.set("")
            temp_and_wind_values = self.__default_settings_manager.read_from_default_settings_without_city()

            if temp_and_wind_values[1] is None:
                self.__chosen_temperature.set(self.TEMPERATURE_SYMBOLS[0])
            else:
                self.__chosen_temperature.set(temp_and_wind_values[1])

            if temp_and_wind_values[0] is None:
                self.__chosen_wind.set(self.WIND_SYMBOLS[0])
            else:
                self.__chosen_wind.set(temp_and_wind_values[0])

            if None in temp_and_wind_values:
                msb.showinfo('ERROR', 'Problem occurred when reading default settings! '
                                      'Please, check and correct your default settings. '
                                      'Incorrect values were replaced with default values of application.')

        except IOError:
            self.__city_name.set("")
            self.__chosen_temperature.set(self.TEMPERATURE_SYMBOLS[0])
            self.__chosen_wind.set(self.WIND_SYMBOLS[0])
            msb.showerror('ERROR', 'Problem occurred when reading default settings! '
                                   'Please, check and correct your default settings. '
                                   'Incorrect values were replaced with default values of application.')

    def __show_error_info(self, err):
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
