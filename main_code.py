import pandas as pd
import requests

df1=pd.read_csv("bseall.csv")
df1=df1.drop(["Security Code","Status","Security Name","Group","Face Value","ISIN No","Industry","Instrument","Sector Name","Industry New Name","Igroup Name","ISubgroup Name"], axis='columns')
sym=df1['Security Id'].head(10).to_list()


dat=[]
for i in sym:
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={i}.bse&outputsize=full&apikey=4XD1D0HZAK8VPI57'
    r = requests.get(url)
    data = r.json()
    print(data)
    time_series = data['Time Series (Daily)']
    
    # Extract and format the data
    for date, daily_data in time_series.items():
        if date.split("-")[0]<2022:
            break
        dat.append({
            "company": i,
            'Date': date,
            'Open': daily_data['1. open'],
            'High': daily_data['2. high'],
            'Low': daily_data['3. low'],
            'Close': daily_data['4. close'],
            'No. of Shares': daily_data['5. volume'],
        })

print(dat)
bse_data=pd.DataFrame(dat)
bse_data.to_csv("2022_onwards.csv")