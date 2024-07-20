import yfinance as yf
import pandas as pd

def fetch_and_save_company_data(symbols, num_companies, start_date='2021-01-01', end_date='2022-12-31', output_file='tata_group_company_data.csv'):
   
   
    num_companies = min(num_companies, len(symbols))
    
    # Select the specified number of symbols
    selected_symbols = symbols[:num_companies]
    
    # Dictionary to store the data for each company
    company_data = {}
    
    # Fetch data for each company
    for symbol in selected_symbols:
        print(f"Fetching data for {symbol}...")
        data = yf.download(symbol, start=start_date, end=end_date)
        if not data.empty:
            data['Company'] = symbol
           
            data_sampled = data.iloc[::10]
            company_data[symbol] = data_sampled[['Open', 'High', 'Low', 'Close', 'Volume']]
            print(f"Data for {symbol}:\n", data_sampled.head(), "\n")
    
    # Combine data
    combined_data = pd.concat(company_data, keys=company_data.keys(), names=['Company', 'Date'])
    
    
    combined_data.reset_index(level=0, inplace=True)
    
    
    combined_data.rename(columns={'Volume': 'No. of Shares'}, inplace=True)
    
    # Save the combined data to a CSV file
    combined_data.to_csv(output_file, index=False)
    
    print(f"Data has been saved to '{output_file}'")

# tata companies 
symbols = [
    'TCS.BO', 'TATAMOTORS.BO', 'TATASTEEL.BO', 'TATAPOWER.BO',
    'TATACHEM.BO', 'TATAELXSI.BO', 'TITAN.BO', 'TATACONSUMER.BO',
    'TATACOMM.BO', 'TATAAD.BO', 'TATAINVEST.BO', 'TATASPONGE.BO',
    'TATAMETALI.BO', 'TATACOFFEE.BO', 'TATASTEELLONG.BO', 'TATTELESER.BO',
    'TATAREALTY.BO', 'TATAHOUSING.BO', 'TATAENGG.BO', 'TATAADVANCED.BO'
]

fetch_and_save_company_data(symbols, num_companies=10)
