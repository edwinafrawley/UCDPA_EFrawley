#1. Importing Data-API Dogecoin

#Output is response 200 which confirms the API works
import pandas as pandas
import requests
data=requests.get("https://chain.so/api/v2/get_price/DOGE")
print(data)

#Output is text of API
import requests
data=requests.get("https://chain.so/api/v2/get_price/DOGE")
print(data.text)

#Output is type of data
import requests
data=requests.get("https://chain.so/api/v2/get_price/DOGE")
data2=data.text
print(type(data2))

#converts data to dictionary
import requests
data=requests.get("https://chain.so/api/v2/get_price/DOGE")
data2=data.json()
print(data2)

#print a key
import requests
data=requests.get("https://chain.so/api/v2/get_price/DOGE")
data2=data.json()
print(data2["data"])


#2. Import CSV File into a Pandas DataFrame

import data =pandas.read_csv(DOGE-USD.csv)
print(data)





