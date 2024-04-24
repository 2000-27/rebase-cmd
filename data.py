import os

from smartystreets_python_sdk import SharedCredentials, StaticCredentials, ClientBuilder, exceptions
from smartystreets_python_sdk.us_autocomplete_pro import Lookup as AutocompleteProLookup, geolocation_type
from smartystreets_python_sdk.us_street import Lookup as StreetLookup
from smartystreets_python_sdk.us_street.match_type import MatchType



key = "196981591642918640"
hostname = "localhost"
credentials = SharedCredentials(key, hostname)



def street_data(data):
    print("VVVVVVVVVVVVVVVVV")
    client = ClientBuilder(credentials).build_us_street_api_client()
    lookup = StreetLookup()
    # lookup.addressee = "John Doe"
    lookup.street = data["street_line"]
    # lookup.street2 = "closet under the stairs"
    lookup.secondary = data["secondary"]
    # lookup.agent= smarty (website:demo/single-address@latest)
    # lookup.urbanization = ""  # Only applies to Puerto Rico addresses
    lookup.city = data["city"]
    lookup.state = data["state"]
    lookup.zipcode = data["zipcode"]
    lookup.candidates = 5
    lookup.match = "enhanced" 
    try:
        client.send_lookup(lookup)
    except exceptions.SmartyException as err:
        print(err)
        return

    result = lookup.result

    if not result:
        print("No candidates. This means the address is not valid.")
        return

    # print(result, "xckhdkjv")

    first_candidate = result[0]
    print(first_candidate.__dict__)
    print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
    print(first_candidate.components.__dict__)

    print("ZIP Code: " + first_candidate.components.zipcode)
    print("County: " + first_candidate.metadata.county_name)
    print("Latitude: {}".format(first_candidate.metadata.latitude))
    print("Longitude: {}".format(first_candidate.metadata.longitude))
   
  


  
def suggestion_method():
    client = ClientBuilder(credentials).build_us_autocomplete_pro_api_client()
    lookup = AutocompleteProLookup('1234 1 Dirt Rd')

    client.send(lookup)
    lookup.max_results = 10
    lookup.prefer_geo = geolocation_type.NONE
    lookup.prefer_ratio = 33
    lookup.source = 'all'

    suggestions = client.send(lookup)

    a = suggestions[0]
    
    for suggestion in suggestions:
        data = suggestion.__dict__
    print(data)
    street_data(data)
    return data




if __name__ == "__main__":
    suggestion_method()