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
import pandas as pd
DOGE=pandas.read_csv("DOGE-USD.csv")
print(DOGE.head())

#3. Check if there are any missing values
print(DOGE.isna().any())

#4. Replace missing values with Zero
DOGE = DOGE.fillna(0)

#5. Check if there are any missing values
print(DOGE.isna().any())

#6. Create a list of dictionaries based on DOGE_USD Data
DOGE_list = [
    {"Date": "2021-06-13", "Open": 0.312485, "Close": 0.324382},
    {"Date": "2021-06-14", "Open": 0.326464, "Close": 0.322889},]
print(DOGE_list)

#7. Create a dictionary of lists with DOGE data
DOGE_dict = {
  "Date": ["2021-06-13", "2021-06-14"],
  "Open": [0.312485, 0.326464],
  "Close": [0.324382, 0.322889]}

#8. Convert dictionary into DataFrame
DOGE = pd.DataFrame(DOGE_dict)
print(DOGE)

#9. Sort DOGE_USD Data
DOGE_USD = pd.read_csv("DOGE-USD.csv")
DOGE_USD_sorted = DOGE_USD.sort_values("Close", ascending=False)
print(DOGE_USD_sorted)

#10. Check if any columns contain missing values
print(DOGE_USD.isna().any())

#11. Replace rows with missing values with 0
DOGE_USD_sorted = DOGE_USD.fillna(0)
print(DOGE_USD_sorted.isna().any())

#12. Index Dogecoin by High
DOGE_USD_ind = DOGE_USD.set_index("High")
print(DOGE_USD_ind)

#13. Reset the index, keeping its contents
print(DOGE_USD_ind.reset_index())

#14. Group data by High greater than 0.0003
DOGE_High = DOGE_USD_ind.groupby("High").mean()
print(DOGE_High)

#15. Loop while through dataframe DOGE_USD
for row in DOGE_USD.head().iterrows():
    print(row)

#16. Merge Dataframes created above DOGE_USD and DOGE
df2 = pd.concat([DOGE_USD, DOGE], axis=1)
print(df2)

#17 Numpy example
import numpy as np
my_array=np.array([DOGE_USD])
print(my_array)

DOGE_transposed=np.transpose(my_array)
print(my_array)

#18 Two charts using Matplotlib
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

stock_data = pd.read_csv("DOGE-USD.csv")

DOGE_USD.describe().plot(kind = "area",fontsize =27, figsize = (20,8),table = True, colormap="rainbow")
plt.xlabel("Date")
plt.ylabel("Close")
plt.title("Closing price of Dogecoin")
plt.show()




X = np.linspace(0, 9)
Y = np.cos (X)
fig, ax = plt.subplots()
ax.plot(X,Y,color="C1")
plt.xlabel ("Day")
plt.ylabel ("Price")
plt.title ("Stock Data")
plt.show()



