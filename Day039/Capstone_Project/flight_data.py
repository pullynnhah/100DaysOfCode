class FlightData:
    def __init__(self, data):
        self.data = data
        self.formatted_data = self._format_data()

    def _format_data(self):
        flight_data = []
        for flight in self.data["data"]:

            new_data = {
                'destiny': flight['cityTo'],
                'from': f'{flight["cityFrom"]}-{flight["flyFrom"]}',
                'to': f'{flight["cityTo"]}-{flight["flyTo"]}',
                'price': flight['price'],
                'link': flight['deep_link'],
                'departure_date': flight['route'][0]["local_departure"].split('T')[0],
                'arrival_date': flight['route'][1]["local_departure"].split('T')[0]
            }
            flight_data.append(new_data)
        return flight_data
