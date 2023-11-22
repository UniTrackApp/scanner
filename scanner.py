import os
from time import sleep
import requests
from dotenv import load_dotenv
from gpiozero import RGBLED

# Loading the Env variables - Be sure to have them
load_dotenv()

# The URL for the endpoint in the env variables
URL = os.getenv('API_UID')
LED = RGBLED(red=17, blue=27, green=22)
GREEN = "GREEN"
RED = "RED"


def check_uid(uid):
    """Function queries the server if the UID is in the database"""
    # The payload to send to the endpoint to be checked
    param = {'uid': uid}
    try:
        # Sending the request
        response = requests.get(URL, params=param)
        return True if response.status_code == 200 else False

    except Exception as e:
        print(f'Error: {e}')


def light(color):
    """It lights the LED in different colors for 1 second and turns it off"""
    if color == RED:
        LED.red = 1
        sleep(1)
        LED.off()

    elif color == GREEN:
        LED.green = 1
        sleep(1)
        LED.off()


if __name__ == '__main__':
    try:
        while True:
            uniqueid = input("Insert UID: ").upper().strip()
            if check_uid(uniqueid):
                light(GREEN)
            else:
                light(RED)

    except KeyboardInterrupt:
        print("\nExiting")
