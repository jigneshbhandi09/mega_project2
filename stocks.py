import yfinance as yf
import pandas as pd
import requests


def fetch_yahoo_finance_data(symbol, start_date, end_date):
    try:
        df = yf.download(symbol, start=start_date, end=end_date, interval='1d')
        if df.empty:
            print(f"No data found for {symbol}")
            return None
        df.reset_index(inplace=True)
        df.rename(columns={
            'Date': 'Date',
            'Open': 'Open',
            'High': 'High',
            'Low': 'Low',
            'Close': 'Close',
            'Volume': 'No. of Shares'
        }, inplace=True)
        df['Company'] = symbol
        return df[['Date', 'Company', 'Open', 'High', 'Low', 'Close', 'No. of Shares']]
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def save_combined_data_to_csv(dataframes, filename):
    try:
        combined_df = pd.concat(dataframes, ignore_index=True)
        combined_df.sort_values(by='Date', ascending=True, inplace=True)
        combined_df.to_csv(filename, index=False, columns=['Date', 'Company', 'Open', 'High', 'Low', 'Close', 'No. of Shares'])
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data to {filename}: {e}")

def process_all_stock_data(symbols, start_date, end_date):
    all_data = []
    for symbol in symbols:
        df = fetch_yahoo_finance_data(symbol, start_date, end_date)
        if df is not None:
            all_data.append(df)
        else:
            print(f"Failed to fetch data for {symbol}")

    if all_data:
        save_combined_data_to_csv(all_data, "combined_stock_data.csv")

def main():
    
    ticker_options = [
        "RELIANCE.BO", "TCS.BO", "INFY.BO", "HDFCBANK.BO",
        "ICICIBANK.BO", "HINDUNILVR.BO", "KOTAKBANK.BO", "SBI.BO",
        "BAJFINANCE.BO", "ITC.BO", "HCLTECH.BO", "M&M.BO",
        "L&T.BO", "AXISBANK.BO", "ONGC.BO", "HDFC.BO",
        "BHARTIARTL.BO", "MARUTI.BO", "DRREDDY.BO", "ADANIGREEN.BO",
        "TATAMOTORS.BO", "CIPLA.BO", "TATASTEEL.BO", "NTPC.BO",
        "POWERGRID.BO", "TCS.BO", "TATAMOTORS.BO", "TATASTEEL.BO", 
        "TATAPOWER.BO", "TATACHEM.BO", "TATAELXSI.BO", "TITAN.BO", 
        "TATACONSUMER.BO", "TATACOMM.BO", "TATAINVEST.BO", 
        "BAJAJELEC.NS", "BAJAJHIND.NS", "BAJFINANCE.NS",
        "BAJAJHLDNG.NS", "BAJAJSTEEL.NS", "BAJAJ-AUTO.NS", 
        "BAJAJFINSV.NS", "BAJAJCON.NS", "BAJAJHC.NS",
        "ABB.BO", "AEGISLOG.BO", "ARE&M.BO", "AMBALALSA.BO", 
        "ANDHRAPET.BO", "ANSALAPI.BO", "UTIQUE.BO", "ARUNAHTEL.BO", 
        "BOMDYEING.BO", "ASIANHOTNR.BO", "ATUL.BO", "ATVPR.BO", 
        "BAJAJELEC.BO", "BAJAJHIND.BO", "FORCEMOT.BO", "BAJFINANCE.BO", 
        "BALRAMCHIN.BO", "BANCOINDIA.BO", "CENTURYTEX.BO", 
        "BANARISUG.BO", "BASF.BO", "BATAINDIA.BO", "BEML.BO", 
        "BEL.BO", "BEPL.BO"
    ]
    
    start_dates = {
        "2019-01-01": "2020-12-31",
        "2021-01-01": "2022-12-31",
        "2017-01-01": "2018-12-31",
        "2015-01-01": "2016-12-31"
    }

    all_data = []
    
    for start_date, end_date in start_dates.items():
        for symbol in ticker_options:
            df = fetch_yahoo_finance_data(symbol, start_date, end_date)
            if df is not None:
                all_data.append(df)
            else:
                print(f"Failed to fetch data for {symbol} from {start_date} to {end_date}")

    if all_data:
        save_combined_data_to_csv(all_data, "all_stock_data.csv")

if __name__ == "__main__":
    main()
