import pandas as pd
import requests

# insert url of API endpoint
url = "https://bdtdq9ln04.execute-api.eu-west-2.amazonaws.com/P/writeKinesis"

# read csv file to pandas DataFrame
data = pd.read_csv('data.csv', nrows = 10)

#print(data.head(5))

#export = data.iloc[2].to_json()
#response = requests.post(url, data=export)

#

for i in data.index:
# convert the row to json
     export = data.iloc[i].to_json()

     # send to API
     response = requests.post(url, data=export)

     # print the returned status
     print(response)

