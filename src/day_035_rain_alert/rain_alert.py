from requests import get
from time import strftime, gmtime


OPEN_WEATHER_MAP_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
# TODO do not put this in VCS
OPEN_WEATHER_MAP_API_KEY = ""
LATITUDE = 49.738430
LONGITUDE = 13.373637


########################################################################################################################

def check_weather(forecast: dict) -> None:
    """
    Check all 3h segments of the input forecast; print a message if it will rain.

    :param forecast: json forecast from openweathermap API
    """

    for weather_segment in forecast["list"]:
        for condition in weather_segment["weather"]:
            # https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
            if condition["id"] < 700:
                print(strftime('%Y-%m-%d %H:%M:%S', gmtime(weather_segment["dt"])))
                print("bring an umbrella")


########################################################################################################################

def get_12h_forecast() -> dict:
    """
    :return: json forecast from openweathermap API (next 12h)
    """

    response = get(url=OPEN_WEATHER_MAP_ENDPOINT, params={
        "lat": LATITUDE,
        "lon": LONGITUDE,
        "cnt": 4,
        "appid": OPEN_WEATHER_MAP_API_KEY
    })
    response.raise_for_status()
    return response.json()


########################################################################################################################

def run_program() -> None:
    """
    Get 12h forecast; check it for rain.
    """

    forecast = get_12h_forecast()
    check_weather(forecast)

########################################################################################################################
