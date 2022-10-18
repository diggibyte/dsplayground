import requests
import pandas as pd
import json
from pandas import json_normalize

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"

querystring = {"symbol":"GOOG","region":"US"}
querystring_1 = {"symbol":"AAPL","region":"US"}
headers = {
	"X-RapidAPI-Key": "60c433a7d9msh44515c28059049ep13d629jsna9844baeaf58",
	"X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
response_1 = requests.request("GET", url, headers=headers, params=querystring_1)

data = response.text
data_1 = response_1.text
dit = json.loads(data)
df2 = json_normalize(dit['prices'])
print(df2)
dit_1 = json.loads(data_1)
df3 = json_normalize(dit_1['prices'])
print(df3)
print(df3.drop(columns=df3.columns, axis=1, inplace=True))
print(df3)