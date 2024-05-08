from typing import Union
from requests import get
from datetime import datetime, timedelta, time as dt_time
from smtplib import SMTP
from os.path import join, dirname, realpath


########################################################################################################################

MY_LATITUDE = 49.746841
MY_LONGITUDE = 13.376990
# TODO: remove before VCS commit; fill before using the program
SENDER = ""
RECIPIENT = ""


########################################################################################################################

def _get_timedelta(time: dt_time) -> timedelta:
    """
    :param time: a time as a datetime.time object
    :return: datetime.timedelta object
    """

    return timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)


########################################################################################################################

def _load_password() -> Union[str, None]:
    """
    Read password to the email that is used for sending. This file exists only locally, for security reasons. No
    email or password will be under VCS.
    """

    try:
        with open(join(dirname(realpath(__file__)), "pass.txt"), "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


########################################################################################################################

def _send_email() -> None:
    """
    Send an email. It informs the recipient that ISS is currently overhead.
    """

    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER, password=_load_password())
        connection.sendmail(from_addr=SENDER,
                            to_addrs=RECIPIENT,
                            msg=f"Subject:ISS Overhead!\n\nLook Up!")


########################################################################################################################

def _is_nighttime() -> bool:
    """
    :return: True if it is currently nighttime (before sunrise or after sunset), False otherwise
    """

    response = get(url="https://api.sunrise-sunset.org/json", params={
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0
    })
    response.raise_for_status()
    sunrise = _get_timedelta(datetime.fromisoformat(response.json()["results"]["sunrise"]).time())
    sunset = _get_timedelta(datetime.fromisoformat(response.json()["results"]["sunset"]).time())
    now = _get_timedelta(datetime.now().time())

    return now < sunrise or now > sunset


########################################################################################################################

def _is_iss_overhead() -> bool:
    """
    :return: True if ISS is currently overhead (within 5 degrees margins), False otherwise
    """

    response = get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_latitude = float(response.json()["iss_position"]["latitude"])
    iss_longitude = float(response.json()["iss_position"]["longitude"])

    return (MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE + 5 and
            MY_LONGITUDE - 5 <= iss_longitude <= MY_LONGITUDE + 5)


########################################################################################################################

def run_program() -> None:
    """
    Send an email if it is nighttime and ISS is currently overhead.
    """

    if _is_iss_overhead() and _is_nighttime():
        _send_email()


########################################################################################################################
