from sys import argv
from geopy.geocoders import Nominatim

def get_info(lat,lon):
    print(f"latitude: {lat}, longitude: {lon}")
    geolocator = Nominatim(user_agent="script_for_devops")
    location = geolocator.reverse(f"{lat}, {lon}")
    url=f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
    return {'location': f'{location}', 'Goggle Maps URL': url}

if __name__ == '__main__':
    try:
        script, lat, lon = argv
    except ValueError:
        inp = input('Введите latitude и longitude через пробел:\n')
        lat,lon = inp.split(' ')
    output = get_info(lat,lon)
    print(output)
