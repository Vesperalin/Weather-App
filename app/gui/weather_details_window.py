import tkinter as tk
from PIL import Image, ImageTk


class WeatherDetailsWindow(tk.Toplevel):

    """
        Class contains details about the weather in a day
        This is a second top level window
    """

    BACKGROUND_COLOUR = 'white'
    TEXT_COLOUR = 'black'
    FONT = "Microsoft YaHei"
    CELSIUS_SIGN = u'\u2103'
    KELVIN_SIGN = 'K'
    FAHRENHEIT_SIGN = u'\u2109'
    METERS_PER_SECOND_SIGN = 'm/s'
    MILES_PER_HOUR_SIGN = 'mph'
    KILOMETERS_PER_HOUR_SIGN = 'km/h'
    KNOTS_SIGN = 'kn'

    def __init__(self, weather_for_day, temp_sign, wind_sign, city_name, country_short, master=None):
        # init self
        super().__init__(master, bg=self.BACKGROUND_COLOUR)
        icon = tk.PhotoImage(file='img\icon.png')
        self.iconphoto(False, icon)
        self.minsize(505, 565)

        # values
        self.__weather_for_day = weather_for_day
        self.__temp_sign = temp_sign
        self.__wind_sign = wind_sign
        self.__city_name = city_name
        self.__country_short = country_short
        self.__temp_day = ""
        self.__temp_morn = ""
        self.__temp_eve = ""
        self.__temp_night = ""
        self.__temp_day_feels_like = ""
        self.__temp_morn_feels_like = ""
        self.__temp_eve_feels_like = ""
        self.__temp_night_feels_like = ""

        # main frames for components
        self.__frame = tk.Frame(self, bg=self.BACKGROUND_COLOUR)
        self.__frame.pack()

        # frame for city name
        self.__city_frame = tk.Frame(self.__frame, bg=self.BACKGROUND_COLOUR)
        self.__city_frame.grid(row=0, column=0, columnspan=2, pady=(10, 4))
        # frame for date and day
        self.__date_frame = tk.Frame(self.__frame, bg=self.BACKGROUND_COLOUR)
        self.__date_frame.grid(row=1, column=0, columnspan=2, pady=(0, 4))
        # frame for icon
        self.__icon_frame = tk.Frame(self.__frame, bg=self.BACKGROUND_COLOUR)
        self.__icon_frame.grid(row=2, column=0, columnspan=2, pady=(0, 4))
        # frame for description
        self.__description_frame = tk.Frame(self.__frame, bg=self.BACKGROUND_COLOUR)
        self.__description_frame.grid(row=3, column=0, columnspan=2, pady=(0, 4))
        # frame for temperature
        self.__temperature_frame = tk.Frame(self.__frame, bg=self.BACKGROUND_COLOUR)
        self.__temperature_frame.grid(row=4, column=0, pady=(0, 4), padx=(10, 0), sticky='w')
        # frame for temperature - feels like
        self.__temperature_feels_like_frame = tk.Frame(self.__frame, bg=self.BACKGROUND_COLOUR)
        self.__temperature_feels_like_frame.grid(row=4, column=1, pady=(0, 4), padx=(20, 10), sticky='w')
        # frame for sunrise and sunset
        self.__sunrise_sunset_frame = tk.Frame(self.__frame, bg=self.BACKGROUND_COLOUR)
        self.__sunrise_sunset_frame.grid(row=5, column=0, columnspan=2, pady=(0, 4), padx=(10, 0), sticky='w')
        # frame for pressure
        self.__pressure_frame = tk.Frame(self.__frame, bg=self.BACKGROUND_COLOUR)
        self.__pressure_frame.grid(row=6, column=0, columnspan=2, pady=(0, 4), padx=(10, 0), sticky='w')
        # frame for humidity
        self.__humidity_frame = tk.Frame(self.__frame, bg=self.BACKGROUND_COLOUR)
        self.__humidity_frame.grid(row=7, column=0, columnspan=2, pady=(0, 4), padx=(10, 0), sticky='w')
        # frame for wind speed
        self.__wind_speed_frame = tk.Frame(self.__frame, bg=self.BACKGROUND_COLOUR)
        self.__wind_speed_frame.grid(row=8, column=0, columnspan=2, pady=(0, 4), padx=(10, 0), sticky='w')
        # frame for cloudiness
        self.__cloudiness_frame = tk.Frame(self.__frame, bg=self.BACKGROUND_COLOUR)
        self.__cloudiness_frame.grid(row=9, column=0, columnspan=2, pady=(0, 5), padx=(10, 0), sticky='w')

        # init components in their frames
        self.__init_city()
        self.__init_icon()
        self.__init_description()
        self.__init_date_and_day_name()
        self.__init_sunrise_sunset()
        self.__init_temperature()
        self.__init_humidity()
        self.__init_pressure()
        self.__init_wind_speed()
        self.__init_cloudiness()

    def __init_city(self):
        self.__city_label = tk.Label(self.__city_frame, bg=self.BACKGROUND_COLOUR, fg=self.TEXT_COLOUR,
                                     font=(self.FONT, 14), text=f'{self.__city_name}, {self.__country_short}')
        self.__city_label.pack()

    def __init_icon(self):
        self.__render = ImageTk.PhotoImage(Image.open(f'img\{self.__weather_for_day.icon_code}.png'))
        self.__img = tk.Label(self.__icon_frame, image=self.__render, bg='white')
        self.__img.image = self.__render
        self.__img.pack()

    def __init_description(self):
        self.__weather_description_label = tk.Label(self.__description_frame, bg=self.BACKGROUND_COLOUR,
                                                    fg=self.TEXT_COLOUR, font=(self.FONT, 14),
                                                    text=self.__weather_for_day.weather_description)
        self.__weather_description_label.pack()

    def __init_date_and_day_name(self):
        self.__date_and_day_label = tk.Label(self.__date_frame, text=f'{self.__weather_for_day.day_name}, '
                                                                     f'{self.__weather_for_day.date}',
                                             bg=self.BACKGROUND_COLOUR, fg=self.TEXT_COLOUR, font=(self.FONT, 14))
        self.__date_and_day_label.pack()

    def __init_sunrise_sunset(self):
        self.__sunrise_sunset_label = tk.Label(self.__sunrise_sunset_frame,
                                               text=f'Sunrise: {self.__weather_for_day.sunrise} \t Sunset: '
                                                    f'{self.__weather_for_day.sunset}',
                                               bg=self.BACKGROUND_COLOUR, fg=self.TEXT_COLOUR, font=(self.FONT, 14))
        self.__sunrise_sunset_label.pack()

    def __init_temperature(self):
        if self.__temp_sign == self.CELSIUS_SIGN:
            self.__temp_day = self.__weather_for_day.temperature_for_day_in_celsius
            self.__temp_morn = self.__weather_for_day.temperature_for_morning_in_celsius
            self.__temp_eve = self.__weather_for_day.temperature_for_evening_in_celsius
            self.__temp_night = self.__weather_for_day.temperature_for_night_in_celsius
            self.__temp_day_feels_like = self.__weather_for_day.temperature_feels_like_for_day_in_celsius
            self.__temp_morn_feels_like = self.__weather_for_day.temperature_feels_like_for_morning_in_celsius
            self.__temp_eve_feels_like = self.__weather_for_day.temperature_feels_like_for_evening_in_celsius
            self.__temp_night_feels_like = self.__weather_for_day.temperature_feels_like_for_night_in_celsius
        elif self.__temp_sign == self.FAHRENHEIT_SIGN:
            self.__temp_day = self.__weather_for_day.temperature_for_day_in_fahrenheit
            self.__temp_morn = self.__weather_for_day.temperature_for_morning_in_fahrenheit
            self.__temp_eve = self.__weather_for_day.temperature_for_evening_in_fahrenheit
            self.__temp_night = self.__weather_for_day.temperature_for_night_in_fahrenheit
            self.__temp_day_feels_like = self.__weather_for_day.temperature_feels_like_for_day_in_fahrenheit
            self.__temp_morn_feels_like = self.__weather_for_day.temperature_feels_like_for_morning_in_fahrenheit
            self.__temp_eve_feels_like = self.__weather_for_day.temperature_feels_like_for_evening_in_fahrenheit
            self.__temp_night_feels_like = self.__weather_for_day.temperature_feels_like_for_night_in_fahrenheit
        else:
            self.__temp_day = self.__weather_for_day.temperature_for_day_in_kelvins
            self.__temp_morn = self.__weather_for_day.temperature_for_morning_in_kelvins
            self.__temp_eve = self.__weather_for_day.temperature_for_evening_in_kelvins
            self.__temp_night = self.__weather_for_day.temperature_for_night_in_kelvins
            self.__temp_day_feels_like = self.__weather_for_day.temperature_feels_like_for_day_in_kelvins
            self.__temp_morn_feels_like = self.__weather_for_day.temperature_feels_like_for_morning_in_kelvins
            self.__temp_eve_feels_like = self.__weather_for_day.temperature_feels_like_for_evening_in_kelvins
            self.__temp_night_feels_like = self.__weather_for_day.temperature_feels_like_for_night_in_kelvins

        self.__temp_day_label = tk.Label(self.__temperature_frame, text=f'Temperature for day: {self.__temp_day}',
                                         bg=self.BACKGROUND_COLOUR, fg=self.TEXT_COLOUR, font=(self.FONT, 14), pady=2)
        self.__temp_morn_label = tk.Label(self.__temperature_frame, text=f'Temperature in the morning: '
                                                                         f'{self.__temp_morn}',
                                          bg=self.BACKGROUND_COLOUR, fg=self.TEXT_COLOUR, font=(self.FONT, 14), pady=2)
        self.__temp_eve_label = tk.Label(self.__temperature_frame, text=f'Temperature in the evening: '
                                                                        f'{self.__temp_eve}',
                                         bg=self.BACKGROUND_COLOUR, fg=self.TEXT_COLOUR, font=(self.FONT, 14), pady=2)
        self.__temp_night_label = tk.Label(self.__temperature_frame, text=f'Temperature in the night: '
                                                                          f'{self.__temp_night}',
                                           bg=self.BACKGROUND_COLOUR, fg=self.TEXT_COLOUR, font=(self.FONT, 14), pady=2)
        self.__temp_day_feels_like_label = tk.Label(self.__temperature_feels_like_frame,
                                                    text=f'feels like: {self.__temp_day_feels_like}',
                                                    bg=self.BACKGROUND_COLOUR, fg=self.TEXT_COLOUR,
                                                    font=(self.FONT, 14), pady=2)
        self.__temp_morn_feels_like_label = tk.Label(self.__temperature_feels_like_frame,
                                                     text=f'feels like: {self.__temp_morn_feels_like}',
                                                     bg=self.BACKGROUND_COLOUR, fg=self.TEXT_COLOUR,
                                                     font=(self.FONT, 14), pady=2)
        self.__temp_eve_feels_like_label = tk.Label(self.__temperature_feels_like_frame,
                                                    text=f'feels like: {self.__temp_eve_feels_like}',
                                                    bg=self.BACKGROUND_COLOUR, fg=self.TEXT_COLOUR,
                                                    font=(self.FONT, 14), pady=2)
        self.__temp_night_feels_like_label = tk.Label(self.__temperature_feels_like_frame,
                                                      text=f'feels like: {self.__temp_night_feels_like}',
                                                      bg=self.BACKGROUND_COLOUR, fg=self.TEXT_COLOUR,
                                                      font=(self.FONT, 14), pady=2)

        self.__temp_day_label.pack(anchor='w')
        self.__temp_morn_label.pack(anchor='w')
        self.__temp_eve_label.pack(anchor='w')
        self.__temp_night_label.pack(anchor='w')
        self.__temp_day_feels_like_label.pack(anchor='w')
        self.__temp_morn_feels_like_label.pack(anchor='w')
        self.__temp_eve_feels_like_label.pack(anchor='w')
        self.__temp_night_feels_like_label.pack(anchor='w')

    def __init_pressure(self):
        self.__pressure_label = tk.Label(self.__pressure_frame, text=f'Pressure: {self.__weather_for_day.pressure}',
                                         bg=self.BACKGROUND_COLOUR, fg=self.TEXT_COLOUR, font=(self.FONT, 14))
        self.__pressure_label.pack()

    def __init_humidity(self):
        self.__humidity_label = tk.Label(self.__humidity_frame, text=f'Humidity: {self.__weather_for_day.humidity}',
                                         bg=self.BACKGROUND_COLOUR, fg=self.TEXT_COLOUR, font=(self.FONT, 14))
        self.__humidity_label.pack()

    def __init_wind_speed(self):
        self.__wind_speed = ""
        if self.__wind_sign == self.METERS_PER_SECOND_SIGN:
            self.__wind_speed = self.__weather_for_day.wind_speed_in_ms
        elif self.__wind_sign == self.KILOMETERS_PER_HOUR_SIGN:
            self.__wind_speed = self.__weather_for_day.wind_speed_in_kmh
        elif self.__wind_sign == self.MILES_PER_HOUR_SIGN:
            self.__wind_speed = self.__weather_for_day.wind_speed_in_mph
        else:
            self.__wind_speed = self.__weather_for_day.wind_speed_in_knots

        self.__wind_speed_label = tk.Label(self.__wind_speed_frame,
                                           text=f'Wind speed: {self.__wind_speed} '
                                                f'{self.__weather_for_day.wind_direction}',
                                           bg=self.BACKGROUND_COLOUR, fg=self.TEXT_COLOUR, font=(self.FONT, 14))
        self.__wind_speed_label.pack()

    def __init_cloudiness(self):
        self.__cloudiness_label = tk.Label(self.__cloudiness_frame,
                                           text=f'Cloudiness: {self.__weather_for_day.cloudiness}',
                                           bg=self.BACKGROUND_COLOUR, fg=self.TEXT_COLOUR, font=(self.FONT, 14))
        self.__cloudiness_label.pack()
