import requests

stock_symbol = input("Enter the stock symbol for the company you would like data for: ")

chart_type = input("Enter the chart type that you would like: ")

api_key = "G6S32AHULPHG2KS5"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api_key}"
response = requests.get(url)
data = response.json()