import requests
from datetime import datetime

stock_symbol = input("Enter the stock symbol for the company you would like data for: ")

chart_type = input("Enter the chart type that you would like (line/bar): ")

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

# Ask for the end date in YYYY-MM-DD format.
def ask_end_date(prompt: str, begin_date: str) -> str:
    while True:
        s = input(prompt).strip()
        try:
            datetime.strptime(s, "%Y-%m-%d")
            if s >= begin_date:
                return s
            else:
                print("End date cannot be before the beginning date. Try again.")
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format (e.g., 2024-10-20).")

end_date = ask_end_date("Enter the end date (YYYY-MM-DD): ", begin_date)

api_key = "G6S32AHULPHG2KS5"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api_key}"
response = requests.get(url)
data = response.json()

# Generate a graph and open it in the user’s default browser.
import matplotlib.pyplot as plt

# Get the proper time series key
key_name = next((k for k in data.keys() if "Time Series" in k), None)
if not key_name:
    print("Error: Could not find time series data in API response.")
    exit()

time_series = data[key_name]
dates = []
closing_prices = []

for date_str, daily_data in time_series.items():
    if begin_date <= date_str <= end_date:
        dates.append(datetime.strptime(date_str, "%Y-%m-%d"))
        closing_prices.append(float(daily_data["4. close"]))

# Handle case with no data in range
if not dates:
    print("No data found for the given date range.")
    exit()

# Sort data by date
dates, closing_prices = zip(*sorted(zip(dates, closing_prices)))

# Create the plot
plt.figure(figsize=(10, 6))

if chart_type.lower() == "bar":
    plt.bar(dates, closing_prices, color='skyblue', label='Closing Price')
else:
    plt.plot(dates, closing_prices, marker='o', linestyle='-', label='Closing Price')

plt.title(f"{stock_symbol.upper()} Closing Prices from {begin_date} to {end_date}")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save and display
plt.savefig("stock_chart.png")
plt.show()