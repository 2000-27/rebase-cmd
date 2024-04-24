                                              
import smartystreets_python_sdk as smarty                                                                                                   
                                                                                                    
def run():                                                                                          
    # This keypair will have been deleted by the time you are watching this video...                
    auth_id = "206be8b2-fa32-9164-6fcd-849d55181e86"
    auth_token = "F3ZIE2zvp9OgrxmkYl6t"                                                            
    credentials = smarty.StaticCredentials(auth_id, auth_token)                                            
                                                                                                    
                                           
    client = smarty.ClientBuilder(credentials).build_us_street_api_client()                                
                                                                                                    
    lookup = smarty.us_street.Lookup('1428 Post Aly Seattle, WA 98101')                                                                                                                                                    
    client.send_lookup(lookup)                                                                      
                                                                                      
    # print("Step 3. Show the resulting candidate addresses:")                                        
    for c, candidate in enumerate(lookup.result):                                                   
        print("- {}: {}, {}".format(c, candidate.delivery_line_1, candidate.last_line))             
                                                                                                    
                                                                                                    
if __name__ == "__main__":                                                                          
    run()                                                                                           
