import bitly_api  
  
API_USER = "username" 
API_KEY = "API_Key"
bitly = bitly_api.Connection(API_USER, API_KEY)  
  
response = bitly.shorten('http://google.com/')  
  
# Now let us print the Bitly URL  
print(response) 