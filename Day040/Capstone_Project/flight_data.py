class FlightData:
    def __init__(self, flight):
        self.data = flight[0]
        self.formatted_data = self._format_data()

    def _format_data(self):
        try:
            return_date = self.data['route'][2]["local_departure"].split('T')[0]
        except IndexError:
            return_date = self.data['route'][1]["local_departure"].split('T')[0]
        return {
            'destiny': self.data['cityTo'],
            'from': f'{self.data["cityFrom"]}-{self.data["flyFrom"]}',
            'to': f'{self.data["cityTo"]}-{self.data["flyTo"]}',
            'price': self.data['price'],
            'departure_date': self.data['route'][0]["local_departure"].split('T')[0],
            'arrival_date': return_date,
            'via_city': self.data['route'][0]['cityTo']
        }
