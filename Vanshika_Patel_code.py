import requests
import json #importing json and requests 
import csv

access_key="i2sHkY5FcQ3FWOLehZfnPpPMcuvA16wqRf7TbJl7UMy-LfOLf9TT8aC6ywha44YIUoPRr51aCHiQdW2iA0GwCRXgWlCJAEVsgl54pY4dOrTbZFRHN5JdzCtn5ieyYHYx" #including access key from yelp
endpoint="https://api.yelp.com/v3/businesses/search"
headers={'Authorization': 'Bearer i2sHkY5FcQ3FWOLehZfnPpPMcuvA16wqRf7TbJl7UMy-LfOLf9TT8aC6ywha44YIUoPRr51aCHiQdW2iA0GwCRXgWlCJAEVsgl54pY4dOrTbZFRHN5JdzCtn5ieyYHYx'}
params={'latitude':'-36.872', 'longitude':'174.74', 'limit':'50', 'radius':'500'}

payload=requests.get(endpoint,params=params,headers=headers).json() #creating variable payload

print(payload) #printing pay load to yelp 

with open('yelp.json','w') as f:
    json.dump(payload,f) #using dump payload for json 
   
payload_good=[['name','rating','url','price','lat','long','category']] #New array for holding data in data file
for business in payload['businesses']: #creating for loop to iterate business in JSON data 
    lat=str(business['coordinates']['latitude']) #Capturing each data items into new variable 
    lon=str(business['coordinates']['longitude'])
    name=str(business['name'])
    url=str(business['url'])
    price=str(business['price']) if 'price' in business else 'null'
    rating=str(business['rating'])
    category=str(business['categories'][0]['title'])
    l=[name,rating,url,price,lat,lon,category]
    payload_good.append(l)
   
with open('yelp.csv','w') as csv_file: #opening csv file , addind write path.
    writer=csv.writer(csv_file)
    writer.writerows(payload_good) #writing payload_good to csv file
csv_file.close()
