import os
import json
import requests
import pandas as pd
import datetime as dt


cwd = os.getcwd()


class EarningsEstimates:
    def __init__(self, ticker: str, alpha_vantage_key: str) -> None:
        self.ticker = ticker.upper()
        self.key = alpha_vantage_key
        self.base_export_path = f"{self._get_data_export_path()}\\{self.ticker}.csv"
        # List of possible function parameters for financial report frequency.
        self.quarterly_params = [
            "q",
            "Q",
            "Quarter",
            "quarter",
            "Quarterly",
            "quarterly",
        ]

    """-------------------------------"""

    def _get_chrome_driver_path(self):
        with open("config.json", "r") as file:
            data = json.load(file)
        path = data["chrome_driver_path"]
        return path

    """-------------------------------"""

    def _get_data_export_path(self):
        with open("config.json", "r") as file:
            data = json.load(file)
        path = data["data_export_path"]
        return path

    """-------------------------------"""

    def get_predefined_path(self):
        return f"{cwd}\\Profiles\\EarningsEstimates\\Earnings\\{self.ticker}.csv"

    """-------------------------------"""

    def get_earnings_estimates(self, frequency: str = "q"):
        if frequency in self.quarterly_params:
            frequency = "quarterlyEarnings"
        elif frequency in self.annual_params:
            frequency = "annualEarnings"

        # Construct the API request URL
        endpoint = "https://www.alphavantage.co/query"
        params = {"function": "EARNINGS", "symbol": self.ticker, "apikey": self.key}

        # Make the api request.
        response = requests.get(endpoint, params=params)

        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()[frequency]
            df = pd.DataFrame(data)
            return df
        else:
            print(f"[Error] Retrieving Earnings Estimates")

    """-------------------------------"""

    def get_all_data(self, frequency: str = "q"):
        # Number that decides if the program needs to fetch new data.
        date_threshold = 90

        try:
            earnings_csv_data = pd.read_csv(self.base_export_path)
            # Get the most recent reporting date.
            most_recent_reporting_date = earnings_csv_data["reportedDate"].iloc[0]
            date_difference = self.get_date_difference(
                target_date=most_recent_reporting_date,
                compare_date=str(dt.datetime.now().date()),
            )

            # If date_difference is greater, fetch new data and write the new rows to the csv file.
            if date_difference > date_threshold:
                # Fetch new earnings data.
                earnings = self.get_earnings_estimates(frequency=frequency)
                # Merge the dataframe from the csv file, and the new dataframe from the earnings file.
                merged_df = pd.concat([earnings_csv_data, earnings], ignore_index=True)
                merged_df = merged_df.drop_duplicates()
                merged_df.to_csv(self.base_export_path, header=True, index=False)
                return merged_df

        except FileNotFoundError as e:
            print(f"[Error] {e}")
            earnings = self.get_earnings_estimates(frequency)
            earnings.to_csv(self.base_export_path, header=True, index=False)
            return earnings


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()
    alpha_vantage_key = os.getenv("alpha_vantage_key")
    e = EarningsEstimates("AAPL", alpha_vantage_key=alpha_vantage_key)

    df = e.get_all_data()