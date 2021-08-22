import csv
import json
import requests


class GeocodioGeocoder:
    GEOCODE_API_ENDPOINT = 'https://api.geocod.io/v1.4/geocode'
    GEOCODIO_API_KEY = ''

    def geocode(self, address: str):
        # construct url, example:
        # https://api.geocod.io/v1.4/geocode?street=1109+N+Highland+St&city=Arlington&state=VA&api_key=YOUR_API_KEY
        url = '{}?street={}'.format(self.GEOCODE_API_ENDPOINT, address).replace(' ', '+')
        # for field in ['city', 'state', 'postal_code']:
        #     if field in d and d[field]:
        #         url += '&{}={}'.format(field, d[field]).replace(' ', '+')
        url += '&api_key={}'.format(self.GEOCODIO_API_KEY)

        # get response
        result = json.loads(requests.get(url).text)
        if 'results' in result and len(result['results']) > 0:
            lat_lng = result['results'][0]['location']
            return '{},{}'.format(lat_lng['lng'], lat_lng['lat'])

        return None


gg = GeocodioGeocoder()
with open('./24hourfitnessclubs.csv') as csv_input, open('24hourfitnessclubs-geocoded.csv', 'w') as csv_output:
    club_reader = csv.reader(csv_input)
    club_writer = csv.writer(csv_output, lineterminator='\n')
    output_rows = []
    row = next(club_reader)
    row.append('Lat/Lng')
    output_rows.append(row)
    for row in club_reader:
        if row[2]:
            address = '{} {} {}'.format(row[0], row[1], row[2])
        else:
            address = '{} {}'.format(row[0], row[1])

        coords = gg.geocode(address)
        row.append(coords)
        output_rows.append(row)

    club_writer.writerows(output_rows)
