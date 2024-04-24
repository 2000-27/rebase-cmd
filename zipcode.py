import os

from smartystreets_python_sdk import SharedCredentials, StaticCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_zipcode import Lookup as ZIPCodeLookup


def run():
   

    key = "196981591642918640"
    hostname = "localhost"

    credentials = SharedCredentials(key, hostname)


    client = ClientBuilder(credentials).build_us_zipcode_api_client()

    lookup = ZIPCodeLookup()
  
    lookup.zipcode = "30350"
    lookup.country = "US"

    try:
        client.send_lookup(lookup)
    except exceptions.SmartyException as err:
        print(err)
        return

    result = lookup.result
    print(result.__dict__)
    zipcodes = result.zipcodes
    cities = result.cities

    for city in cities:
        print("\nCity: " + city.city)
        print("State: " + city.state)
        print("Mailable City: {}".format(city.mailable_city))

    for zipcode in zipcodes:
        print("\nZIP Code: " + zipcode.zipcode)
        print("Latitude: {}".format(zipcode.latitude))
        print("Longitude: {}".format(zipcode.longitude))


if __name__ == "__main__":
    run()