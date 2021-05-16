import tkinter as tk
from PIL import Image, ImageTk


import app.gui.weather_details_window as details


BACKGROUND_COLOUR = 'white'
FOREGROUND_COLOUR = 'black'
FONT = "Microsoft YaHei"


class WeatherFrameForDay(tk.Frame):
    """
        Class contains basic information about weather forecast
    """

    CELSIUS_SIGN = u'\u2103'
    KELVIN_SIGN = 'K'
    FAHRENHEIT_SIGN = u'\u2109'
    METERS_PER_SECOND_SIGN = 'm/s'
    MILES_PER_HOUR_SIGN = 'mph'
    KILOMETERS_PER_HOUR_SIGN = 'km/h'
    KNOTS_SIGN = 'kn'

    def __init__(self, weather_for_day, city_name, country_short, temp_sign, wind_sign, master=None):
        tk.Frame.__init__(self, master, bg=BACKGROUND_COLOUR, bd=5)

        # values
        self.__weather_for_day = weather_for_day
        self.__temp_sign = temp_sign
        self.__wind_sign = wind_sign
        self.__city_name = city_name
        self.__country_short = country_short

        # init img
        self.__render = ImageTk.PhotoImage(Image.open(f'img\{self.__weather_for_day.icon_code}.png'))
        self.__img = tk.Label(self, image=self.__render, bg=BACKGROUND_COLOUR)
        self.__img.image = self.__render
        self.__img.pack(padx=10)

        # init date label
        self.__date_label = tk.Label(self, text=f'{self.__weather_for_day.day_name}', bg=BACKGROUND_COLOUR,
                                     fg=FOREGROUND_COLOUR, font=(FONT, 13))
        self.__date_label.pack()

        # init temperature label
        self.__temperature = ""
        if temp_sign == self.CELSIUS_SIGN:
            self.__temperature = self.__weather_for_day.temperature_for_day_in_celsius
        elif temp_sign == self.KELVIN_SIGN:
            self.__temperature = self.__weather_for_day.temperature_for_day_in_kelvins
        else:
            self.__temperature = self.__weather_for_day.temperature_for_day_in_fahrenheit

        self.__temperature_label = tk.Label(self, text=f'{self.__temperature}', bg=BACKGROUND_COLOUR,
                                            fg=FOREGROUND_COLOUR, font=(FONT, 18, 'bold'))
        self.__temperature_label.pack()

        # init description for the weather label
        self.__weather_description_label = tk.Label(self, text=self.__weather_for_day.weather_description,
                                                    bg=BACKGROUND_COLOUR, fg=FOREGROUND_COLOUR, font=(FONT, 13))
        self.__weather_description_label.pack()

        # init "more" button, which opens WeatherDetailsWindow instance top lavel window
        self.__more_button = tk.Button(self, text='more', font=(FONT, 11), bd=1,
                                       command=lambda: self.__more_button_clicked())
        self.__more_button.pack(pady=5)

    def __more_button_clicked(self):
        more = details.WeatherDetailsWindow(self.__weather_for_day, self.__temp_sign, self.__wind_sign,
                                            self.__city_name, self.__country_short, self)
