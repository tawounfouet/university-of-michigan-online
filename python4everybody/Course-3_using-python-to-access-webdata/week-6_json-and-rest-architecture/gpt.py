import urllib.request, urllib.parse, urllib.error
import json

# Base URL for the provided API endpoint
serviceurl = "http://py4e-data.dr-chuck.net/geojson?"

while True:
    # Prompt user for the location
    address = input("Enter location: ")
    if len(address) < 1:
        break

    # Encode the parameters and construct the full URL
    url = serviceurl + urllib.parse.urlencode({"address": address})

    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("==== Failure To Retrieve ====")
        print(data)
        continue

    # Extract the place_id from the JSON response
    place_id = js["results"][0]["place_id"]
    print("Place ID:", place_id)
    
    # Extract the plus_code from the JSON response, if available
    plus_code = js["results"][0].get("plus_code", {}).get("global_code")
    if plus_code:
        print("Plus Code:", plus_code)
    else:
        print("Plus Code not found")

    break
