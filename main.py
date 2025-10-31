import requests

stock_symbol = input("Enter the stock symbol for the company you would like data for: ")

chart_type = input("Enter the chart type that you would like: ")

api_key = "G6S32AHULPHG2KS5"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api_key}"
response = requests.get(url)
data = response.json()

#Ask the user for the time series function they want the api to use.
print("\nChoose a time series function:")
print("1) TIME_SERIES_DAILY")
print("2) TIME_SERIES_WEEKLY")
print("3) TIME_SERIES_MONTHLY")
choice = input("Enter 1, 2, or 3: ").strip()

if choice == "1":
    function = "TIME_SERIES_DAILY"
elif choice == "2":
    function = "TIME_SERIES_WEEKLY"
elif choice == "3":
    function = "TIME_SERIES_MONTHLY"
else:
    print("Invalid choice. Defaulting to TIME_SERIES_DAILY.")
    function = "TIME_SERIES_DAILY"

#Ask the user for the beginning date in YYYY-MM-DD format.
def ask_date(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        try:
            datetime.strptime(s, "%Y-%m-%d") 
            return s
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format (e.g., 2024-10-15).")

begin_date = ask_date("Enter the beginning date (YYYY-MM-DD): ")