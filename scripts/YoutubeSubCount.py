import  urllib.request
import json
name = input('Enter user: ')
key = "AIzaSyCOXxH7PpXLeHK6WjkG6Hd3AdUr_meDrQg"
data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+name+"&key="+key).read()
subs = json.loads(data)
print(json.loads(data))
print(f'Subs {subs}')