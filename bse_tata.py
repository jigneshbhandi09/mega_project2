import yfinance as yf
import pandas as pd

def get_stock_data(symbol, start_date, end_date):
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

def save_combined_data_to_csv(df, filename):
    try:
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data to {filename}: {e}")

def process_all_stock_data(symbols, start_date, end_date):
    all_data = []
    for symbol in symbols:
        df = get_stock_data(symbol, start_date, end_date)
        
        if df is not None:
            all_data.append(df)
        else:
            print(f"Failed to fetch or save data for {symbol}")

    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        save_combined_data_to_csv(combined_df, "tata_group_stock_data_2021_2022.csv")

def main():
    
    tata_group_tickers = [
        "TCS.BO", "TATAMOTORS.BO", "TATASTEEL.BO", "TATAPOWER.BO",
        "TATACHEM.BO", "TATAELXSI.BO", "TITAN.BO", "TATACONSUMER.BO",
        "TATACOMM.BO", "TATAINVEST.BO"
    ]
    
    start_date = "2021-01-01"
    end_date = "2022-12-31"
    process_all_stock_data(tata_group_tickers, start_date, end_date)

if __name__ == "__main__":
    main()
