import requests
import json


import app.utils.api_key as api_key


class WeatherApiUtility:
    """
        Class used to connect and get data in json format from weather API.
        Uses my private api key, which is saved in api_key file (ignored in .gitignore)
        Attributes:
            __days_amount -- infix for api call, amount of days of forecast, type str
        Methods:
            get_data(self, city_name) -- parameter is a city name of string type, returns json with information
                about weather or code of error if getting data from api didn't succeed

        Info: Made it as a class, not separate methods, because it may help with developing app- in the future
    """

    __API_CALL = 'http://api.openweathermap.org/data/2.5/forecast/daily?q='
    __DAYS_AMOUNT_INFIX = '&cnt='
    __API_KEY = '&appid=' + api_key.PRIVATE_API_KEY

    def __init__(self, amount_of_days):
        self.__days_amount = self.__DAYS_AMOUNT_INFIX + str(amount_of_days)

    def get_data_for_days(self, city_name):
        response = requests.get(f'{self.__API_CALL}{city_name}{self.__days_amount}{self.__API_KEY}')
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code  # value is a type of int


if __name__ == '__main__':
    # TODO - delete
    n = WeatherApiUtility(7)
    d = n.get_data_for_days('Leszno')
    # print(json.dumps(d, indent=4))
    if d == 400:
        print(400)
    else:
        print(json.dumps(d, indent=4))
