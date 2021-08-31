import requests


def retrieve_local_ip_address():
    '''Return IP address of the computer'''
    response = requests.get('https://api.ipify.org')

    return response.text


def get_geolocation(ip_address):
    '''Get geolocation of an ip address'''
    response = requests.get(f'https://ipinfo.io/{ip_address}')
    data = response.json()
    city, country = data['city'], data['country']
    coords = [float(coord) for coord in data['loc'].split(',')]

    return city, country, coords


def greet(ip_address):
    information = get_geolocation(ip_address)
    
    return f'Hello, you are presently in {information[0]},{information[1]} \
and your cordinates are latitude: {information[2][0]} and longitude: {information[2][1]}'

if __name__ == '__main__':
    ip_address = retrieve_local_ip_address()
    msg_str = greet(ip_address)
    print(msg_str)
    

