flight_params = {
    'apikey': 'API',
    'fly_from': 'LON',
    'date_from': 'tomorrow',
    'date_to': 'future_date',
    'nights_in_dst_from': 7,
    'nights_in_dst_to': 28,
    'flight_type': 'round',
    'one_for_city': 1,
    'adults': 1,
    'curr': 'GBP'
}
flight_params.update(fly_to='LAX', max_stopovers=0)
print(flight_params)
