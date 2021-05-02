# TODO - add docs
# TODO - fields values like in json, wanted format via properties (as strings)
# TODO - add utilities, converters
class WeatherForDay:

    def __init__(self, data_for_day, timezone_shift):
        self.__date = data_for_day["dt"]  # timestamp in UTC, type int
        self.__timezone = timezone_shift  # Shift in seconds from UTC, type int
        self.__sunrise = data_for_day["sunrise"]  # timestamp in UTC, type int
        self.__sunset = data_for_day["sunset"]  # timestamp in UTC, type int

        self.__temp_day = data_for_day["temp"]["day"]  # by default temp is in K, type real
        self.__temp_morn = data_for_day["temp"]["morn"]  # by default temp is in K, type real
        self.__temp_eve = data_for_day["temp"]["eve"]  # by default temp is in K, type real
        self.__temp_night = data_for_day["temp"]["night"]  # by default temp is in K, type real

        self.__temp_feels_like_day = data_for_day["feels_like"]["day"]  # by default temp is in K, type real
        self.__temp_feels_like_morn = data_for_day["feels_like"]["morn"]  # by default temp is in K, type real
        self.__temp_feels_like_eve = data_for_day["feels_like"]["eve"]  # by default temp is in K, type real
        self.__temp_feels_like_night = data_for_day["feels_like"]["eve"]  # by default temp is in K, type real

        self.__pressure = data_for_day["pressure"]  # by default in hPa, type int
        self.__humidity = data_for_day["humidity"]  # in %, type int
        self.__wind_speed = data_for_day["speed"]  # by default in m/s, type real
        self.__wind_direction = data_for_day["deg"]  # by default in degrees (meteorological), type int
        self.__cloudiness = data_for_day["clouds"]  # in % - cloudiness, type int

        self.__weather_description = data_for_day["weather"][0]["description"]  # weather description, type str
        self.__icon_code = data_for_day["weather"][0]["icon"]  # weather icon code, type str

    # TODO - delete - temp, for tests
    def __str__(self):
        return str(self.__date) + " " + str(self.__timezone) + " " + str(self.__sunrise) + " " + str(self.__sunset) + " " + \
               str(self.__temp_day) + " " + str(self.__temp_morn) + " " + str(self.__temp_eve) + " " + str(self.__temp_night) + " " + \
               str(self.__temp_feels_like_day) + " " + str(self.__temp_feels_like_morn) + " " + str(self.__temp_feels_like_eve) + \
               " " + str(self.__temp_feels_like_night) + " " + str(self.__pressure) + " " + str(self.__humidity) + " " + \
               str(self.__wind_speed) + " " + str(self.__wind_direction) + str(self.__cloudiness) + " " + self.__weather_description + \
               " " + self.__icon_code
