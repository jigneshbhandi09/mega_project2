import yfinance as yf
import pandas as pd
import requests
from nsetools import Nse


def suraj():
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
                df.to_csv(f"{symbol}_stock_data_2019_2020.csv", index=False)
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

        start_date = "2019-01-01"
        end_date = "2020-12-31"
        save_stock_data(selected_symbols, start_date, end_date)

    if __name__ == "__main__":
        main()

# Call the suraj function to execute the script
suraj()





def hemant():
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

    # Call the main function inside hemant to execute the script
    main()

# Call the hemant function to execute the entire process
hemant()



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
            print(f"Data for {symbol} saved to {symbol}_stock_data_2017_2018.csv")
        else:
            print(f"Failed to fetch or save data for {symbol}")

def afiya():
    # List of tickers
    ticker_options = [
        "BAJAJELEC.NS", "BAJAJHIND.NS", "BAJFINANCE.NS",
        "BAJAJHLDNG.NS", "BAJAJSTEEL.NS",
        "BAJAJ-AUTO.NS", "BAJAJFINSV.NS", "BAJAJCON.NS",
        "BAJAJHC.NS"
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

# Now, calling the function afiya() will execute the entire process
afiya()




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
            df.to_csv(f"{symbol}_stock_data_2015_2016.csv", index=False)
            print(f"Data for {symbol} saved to {symbol}_stock_data_2015_2016.csv")
        else:
            print(f"Failed to fetch or save data for {symbol}")

def rahul():
    # List of tickers
    ticker_options = [
        "ABB.BO", "AEGISLOG.BO", "ARE&M.BO", "AMBALALSA.BO", "ANDHRAPET.BO", "ANSALAPI.BO", "UTIQUE.BO", 
        "ARUNAHTEL.BO", "BOMDYEING.BO", "ASIANHOTNR.BO", "ATUL.BO", "ATVPR.BO", "BAJAJELEC.BO", 
        "BAJAJHIND.BO", "FORCEMOT.BO", "BAJFINANCE.BO", "BALRAMCHIN.BO", "BANCOINDIA.BO", 
        "CENTURYTEX.BO", "BANARISUG.BO", "BASF.BO", "BATAINDIA.BO", "BEML.BO", "BEL.BO", "BEPL.BO"
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

    start_date = "2015-01-01"
    end_date = "2016-12-31"
    save_stock_data(selected_symbols, start_date, end_date)

# Now, calling the function rahul() will execute the entire process
rahul()



df1=pd.read_csv("bseall.csv")
df1=df1.drop(["Security Code","Security Name","Group","Face Value","ISIN No","Industry","Instrument","Sector Name","Industry New Name","Igroup Name","ISubgroup Name"], axis='columns')
sym=df1['Security Id'].head(10).to_list()
df1[df1['Status']=="Active"]
dat=[]
for i in sym:
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={i}.bse&interval=60min&month=2015-01&outputsize=full&apikey=7B9YZHUIXE9DOQ72'
    r = requests.get(url)
    data = r.json()
    # dat.append(data['Time Series (Daily)'])
    time_series = data['Time Series (Daily)']
    
    # Extract and format the data
    for date, daily_data in time_series.items():
        dat.append({
            "company": i,
            'Date': date,
            'Open': daily_data['1. open'],
            'High': daily_data['2. high'],
            'Low': daily_data['3. low'],
            'Close': daily_data['4. close'],
            'No. of Shares': daily_data['5. volume'],
        })
datafram=pd.DataFrame(dat)
datafram
