import os
from time import sleep
import requests
from dotenv import load_dotenv
from gpiozero import RGBLED
from mfrc522 import BasicMFRC522
# We should not mix RPi.GPIO and gpiozero to avoid corruption - Disabled for now
# import RPi.GPIO as GPIO

# Loading the Env variables - Be sure to have them
load_dotenv()


# The URL for the endpoint in the env variables
URL = os.getenv('API_UID')
# The GPIO pins used for the lights
LED = RGBLED(red=18, blue=6, green=26)
GREEN = "GREEN"
RED = "RED"
# The RFID reader
reader = BasicMFRC522()
# Running flag
reading = True


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
        while reading:
            print("\nScan Card")
            # Fetching the card UID and converting it to HEX
            card_id = f'{reader.read_id():x}'.upper()
            # Printing on terminal the UID for reference
            print(card_id)
            # Light will go green or red based on the UID being in the database on server
            light(GREEN) if check_uid(card_id) else light(RED)
            sleep(1)

    except KeyboardInterrupt as error:
        # Resetting the running flag
        reading = False
        print(f"Exiting: {error}")
    
    finally:
        # Freeing the GPIO resources
        LED.off()
        # GPIO.cleanup()
