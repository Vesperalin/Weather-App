import tkinter as tk


import app.gui.weather_frame_for_day as weather_frame_for_day


class WeatherWindow(tk.Toplevel):

    """
            Class contains WeatherFrameForDay frames
            This is a first top level window
    """

    BACKGROUND_COLOUR = '#6BC0EE'

    def __init__(self, parent, temp_sign, wind_sign, weather_conditions):
        # init self
        super().__init__(parent, bg=self.BACKGROUND_COLOUR)
        icon = tk.PhotoImage(file='img\icon.png')
        self.iconphoto(False, icon)
        self.minsize(1230, 400)

        # values
        self.__weather_data_frames = []

        # main frame in the window
        self.__frame = tk.Frame(self, bg=self.BACKGROUND_COLOUR)
        self.__frame.pack()

        # frames for components
        self.__city_name_frame = tk.Frame(self.__frame, bg=self.BACKGROUND_COLOUR)
        self.__city_name_frame.grid(row=0, column=0, columnspan=weather_conditions.amount_of_days, sticky='w',
                                    pady=(10, 20), padx=(30, 0))

        # init city label in its frame
        self.__city_label = tk.Label(self.__city_name_frame, text=f'{weather_conditions.city_name}, '
                                                                  f'{weather_conditions.country_short}',
                                     bg=self.BACKGROUND_COLOUR, fg='white', font=("Microsoft YaHei", 38))
        self.__city_label.pack()

        # init WeatherFrameForDay instances
        for i in range(0, weather_conditions.amount_of_days):
            frame = weather_frame_for_day.WeatherFrameForDay(weather_conditions.weather_forecasts_for_days[i],
                                                             weather_conditions.city_name,
                                                             weather_conditions.country_short, temp_sign, wind_sign,
                                                             self.__frame)
            frame.grid(row=1, column=i, padx=9, pady=(0, 20))
            self.__weather_data_frames.append(frame)
