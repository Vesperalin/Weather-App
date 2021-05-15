import tkinter as tk


class WeatherFrame(tk.Toplevel):
    def __init__(self, parent, city_name, temp_sign, wind_sign, weather_conditions):
        super().__init__(parent)
        self.__parent = parent
        self.__city_name = city_name
        self.__temp_sign = temp_sign
        self.__wind_sign = wind_sign
        self.__weather_conditions = weather_conditions

        # main frame of the window
        self.__frame = tk.Frame(self)
        self.__frame.pack()

        label = tk.Label(self.__frame, text=self.__city_name)
        label.pack()
