import json
import os

from dotenv import load_dotenv

from utils.get_weather import (
    get_daily_forecast,
    get_location_key
)

load_dotenv()
api_key = os.getenv("API_KEY")


def main():
    location_name = "Moscow"
    location_key = get_location_key(location_name, api_key)
    if location_key:

        daily_forecast = get_daily_forecast(location_key, api_key)
        if daily_forecast:
            print("\nПрогноз погоды на завтра:")
            print(daily_forecast)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'response.json')

        with open(file_path, 'w') as f:
            json.dump(daily_forecast, f, indent=4)


if __name__ == "__main__":
    main()
