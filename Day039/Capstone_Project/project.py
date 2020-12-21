import datetime as dt
import data_manager as dm
import flight_search as fs
import flight_data as fd
import notification_manager as nm


DEPARTURE_IATA = 'LON'
SIX_MONTHS_IN_DAYS = 180


def get_date(date, **kwargs):
    new_date = date + dt.timedelta(**kwargs)
    return new_date.strftime('%d/%m/%Y')


today = dt.datetime.now()
tomorrow = get_date(today, days=1)
future_date = get_date(today, days=SIX_MONTHS_IN_DAYS)

flight_params = {
    'apikey': fs.API_KEY,
    'fly_from': DEPARTURE_IATA,
    'date_from': tomorrow,
    'date_to': future_date,
    'nights_in_dst_from': 7,
    'nights_in_dst_to': 28,
    'flight_type': 'round',
    'one_for_city': 1,
    'adults': 1,
    'curr': 'GBP',
    'max_stopovers': 0
}

data_manager = dm.DataManager(dm.ENDPOINT, dm.SHEET, dm.TOKEN)
print(data_manager.data)
for row in data_manager.data['prices']:
    city = row['city']
    params = {
        'apikey': fs.API_KEY,
        'location_types': 'city',
        'term': city
    }
    flight_search = fs.FlightSearch(fs.API_LOCATIONS, fs.ENDPOINT, params)
    row['iataCode'] = flight_search.search_locations('name', city, 'code')
    data_manager.put_data(row)

iata_codes = [row['iataCode'] for row in data_manager.data['prices']]

flight_params.update(fly_to=','.join(iata_codes))
print('')
flight_search = fs.FlightSearch(fs.API_SEARCH, fs.ENDPOINT, flight_params)
flight_data = fd.FlightData(flight_search.data)

notification_manager = nm.NotificationManager(nm.ACCOUNT_SID, nm.AUTH_TOKEN)
rows_already_notified = []

for data in flight_data.formatted_data:
    for row in data_manager.data['prices']:
        if row in rows_already_notified:
            continue
        if data['destiny'] == row['city']:
            rows_already_notified.append(row)
            if data['price'] <= row['lowestPrice']:
                message_part1 = '\n🚨Low price alert🚨'
                message_part2 = f'\nOnly £{data["price"]:.2f} to fly'
                message_part3 = f'\nfrom {data["from"]} to {data["to"]},'
                message_part4 = f'\nfrom {data["departure_date"]} to {data["arrival_date"]}.'
                message = message_part1 + message_part2 + message_part3 + message_part4
                notification_manager.send_message(nm.TWILIO_NUMBER, nm.MY_NUMBER, message)
