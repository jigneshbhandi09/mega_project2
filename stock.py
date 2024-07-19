import requests
import pandas as pd
import time

def fetch_alpha_vantage_data(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=full&datatype=json"
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}")
        return None
    
    data = response.json()
    
    # Check if the response contains the expected data
    if 'Time Series (Daily)' not in data:
        print("Error: 'Time Series (Daily)' not found in response")
        print(data)
        return None
    
    time_series = data['Time Series (Daily)']
    
    # Extract and format the data
    formatted_data = []
    for date, daily_data in time_series.items():
        formatted_data.append({
            'Date': date,
            'Open': daily_data['1. open'],
            'High': daily_data['2. high'],
            'Low': daily_data['3. low'],
            'Close': daily_data['4. close'],
            'No. of Shares': daily_data['5. volume'],
        })
    
    # Convert to DataFrame
    df = pd.DataFrame(formatted_data)
    
    # Check if the DataFrame is not empty
    if df.empty:
        print("No data found for the specified date range")
        return None
    
    return df

# Example usage
api_key = "7C26R9XX1YML6JPH"
symbol = "RELIANCE.BSE"
start_date = "2019-01-01"
end_date = "2020-12-31"
df = fetch_alpha_vantage_data(symbol, api_key)

# Filter DataFrame for the specified date range
if df is not None:
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    df.to_csv(f"{symbol}_stock_data_2019_2020.csv", index=False)
    print(f"Data saved to {symbol}_stock_data_2019_2020.csv")
else:
    print("Failed to fetch or save data")

