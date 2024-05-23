import urllib.request
import urllib.parse
import json
import ssl

# API endpoint
serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

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

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('==== Download error ===')
        #print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        #print(data)
        break

    # Extracting latitude and longitude
    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    print('lat', lat, 'lon', lon)

    # Extracting plus code
    plus_code = js['features'][0]['properties'].get('plus_code')
    if plus_code and isinstance(plus_code, str):  # Check if 'plus_code' exists and is a string
        print('Plus code:', plus_code)
    else:
        print('Plus code not found for this location.')
