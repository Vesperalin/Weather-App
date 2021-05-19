import tkinter as tk


class SettingsInfoWindow(tk.Toplevel):

    """
        Class contains labels with information about default settings, default values
    """

    BACKGROUND_COLOUR = 'white'
    TEXT_COLOUR = 'black'
    FONT = "Microsoft YaHei"

    def __init__(self, default_values, master=None):
        # init self
        super().__init__(master, bg=self.BACKGROUND_COLOUR)
        self.minsize(280, 100)

        # main frames for components
        self.__frame = tk.Frame(self, bg=self.BACKGROUND_COLOUR)
        self.__frame.pack()

        # labels for values
        self.__city_name_label = tk.Label(self.__frame, text=f'Default city: {default_values[2]}',
                                          bg=self.BACKGROUND_COLOUR, fg=self.TEXT_COLOUR, font=(self.FONT, 12))
        self.__city_name_label.grid(row=0, column=0, sticky='w', pady=(10, 5))

        self.__temperature_label = tk.Label(self.__frame, text=f'Default temperature sign: {default_values[1]}',
                                            bg=self.BACKGROUND_COLOUR,  fg=self.TEXT_COLOUR, font=(self.FONT, 12))
        self.__temperature_label.grid(row=1, column=0, sticky='w', pady=(0, 5))

        self.__wind_label = tk.Label(self.__frame, text=f'Default wind sign: {default_values[0]}',
                                     bg=self.BACKGROUND_COLOUR, fg=self.TEXT_COLOUR, font=(self.FONT, 12))
        self.__wind_label.grid(row=2, column=0, sticky='w', pady=(0, 10))
