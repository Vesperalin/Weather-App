import tkinter as tk


import app.gui.weather_frame_for_day as weather_frame_for_day


# TODO - add docs
class WeatherWindow(tk.Toplevel):
    def __init__(self, parent, temp_sign, wind_sign, weather_conditions):
        super().__init__(parent, bg='#6BC0EE')
        self.minsize(1230, 400)

        # values
        self.__parent = parent
        self.__temp_sign = temp_sign
        self.__wind_sign = wind_sign
        self.__weather_conditions = weather_conditions
        self.__weather_data_frames = []

        # frames for components
        self.__frame = tk.Frame(self, bg='#6BC0EE')
        self.__frame.pack()

        self.__city_name_frame = tk.Frame(self.__frame, bg='#6BC0EE')
        self.__city_name_frame.grid(row=0, column=0, columnspan=self.__weather_conditions.amount_of_days, sticky='w',
                                    pady=(10, 20), padx=(30, 0))

        # init city label in frame
        self.__city_label = tk.Label(self.__city_name_frame, text=f'{self.__weather_conditions.city_name}, '
                                                                  f'{self.__weather_conditions.country_short}',
                                     bg='#6BC0EE', fg='white', font=("Microsoft YaHei", 38))
        self.__city_label.pack()

        for i in range(0, self.__weather_conditions.amount_of_days):
            frame = weather_frame_for_day.WeatherFrameForDay(i, self.__weather_conditions.weather_forecasts_for_days[i],
                                                             self.__weather_conditions.city_name,
                                                             self.__weather_conditions.country_short, self.__temp_sign,
                                                             self.__wind_sign, self.__frame)
            self.__weather_data_frames.append(frame)

