import yfinance as yf
import pandas as pd

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
        return df
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def save_stock_data(symbols, start_date, end_date):
    for symbol in symbols:
        df = fetch_yahoo_finance_data(symbol, start_date, end_date)
        
        if df is not None:
            df.to_csv(f"{symbol}_stock_data_2017_2018.csv", index=False)
            print(f"Data for {symbol} saved to {symbol}_stock_data_2019_2020.csv")
        else:
            print(f"Failed to fetch or save data for {symbol}")

def main():
    # List of tickers
    ticker_options = [
        "RELIANCE.BO", "TCS.BO", "INFY.BO", "HDFCBANK.BO",
        "ICICIBANK.BO", "HINDUNILVR.BO", "KOTAKBANK.BO", "SBI.BO",
        "BAJFINANCE.BO", "ITC.BO", "HCLTECH.BO", "M&M.BO",
        "L&T.BO", "AXISBANK.BO", "ONGC.BO", "HDFC.BO",
        "BHARTIARTL.BO", "MARUTI.BO", "DRREDDY.BO", "ADANIGREEN.BO",
        "TATAMOTORS.BO", "CIPLA.BO", "TATASTEEL.BO", "NTPC.BO",
        "POWERGRID.BO"
    ]
    
    # Display options
    print("Select ticker symbols to include in the CSV file:")
    for i, ticker in enumerate(ticker_options, 1):
        print(f"{i}. {ticker}")
    print(f"{len(ticker_options) + 1}. Exit")

    # Get user selection
    selected_indices = input("Enter the numbers of the ticker symbols you want to include (comma-separated): ")
    selected_indices = selected_indices.split(',')

    if len(selected_indices) > len(ticker_options) + 1 or len(selected_indices) == 0:
        print("Invalid selection. Exiting.")
        return

    selected_symbols = []
    for index in selected_indices:
        index = index.strip()
        if index.isdigit():
            index = int(index)
            if index == len(ticker_options) + 1:
                print("Exiting.")
                return
            elif 1 <= index <= len(ticker_options):
                selected_symbols.append(ticker_options[index - 1])
            else:
                print(f"Invalid index: {index}. Skipping.")
        else:
            print(f"Invalid input: {index}. Skipping.")

    if not selected_symbols:
        print("No valid ticker symbols selected. Exiting.")
        return

    start_date = "2017-01-01"
    end_date = "2018-12-31"
    save_stock_data(selected_symbols, start_date, end_date)

if __name__ == "__main__":
    main()
