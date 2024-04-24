import os

from smartystreets_python_sdk import SharedCredentials, StaticCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_street import Lookup as StreetLookup
from smartystreets_python_sdk.us_street.match_type import MatchType


def run():
    # key = "Your SmartyStreets Key here"
    # hostname = "Your Hostname here"

    # We recommend storing your secret keys in environment variables instead---it's safer!
    # for client-side requests (browser/mobile), use this code:
    key = "196999214422605260"
    hostname = "localhost"

    credentials = SharedCredentials(key, hostname)


    # The appropriate license values to be used for your subscriptions
    # can be found on the Subscriptions page of the account dashboard.
    # https://www.smartystreets.com/docs/cloud/licensing
    client = ClientBuilder(credentials).build_us_street_api_client()
    # client = ClientBuilder(credentials).with_custom_header({'User-Agent': 'smartystreets (python@0.0.0)', 'Content-Type': 'application/json'}).build_us_street_api_client()
    # client = ClientBuilder(credentials).with_proxy('localhost:8080', 'user', 'password').build_us_street_api_client()
    # Uncomment the line above to try it with a proxy instead

    # Documentation for input fields can be found at:
    # https://smartystreets.com/docs/us-street-api#input-fields

    lookup = StreetLookup()
  
    # lookup.addressee = "John Doe"
    lookup.street = "D"
    # lookup.street2 = "closet under the stairs"
    # lookup.secondary = "APT 2"
    # lookup.agent= smarty (website:demo/single-address@latest)
    # lookup.urbanization = ""  # Only applies to Puerto Rico addresses
    # lookup.city = "Mountain View"
    # lookup.state = "CA"
    lookup.zipcode = "027"
    lookup.candidates = 5
    lookup.match ="enhanced"  # "invalid" is the most permissive match,
                                    #   this will always return at least one result even if the address is invalid.
                                    #   Refer to the documentation for additional Match Strategy options.

    try:
        client.send_lookup(lookup)
    except exceptions.SmartyException as err:
        print(err)
        return

    result = lookup.result
   

    if not result:
        print("No candidates. This means the address is not valid.")
        return

 

    first_candidate = result[0]
    print(first_candidate.__dict__,"MMMMMMMMMMMMMM")

    print("ZIP Code: " + first_candidate.components.zipcode)
    print("County: " + first_candidate.metadata.county_name)
    print("Latitude: {}".format(first_candidate.metadata.latitude))
    print("Longitude: {}".format(first_candidate.metadata.longitude))
   
  

if __name__ == "__main__":
    run()