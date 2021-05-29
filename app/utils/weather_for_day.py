import datetime


class WeatherForDay:

    """
        Class stores, converts and represents weather conditions for a specific day

        Static variables:
            CELSIUS_SIGN -- sign for temperature in celsiuses, type str
            KELVIN_SIGN -- sign for temperature in kelvins, type str
            FAHRENHEIT_SIGN -- sign for temperature in fahrenheits, type str
            PRESSURE_SIGN -- sign for pressure, type str
            PERCENTAGE_SIGN -- %, type str
            METERS_PER_SECOND_SIGN -- sign for wind speed in meters per second, type str
            MILES_PER_HOUR_SIGN -- sign for wind speed in miles per hour, type str
            KILOMETERS_PER_HOUR_SIGN -- sign for wind speed in kilometers per hour, type str
            KNOTS_SIGN -- sign for wind speed in knots, type str
            CARDINAL_DIRECTION -- signs for wind direction, type str
        Attributes:
             __date -- timestamp in UTC, type int
            __timezone_shift -- shift in seconds from UTC, type int
            __sunrise -- sunrise time, timestamp in UTC, type int
            __sunset -- sunset time, timestamp in UTC, type int
            __temp_day -- temperature during the day, by default temp is in Kelvins, type real
                (same for: __temp_morn, __temp_eve, __temp_night)
            __temp_feels_like_day -- temperature during the day, feels like, by default temp is in Kelvins, type real
                (same for: __temp_feels_like_morn, __temp_feels_like_eve, __temp_feels_like_night)
             __pressure -- pressure, by default in hPa, type int
             __humidity -- humidity in %, type int
            __cloudiness -- cloudiness in %, type int
            __wind_speed -- wind speed, by default in m/s, type real
             __wind_direction -- by default in degrees (meteorological), type int
            __weather_description -- short (1/3 words) description of the weather, type str
            __icon_code -- code of the weather icon, type str
        Properties:
            date -- returns date in format DD.MM.YYYY, type str
            day_name -- returns day name, type str
            sunrise -- returns time of sunrise in format HH:MM, type str
            sunset -- returns time of sunset in format HH:MM, type str
            temperature_for_day_in_kelvins -- returns temperature for the day in Kelvins, type str, with Kelvin sign
            temperature_for_day_in_celsius -- returns temperature for the day in Celsius, type str, with Celsius sign
            temperature_for_day_in_fahrenheit -- returns temperature for the day in Fahrenheit, type str,
                                                                                                    with fahrenheit sign
            (same for: __temp_morn, __temp_eve, __temp_night)
            temperature_feels_like_for_day_in_kelvins -- returns temperature for the day, feels like,
                                                                                in Kelvins, type str, with Kelvin sign
            temperature_feels_like_for_day_in_celsius -- returns temperature for the day, feels like,
                                                                                in Celsius, type str, with Celsius sign
            temperature_feels_like_for_day_in_fahrenheit -- returns temperature for the day, feels like,
                                                                        in Fahrenheit, type str, with fahrenheit sign
            (same for: __temp_feels_like_morn, __temp_feels_like_eve, __temp_feels_like_night)
            pressure -- returns pressure in hPa, type str, with pressure sign
            humidity -- returns humidity, in %, type str, with percentage sign
            cloudiness -- returns cloudiness in %, type str, with percentage sign
            wind_speed_in_ms -- returns wind speed in m/s (meters per second), with m/s sign
            wind_speed_in_mph -- returns wind speed in mph (miles per hour), with mph sign
            wind_speed_in_kmh -- returns wind speed in km/h (kilometers per hour), with km/h sign
            wind_speed_in_knots -- returns wind speed in kn (knots), with kn sign
            wind_direction -- converts meteorological degrees to cardinal directions (of wind), type str
            weather_description -- short (1/3 words) description of the weather, type str
            icon_code -- code of the weather icon, type str
        Methods:
            __convert_to_celsius -- converts Kelvins to Celsius, type int
            __convert_to_fahrenheit -- converts Kelvins to Fahrenheit, type int
    """

    CELSIUS_SIGN = u'\u2103'
    KELVIN_SIGN = 'K'
    FAHRENHEIT_SIGN = u'\u2109'
    PRESSURE_SIGN = 'hPa'
    PERCENTAGE_SIGN = '%'
    METERS_PER_SECOND_SIGN = 'm/s'
    MILES_PER_HOUR_SIGN = 'mph'
    KILOMETERS_PER_HOUR_SIGN = 'km/h'
    KNOTS_SIGN = 'kn'
    CARDINAL_DIRECTIONS = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW",
                           "NNW"]

    def __init__(self, data_for_day, timezone_shift):
        self.__date = data_for_day["dt"]
        self.__timezone_shift = timezone_shift
        self.__sunrise = data_for_day["sunrise"]
        self.__sunset = data_for_day["sunset"]

        self.__temp_day = data_for_day["temp"]["day"]
        self.__temp_morn = data_for_day["temp"]["morn"]
        self.__temp_eve = data_for_day["temp"]["eve"]
        self.__temp_night = data_for_day["temp"]["night"]

        self.__temp_feels_like_day = data_for_day["feels_like"]["day"]
        self.__temp_feels_like_morn = data_for_day["feels_like"]["morn"]
        self.__temp_feels_like_eve = data_for_day["feels_like"]["eve"]
        self.__temp_feels_like_night = data_for_day["feels_like"]["night"]

        self.__pressure = data_for_day["pressure"]
        self.__humidity = data_for_day["humidity"]
        self.__wind_speed = data_for_day["speed"]
        self.__wind_direction = data_for_day["deg"]
        self.__cloudiness = data_for_day["clouds"]

        self.__weather_description = data_for_day["weather"][0]["description"]
        self.__icon_code = data_for_day["weather"][0]["icon"]

    @property
    def date(self):
        date = datetime.datetime.utcfromtimestamp(self.__date + self.__timezone_shift).__str__()
        date = date.split(" ")[0].split("-")
        date = f'{date[2]}.{date[1]}.{date[0]}'
        return date

    @property
    def day_name(self):
        date = datetime.datetime.utcfromtimestamp(self.__date + self.__timezone_shift)
        day = date.strftime("%A")
        return day

    @property
    def sunrise(self):
        date = datetime.datetime.utcfromtimestamp(self.__sunrise + self.__timezone_shift).__str__()
        time = date.split(" ")[1]
        time = time[:len(time) - 3]
        return time

    @property
    def sunset(self):
        date = datetime.datetime.utcfromtimestamp(self.__sunset + self.__timezone_shift).__str__()
        time = date.split(" ")[1]
        time = time[:len(time) - 3]
        return time

    @property
    def temperature_for_day_in_kelvins(self):
        return f'{round(self.__temp_day)} {self.KELVIN_SIGN}'

    @property
    def temperature_for_day_in_celsius(self):
        return f'{self.__convert_to_celsius(self.__temp_day)} {self.CELSIUS_SIGN}'

    @property
    def temperature_for_day_in_fahrenheit(self):
        return f'{self.__convert_to_fahrenheit(self.__temp_day)} {self.FAHRENHEIT_SIGN}'

    @property
    def temperature_for_morning_in_kelvins(self):
        return f'{round(self.__temp_morn)} {self.KELVIN_SIGN}'

    @property
    def temperature_for_morning_in_celsius(self):
        return f'{self.__convert_to_celsius(self.__temp_morn)} {self.CELSIUS_SIGN}'

    @property
    def temperature_for_morning_in_fahrenheit(self):
        return f'{self.__convert_to_fahrenheit(self.__temp_morn)} {self.FAHRENHEIT_SIGN}'

    @property
    def temperature_for_evening_in_kelvins(self):
        return f'{round(self.__temp_eve)} {self.KELVIN_SIGN}'

    @property
    def temperature_for_evening_in_celsius(self):
        return f'{self.__convert_to_celsius(self.__temp_eve)} {self.CELSIUS_SIGN}'

    @property
    def temperature_for_evening_in_fahrenheit(self):
        return f'{self.__convert_to_fahrenheit(self.__temp_eve)} {self.FAHRENHEIT_SIGN}'

    @property
    def temperature_for_night_in_kelvins(self):
        return f'{round(self.__temp_night)} {self.KELVIN_SIGN}'

    @property
    def temperature_for_night_in_celsius(self):
        return f'{self.__convert_to_celsius(self.__temp_night)} {self.CELSIUS_SIGN}'

    @property
    def temperature_for_night_in_fahrenheit(self):
        return f'{self.__convert_to_fahrenheit(self.__temp_night)} {self.FAHRENHEIT_SIGN}'

    @property
    def temperature_feels_like_for_day_in_kelvins(self):
        return f'{round(self.__temp_feels_like_day)} {self.KELVIN_SIGN}'

    @property
    def temperature_feels_like_for_day_in_celsius(self):
        return f'{self.__convert_to_celsius(self.__temp_feels_like_day)} {self.CELSIUS_SIGN}'

    @property
    def temperature_feels_like_for_day_in_fahrenheit(self):
        return f'{self.__convert_to_fahrenheit(self.__temp_feels_like_day)} {self.FAHRENHEIT_SIGN}'

    @property
    def temperature_feels_like_for_morning_in_kelvins(self):
        return f'{round(self.__temp_feels_like_morn)} {self.KELVIN_SIGN}'

    @property
    def temperature_feels_like_for_morning_in_celsius(self):
        return f'{self.__convert_to_celsius(self.__temp_feels_like_morn)} {self.CELSIUS_SIGN}'

    @property
    def temperature_feels_like_for_morning_in_fahrenheit(self):
        return f'{self.__convert_to_fahrenheit(self.__temp_feels_like_morn)} {self.FAHRENHEIT_SIGN}'

    @property
    def temperature_feels_like_for_evening_in_kelvins(self):
        return f'{round(self.__temp_feels_like_eve)} {self.KELVIN_SIGN}'

    @property
    def temperature_feels_like_for_evening_in_celsius(self):
        return f'{self.__convert_to_celsius(self.__temp_feels_like_eve)} {self.CELSIUS_SIGN}'

    @property
    def temperature_feels_like_for_evening_in_fahrenheit(self):
        return f'{self.__convert_to_fahrenheit(self.__temp_feels_like_eve)} {self.FAHRENHEIT_SIGN}'

    @property
    def temperature_feels_like_for_night_in_kelvins(self):
        return f'{round(self.__temp_feels_like_night)} {self.KELVIN_SIGN}'

    @property
    def temperature_feels_like_for_night_in_celsius(self):
        return f'{self.__convert_to_celsius(self.__temp_feels_like_night)} {self.CELSIUS_SIGN}'

    @property
    def temperature_feels_like_for_night_in_fahrenheit(self):
        return f'{self.__convert_to_fahrenheit(self.__temp_feels_like_night)} {self.FAHRENHEIT_SIGN}'

    @property
    def pressure(self):
        return f'{self.__pressure} {self.PRESSURE_SIGN}'

    @property
    def humidity(self):
        return f'{self.__humidity} {self.PERCENTAGE_SIGN}'

    @property
    def wind_speed_in_ms(self):
        return f'{round(self.__wind_speed, 2)} {self.METERS_PER_SECOND_SIGN}'

    @property
    def wind_speed_in_mph(self):
        return f'{round(self.__wind_speed * 2.23694, 2)} {self.MILES_PER_HOUR_SIGN}'

    @property
    def wind_speed_in_kmh(self):
        return f'{round(self.__wind_speed * 3.6, 2)} {self.KILOMETERS_PER_HOUR_SIGN}'

    @property
    def wind_speed_in_knots(self):
        return f'{round(self.__wind_speed * 1.943844, 2)} {self.KNOTS_SIGN}'

    @property
    def wind_direction(self):
        i = round(self.__wind_direction / (360. / len(self.CARDINAL_DIRECTIONS)))
        return self.CARDINAL_DIRECTIONS[i % len(self.CARDINAL_DIRECTIONS)]

    @property
    def cloudiness(self):
        return f'{self.__cloudiness} {self.PERCENTAGE_SIGN}'

    @property
    def description(self):
        return self.__weather_description

    @property
    def icon_code(self):
        return str(self.__icon_code)

    @property
    def weather_description(self):
        return self.__weather_description

    def __convert_to_celsius(self, temp):
        return round(temp - 273.15)

    def __convert_to_fahrenheit(self, temp):
        return round((1.8 * (temp - 273)) + 32)
