import json
import os
import requests

ENDPOINT = 'https://tequila-api.kiwi.com'
API_LOCATIONS = '/locations/query'
API_SEARCH = '/v2/search'
API_KEY = os.environ['TEQUILA_API_KEY']
AFFILL_ID = os.environ['TEQUILA_AFFILL_ID']


class FlightSearch:
    def __init__(self, api_call, endpoint, params):
        self.endpoint = f'{endpoint}{api_call}'
        self.params = params
        self.data = self._get_data()

    def _get_data(self):
        response = requests.get(self.endpoint, self.params)
        return response.json()

    def search_locations(self, key, value, city):
        for location in self.data['locations']:
            if location[key] == value:
                return location[city]
