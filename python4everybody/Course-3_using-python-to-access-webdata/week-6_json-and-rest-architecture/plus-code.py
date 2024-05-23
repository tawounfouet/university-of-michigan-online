import urllib.request
import urllib.parse
import json
import ssl

# Function to encode latitude and longitude into Open Location Code (OLC)
def encode_plus_code(latitude, longitude):
    code_digits = "23456789CFGHJMPQRVWX"
    code_length = 10
    precision_levels = [20, 1, 0.05, 0.0025, 0.000125]

    def encode_pair(value, max_value, length):
        value += max_value
        code = ''
        for _ in range(length):
            value *= 20
            digit = int(value)
            code += code_digits[digit]
            value -= digit
        return code

    code = ''
    for level in precision_levels:
        code += encode_pair(latitude, 90, int(round(code_length / 2)))
        code += encode_pair(longitude, 180, int(round(code_length / 2)))
        code_length -= 2
        latitude %= level
        longitude %= level

    code = code[:code_length] + '+' + code[code_length:]

    return code

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    address = address.strip()
    parms = {'q': address}

    url = f'https://py4e-data.dr-chuck.net/opengeo?{urllib.parse.urlencode(parms)}'
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        continue

    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    print('lat', lat, 'lon', lon)
    location = js['features'][0]['properties']['formatted']
    print('Location:', location)

    # Generate Plus Code
    plus_code = encode_plus_code(lat, lon)
    print('Plus Code:', plus_code)
