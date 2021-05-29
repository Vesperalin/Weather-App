import app.utils.weather_api_utility as weather_utility
import app.utils.api_error as api_error
import app.utils.weather_for_day as weather_for_day


class ForecastForDays:

    """
        Class used to get and store information about weather for days

        Attributes:
            __api_utility -- reference to WeatherApiUtility instance
            __weather_forecasts_for_days -- list of WeatherForDay instances
            __city_name -- name of the city for which is the forecast, type str
            __country_short -- short name of country where the city is, type str
            __amount_of_days -- amount of days, for which forecast is wanted, type int
        Properties:
            weather_forecasts_for_days -- returns reference to WeatherApiUtility instance
            city_name -- returns name of the city for which is the forecast, type str
            country_short -- returns short name of country where the city is, type str
            amount_of_days -- returns amount of days, for which forecast is wanted, type int
        Methods:
            get_data_for_city(self, city_name) -- parameter is a city name for which is the forecast, returns None
                Method gets and processes information about weather from api to fill __weather_forecasts_for_days
    """

    def __init__(self, amount_of_days):
        self.__api_utility = weather_utility.WeatherApiUtility(amount_of_days)
        self.__weather_forecasts_for_days = []
        self.__city_name = ""
        self.__country_short = ""
        self.__amount_of_days = amount_of_days

    def get_data_for_city(self, city_name):
        data = self.__api_utility.get_data_for_days(city_name)

        if isinstance(data, int):  # if error occurred
            raise api_error.ApiError(data)
        else:
            self.__city_name = data["city"]["name"]
            self.__country_short = data["city"]["country"]

            for i in range(0, self.__amount_of_days):
                self.__weather_forecasts_for_days.append(weather_for_day.WeatherForDay(data["list"][i],
                                                                                       data["city"]["timezone"]))

        return None

    @property
    def weather_forecasts_for_days(self):
        return self.__weather_forecasts_for_days

    @property
    def city_name(self):
        return self.__city_name

    @property
    def country_short(self):
        return self.__country_short

    @property
    def amount_of_days(self):
        return self.__amount_of_days
