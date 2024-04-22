from os.path import join, dirname, realpath
from csv import reader

WEATHER_DATA_FILE = "weather_data.csv"
WEATHER_DATA_PATH = join(dirname(realpath(__file__)), WEATHER_DATA_FILE)


########################################################################################################################

def run_program() -> None:
    """

    """

    with open(WEATHER_DATA_PATH, "r") as f:
        data = reader(f)
        temperatures = list(int(row[1]) for row in list(data)[1:])
        print(temperatures)

########################################################################################################################
