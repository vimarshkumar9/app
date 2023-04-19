import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta
import yfinance as yf

# AWS MySQL Database Configuration
config = {
    'user': 'admin',
    'password': 'admin123',
    'host': 'myapp.c5uhvekimwws.eu-north-1.rds.amazonaws.com',
    'database': 'stock_data'
}

# Tickers of the companies to be scraped
tickers = ['AAPL', 'AMZN', 'GOOG', 'TSLA','NVDA', 'JPM', 'WMT', 'V', 'JNJ', 'PG', 'UNH', 'MA', 'BAC', 'HD', 'DIS', 'KO', 'ADBE', 'CRM']

try:
    # Establishing connection to MySQL Database
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Creating table to store company details if it doesn't exist
    cursor.execute("""CREATE TABLE IF NOT EXISTS companies (
                      ticker VARCHAR(10) NOT NULL PRIMARY KEY,
                      company_name VARCHAR(255) NOT NULL,
                      exchange VARCHAR(255) NOT NULL,
                      industry VARCHAR(255) NOT NULL)""")
    print("Table companies created successfully.")

    # Creating table to store stock prices if it doesn't exist
    cursor.execute("""CREATE TABLE IF NOT EXISTS stock_prices (
                      ticker VARCHAR(10) NOT NULL,
                      date DATE NOT NULL,
                      open_price FLOAT NOT NULL,
                      high_price FLOAT NOT NULL,
                      low_price FLOAT NOT NULL,
                      close_price FLOAT NOT NULL,
                      volume FLOAT NOT NULL,
                      PRIMARY KEY (ticker, date))""")
    print("Table stock_prices created successfully.")

    # Scraping stock prices for each ticker
    for ticker in tickers:
        # Retrieving data for the last 10 years
        ten_years_ago = (datetime.today() - timedelta(days=365*10)).strftime('%Y-%m-%d')
        today = datetime.today().strftime('%Y-%m-%d')
        data = yf.download(ticker, start=ten_years_ago, end=today)

        # Saving company details to companies table
        company_info = yf.Ticker(ticker).info
        company_name = company_info['longName']
        exchange = company_info['exchange']
        industry = company_info['industry']
        cursor.execute("""INSERT INTO companies (ticker, company_name, exchange, industry)
                          VALUES (%s, %s, %s, %s)
                          ON DUPLICATE KEY UPDATE 
                          company_name = VALUES(company_name), 
                          exchange = VALUES(exchange), 
                          industry = VALUES(industry)""",
                       (ticker, company_name, exchange, industry))

            # Loop over the rows in the data and insert them into the MySQL table
        for index, row in data.iterrows():
            # Convert numpy.float64 to regular float
            open_price = float(row['Open'])
            high_price = float(row['High'])
            low_price = float(row['Low'])
            close_price = float(row['Close'])
            volume = float(row['Volume'])
            
            # Insert data into MySQL table
            cursor.execute("""INSERT INTO stock_prices (ticker, date, open_price, high_price, low_price, close_price, volume)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                            ON DUPLICATE KEY UPDATE 
                            open_price = VALUES(open_price), 
                            high_price = VALUES(high_price), 
                            low_price = VALUES(low_price), 
                            close_price = VALUES(close_price), 
                            volume = VALUES(volume)""",
                        (ticker, index.strftime('%Y-%m-%d'), open_price, high_price, low_price, close_price, volume))
        conn.commit()
        print(f"Data for {ticker} saved successfully.")

except Error as e:
    print(f"Error connecting to MySQL Database: {e}")

finally:
    # Closing database connection
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed.")
