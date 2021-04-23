import requests
import json


import api_key


class ApiSevenDaysUtility:
    """
        class used to connect and get data in json format from weather API
        uses my private api key, which is saved in api_key file
    """
    API_CALL = 'http://api.openweathermap.org/data/2.5/forecast/daily?'
    DAYS_AMOUNT = '&cnt=5'
    API_KEY = '&appid=' + api_key.PRIVATE_API_KEY

    def __init__(self):
        pass

    def get_data(self, city):
        response = requests.get(f'{self.API_CALL}q={city}{self.DAYS_AMOUNT}{self.API_KEY}')
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code


if __name__ == '__main__':
    # TODO - delete
    n = ApiSevenDaysUtility()
    # d = n.get_data('Leszno')
    # print(json.dumps(d, indent=4))
    if n.get_data('Leszno') == 400:
        print(400)
    else:
        print(json.dumps(n.get_data('Leszno'), indent=4))
