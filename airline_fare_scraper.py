import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Target URL (hypothetical page that lists airline fare data)
url = "https://example.com/airline-ticket-prices"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Send HTTP request to the website
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Pause to simulate human browsing
time.sleep(2)

# Locate the table that contains flight fare data
table = soup.find("table", {"id": "flight-data"})

# If table not found, exit (helps avoid crashing in real scraping)
if table is None:
    print("Flight data table not found. Please check the site structure.")
    exit()

rows = table.find_all("tr")

data = []
for row in rows[1:]:  # Skip header row
    cols = row.find_all("td")
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

# Define column names based on the structure of the website
columns = [
    "Date_of_journey", "Journey_day", "Airline", "Flight_code", "Class",
    "Source", "Departure", "Total_stops", "Arrival", "Destination",
    "Duration_in_hours", "Days_left", "Fare"
]

# Convert list of data to a pandas DataFrame
df = pd.DataFrame(data, columns=columns)

# Uncomment below if you want to drop duplicates
# df.drop_duplicates(inplace=True)

# Save the scraped data to CSV for later use
df.to_csv("flight_prices_scraped.csv", index=False)

# Preview scraped data
print("Sample of scraped data:")
print(df.head())

# Uncomment this to inspect data types during preprocessing
# print(df.dtypes)
