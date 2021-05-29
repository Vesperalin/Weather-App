import app.utils.weather_api_utility as util
import app.utils.api_error as api_error


class DefaultSettingsManager:

    """
        Class used to get and set default settings in weather app: city name, temperature sign, wind sign

        Static variables:
            __FILE -- path to file, where default settings are stored, type str
            __api_util -- reference to WeatherApiUtility instance, used to check if city is correct
            TEMPERATURE_SYMBOLS -- temperature signs, type [str]
            WIND_SYMBOLS -- wind signs, type [str]
        Methods:
            read_from_default_settings(self) -- reads default values from file.
                    Returns list: [wind sign, temperature sign, city name]
                    If value  is not correct, the value will be None
            read_from_default_settings_without_city -- reads default values from file, without city.
                    Returns list: [wind sign, temperature sign]
                    If value  is not correct, the value will be None
            set_as_default(self, city_name, temperature, wind) -- writes new default values to file.
                    If city name is incorrect, throws ApiError exception and default values are not changed
    """

    __FILE = "utils/default_settings.txt"
    __api_util = util.WeatherApiUtility(1)  # to check if city is correct
    TEMPERATURE_SYMBOLS = [u'\u2103', 'K', u'\u2109']
    WIND_SYMBOLS = ['km/h', 'm/s', 'mph', 'kn']

    def __init__(self):
        pass

    def read_from_default_settings(self):
        file = open(self.__FILE, "r", encoding='UTF8')
        line_for_city_name = file.readline().rstrip('\n')
        line_for_temperature = file.readline().rstrip('\n')
        line_for_wind = file.readline().rstrip('\n')
        ret_values = [None, None, None]

        # check correctness of city name
        tmp = self.__api_util.get_data_for_days(line_for_city_name)
        if not isinstance(tmp, int):
            ret_values[2] = line_for_city_name

        # check correctness of temperature sign
        if line_for_temperature in self.TEMPERATURE_SYMBOLS:
            ret_values[1] = line_for_temperature

        # check correctness of wind sign
        if line_for_wind in self.WIND_SYMBOLS:
            ret_values[0] = line_for_wind

        file.close()
        return ret_values

    def read_from_default_settings_without_city(self):
        file = open(self.__FILE, "r", encoding='UTF8')
        line_for_city_name = file.readline().rstrip('\n')
        line_for_temperature = file.readline().rstrip('\n')
        line_for_wind = file.readline().rstrip('\n')
        ret_values = [None, None]

        # check correctness of temperature sign
        if line_for_temperature in self.TEMPERATURE_SYMBOLS:
            ret_values[1] = line_for_temperature

        # check correctness of wind sign
        if line_for_wind in self.WIND_SYMBOLS:
            ret_values[0] = line_for_wind

        file.close()
        return ret_values

    def set_as_default(self, city_name, temperature, wind):
        # check correctness of city name
        tmp = self.__api_util.get_data_for_days(city_name)
        if isinstance(tmp, int):
            raise api_error.ApiError(tmp)

        file = open(self.__FILE, "w", encoding='UTF8')
        file.write(f'{city_name}\n')
        file.write(f'{temperature}\n')
        file.write(f'{wind}')
        file.close()
