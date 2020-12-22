import json
import os
import requests

SHEET = 'price'
ENDPOINT = 'https://api.sheety.co/0599c004d034001f75a8249650a83978/flightDeals'
TOKEN = os.environ['SHEETY_TOKEN']
USERS_SHEET = 'user'


class DataManager:
    def __init__(self, endpoint, sheet, token):
        self.sheet = sheet
        self.endpoint = f'{endpoint}/{sheet}s'
        self.headers = {"Authorization": f'Bearer {token}'}
        self.data = self._get_data()

    def _get_data(self):
        response = requests.get(self.endpoint, headers=self.headers)
        return response.json()

    def put_data(self, data):
        row = data.pop('id')
        requests.put(f'{self.endpoint}/{row}',
                     json=self._gen_data(**data),
                     headers=self.headers)
        self.data = self._get_data()

    def _gen_data(self, **kwargs):
        return {
            self.sheet: kwargs
        }

    def get_iata_codes(self):
        return [row['iataCode'] for row in self.data]

    def get_lowest_prices(self):
        return [row['lowestPrice'] for row in self.data]
