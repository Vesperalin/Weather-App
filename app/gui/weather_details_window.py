import tkinter as tk
from PIL import Image, ImageTk


# TODO - add docs
class WeatherDetailsWindow(tk.Toplevel):
    CELSIUS_SIGN = u'\u2103'
    KELVIN_SIGN = 'K'
    FAHRENHEIT_SIGN = u'\u2109'
    METERS_PER_SECOND_SIGN = 'm/s'
    MILES_PER_HOUR_SIGN = 'mph'
    KILOMETERS_PER_HOUR_SIGN = 'km/h'
    KNOTS_SIGN = 'kn'

    def __init__(self, weather_for_day, temp_sign, wind_sign, city_name, country_short, master=None):
        super().__init__(master)
        self.__weather_for_day = weather_for_day
        self.__temp_sign = temp_sign
        self.__wind_sign = wind_sign
        self.__city_name = city_name
        self.__country_short = country_short
        self.minsize(100, 100)

        # frames for components
        self.__frame = tk.Frame(self)
        self.__frame.pack()

        # frame for icon
        self.__icon_frame = tk.Frame(self.__frame, bg='blue', width=100, height=50)
        self.__icon_frame.grid(row=0, column=0, columnspan=2)

        # frame for description
        self.__description_frame = tk.Frame(self.__frame, bg='pink', width=100, height=50)
        self.__description_frame.grid(row=1, column=0, columnspan=2)

        # frame for date and day
        self.__date_frame = tk.Frame(self.__frame, bg='yellow', width=100, height=50)
        self.__date_frame.grid(row=2, column=0, columnspan=2)

        # frame for sunrise
        self.__sunrise_frame = tk.Frame(self.__frame, bg='green', width=100, height=50)
        self.__sunrise_frame.grid(row=3, column=0)

        # frame for sunset
        self.__sunset_frame = tk.Frame(self.__frame, bg='white', width=100, height=50)
        self.__sunset_frame.grid(row=3, column=1)

        # frame for temperature
        self.__temperature_frame = tk.Frame(self.__frame, bg='pink', width=100, height=50)
        self.__temperature_frame.grid(row=4, column=0)

        # frame for temperature - feels like
        self.__temperature_feels_like_frame = tk.Frame(self.__frame, bg='red', width=100, height=50)
        self.__temperature_feels_like_frame.grid(row=4, column=1)

        # frame for pressure
        self.__pressure_frame = tk.Frame(self.__frame, bg='green', width=100, height=50)
        self.__pressure_frame.grid(row=5, column=0, columnspan=2)

        # frame for humidity
        self.__humidity_frame = tk.Frame(self.__frame, bg='brown', width=100, height=50)
        self.__humidity_frame.grid(row=6, column=0, columnspan=2)

        # frame for wind speed
        self.__wind_speed_frame = tk.Frame(self.__frame, bg='pink', width=100, height=50)
        self.__wind_speed_frame.grid(row=7, column=0, columnspan=2)

        # frame for cloudiness
        self.__cloudiness_frame = tk.Frame(self.__frame, bg='yellow', width=100, height=50)
        self.__cloudiness_frame.grid(row=8, column=0, columnspan=2)

        # init components in their frames
        self.__init_icon()
        self.__init_description()
        self.__init_date_and_day_name()
        self.__init_sunrise()
        self.__init_sunset()
        self.__init_temperature()
        self.__init_temperature_feels_like()

    def __init_icon(self):
        self.__render = ImageTk.PhotoImage(Image.open(f'img\{self.__weather_for_day.icon_code}.png'))
        self.__img = tk.Label(self.__icon_frame, image=self.__render, bg='white')
        self.__img.image = self.__render
        self.__img.pack()

    def __init_description(self):
        self.__weather_description_label = tk.Label(self.__description_frame, bg='white', fg='black',
                                                    font=("Microsoft YaHei", 13),
                                                    text=self.__weather_for_day.weather_description)
        self.__weather_description_label.pack()

    def __init_date_and_day_name(self):
        self.__date_and_day_label = tk.Label(self.__date_frame, text=f'{self.__weather_for_day.day_name}, '
                                                                     f'{self.__weather_for_day.date}',
                                             bg='white', fg='black', font=("Microsoft YaHei", 13))
        self.__date_and_day_label.pack()

    def __init_sunrise(self):
        self.__sunrise_label = tk.Label(self.__sunrise_frame, text=f'Sunrise: {self.__weather_for_day.sunrise}',
                                        bg='white', fg='black', font=("Microsoft YaHei", 13))
        self.__sunrise_label.pack()

    def __init_sunset(self):
        self.__sunset_label = tk.Label(self.__sunset_frame, text=f'Sunrise: {self.__weather_for_day.sunset}',
                                       bg='white', fg='black', font=("Microsoft YaHei", 13))
        self.__sunset_label.pack()

    def __init_temperature(self):
        self.__temp_day = ""
        self.__temp_morn = ""
        self.__temp_eve = ""
        self.__temp_night = ""
        if self.__temp_sign == self.CELSIUS_SIGN:
            self.__temp_day = self.__weather_for_day.temperature_for_day_in_celsius
            self.__temp_morn = self.__weather_for_day.temperature_for_morning_in_celsius
            self.__temp_eve = self.__weather_for_day.temperature_for_evening_in_celsius
            self.__temp_night = self.__weather_for_day.temperature_for_night_in_celsius
        elif self.__temp_sign == self.FAHRENHEIT_SIGN:
            self.__temp_day = self.__weather_for_day.temperature_for_day_in_fahrenheit
            self.__temp_morn = self.__weather_for_day.temperature_for_morning_in_fahrenheit
            self.__temp_eve = self.__weather_for_day.temperature_for_evening_in_fahrenheit
            self.__temp_night = self.__weather_for_day.temperature_for_night_in_fahrenheit
        else:
            self.__temp_day = self.__weather_for_day.temperature_for_day_in_kelvins
            self.__temp_morn = self.__weather_for_day.temperature_for_morning_in_kelvins
            self.__temp_eve = self.__weather_for_day.temperature_for_evening_in_kelvins
            self.__temp_night = self.__weather_for_day.temperature_for_night_in_kelvins

        self.__temp_day_label = tk.Label(self.__temperature_frame, text=f'Temperature for day: {self.__temp_day}',
                                         bg='white', fg='black', font=("Microsoft YaHei", 13))
        self.__temp_morn_label = tk.Label(self.__temperature_frame, text=f'Temperature in the morning: '
                                                                         f'{self.__temp_morn}',
                                          bg='white', fg='black', font=("Microsoft YaHei", 13))
        self.__temp_eve_label = tk.Label(self.__temperature_frame, text=f'Temperature in the evening: '
                                                                        f'{self.__temp_eve}',
                                         bg='white', fg='black', font=("Microsoft YaHei", 13))
        self.__temp_night_label = tk.Label(self.__temperature_frame, text=f'Temperature in the night: '
                                                                          f'{self.__temp_night}',
                                           bg='white', fg='black', font=("Microsoft YaHei", 13))
        self.__temp_day_label.pack()
        self.__temp_morn_label.pack()
        self.__temp_eve_label.pack()
        self.__temp_night_label.pack()

    def __init_temperature_feels_like(self):
        self.__temp_day_feels_like = ""
        self.__temp_morn_feels_like = ""
        self.__temp_eve_feels_like = ""
        self.__temp_night_feels_like = ""
        if self.__temp_sign == self.CELSIUS_SIGN:
            self.__temp_day_feels_like = self.__weather_for_day.temperature_feels_like_for_day_in_celsius
            self.__temp_morn_feels_like = self.__weather_for_day.temperature_feels_like_for_morning_in_celsius
            self.__temp_eve_feels_like = self.__weather_for_day.temperature_feels_like_for_evening_in_celsius
            self.__temp_night_feels_like = self.__weather_for_day.temperature_feels_like_for_night_in_celsius
        elif self.__temp_sign == self.FAHRENHEIT_SIGN:
            self.__temp_day_feels_like = self.__weather_for_day.temperature_feels_like_for_day_in_fahrenheit
            self.__temp_morn_feels_like = self.__weather_for_day.temperature_feels_like_for_morning_in_fahrenheit
            self.__temp_eve_feels_like = self.__weather_for_day.temperature_feels_like_for_evening_in_fahrenheit
            self.__temp_night_feels_like = self.__weather_for_day.temperature_feels_like_for_night_in_fahrenheit
        else:
            self.__temp_day_feels_like = self.__weather_for_day.temperature_feels_like_for_day_in_kelvins
            self.__temp_morn_feels_like = self.__weather_for_day.temperature_feels_like_for_morning_in_kelvins
            self.__temp_eve_feels_like = self.__weather_for_day.temperature_feels_like_for_evening_in_kelvins
            self.__temp_night_feels_like = self.__weather_for_day.temperature_feels_like_for_night_in_kelvins

        self.__temp_day_feels_like_label = tk.Label(self.__temperature_feels_like_frame,
                                                    text=f'feels like: {self.__temp_day_feels_like}',
                                                    bg='white', fg='black', font=("Microsoft YaHei", 13))

        self.__temp_morn_feels_like_label = tk.Label(self.__temperature_feels_like_frame,
                                                     text=f'feels like: {self.__temp_morn_feels_like}',
                                                     bg='white', fg='black', font=("Microsoft YaHei", 13))
        self.__temp_eve_feels_like_label = tk.Label(self.__temperature_feels_like_frame,
                                                    text=f'feels like: {self.__temp_eve_feels_like}',
                                                    bg='white', fg='black', font=("Microsoft YaHei", 13))
        self.__temp_night_feels_like_label = tk.Label(self.__temperature_feels_like_frame,
                                                      text=f'feels like: {self.__temp_night_feels_like}',
                                                      bg='white', fg='black', font=("Microsoft YaHei", 13))
        self.__temp_day_feels_like_label.pack()
        self.__temp_morn_feels_like_label.pack()
        self.__temp_eve_feels_like_label.pack()
        self.__temp_night_feels_like_label.pack()

    #TODO - add rest of the elements