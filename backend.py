import os
from dotenv import load_dotenv, dotenv_values
import requests as r

load_dotenv()
config = dotenv_values(".env")
key = os.getenv("API_KEY")


def get_data(place, forcast_days, kind):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={key}"
    res = r.get(url)
    data = res.json()
    filter_data = data["list"]
    number_values = 8 * forcast_days
    filter_data = filter_data[:number_values]

    if kind == "Temperature":
        filter_data = [dt["main"]["temp"] for dt in filter_data]
    if kind == "Sky":
        filter_data = [dt["weather"][0]["main"] for dt in filter_data]

    return filter_data


if __name__ == "__main__":
    print(get_data(place="cairo", forcast_days=3, kind="Temperature"))
