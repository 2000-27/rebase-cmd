import os

from smartystreets_python_sdk import SharedCredentials, StaticCredentials, ClientBuilder
from smartystreets_python_sdk.us_autocomplete_pro import Lookup as AutocompleteProLookup, geolocation_type


def run():
  
    key = "196981591642918640"
    hostname = "localhost"
    
    credentials = SharedCredentials(key, hostname)

    client = ClientBuilder(credentials).build_us_autocomplete_pro_api_client()
    lookup = AutocompleteProLookup('1234 1 Dirt Rd')

    client.send(lookup)

    print('*** Result with no filter ***')
    print()
    for suggestion in lookup.result:
        print(suggestion.__dict__)
        # print(suggestion.street_line + " " + suggestion.city, suggestion.state, sep=", ")



    # lookup.add_city_filter('Denver,Aurora,CO')
    # lookup.add_city_filter('Orem,UT')
    # lookup.add_state_preference('CO')

    lookup.max_results = 10
    lookup.prefer_geo = geolocation_type.NONE
    lookup.prefer_ratio = 33
    lookup.source = 'all'

    suggestions = client.send(lookup)  # The client will also return the suggestions directly

    print()
    print('*** Result with some filters ***')
    for suggestion in suggestions:
        print(suggestion.__dict__)
        # print({"street_line":suggestion.street_line , "city " : suggestion.city , "state " : suggestion.state,"zipcode" :suggestion.zipcode})


if __name__ == "__main__":
    run()