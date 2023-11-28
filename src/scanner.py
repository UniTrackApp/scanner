import os
from time import sleep
import requests
from dotenv import load_dotenv
from gpiozero import RGBLED
from mfrc522 import BasicMFRC522
from constants.colour import Colour
from constants.lecture_id import LectureId
from constants.status import Status

# Loading the Env variables - Be sure to have them
load_dotenv()

# The URL for the endpoint in the env variables
URL = os.getenv('API_UID')
ATTENDANCE_URL = os.getenv('API_ATTENDANCE')
# The GPIO pins used for the lights
LED = RGBLED(red=18, blue=6, green=26)
# The RFID reader
reader = BasicMFRC522()
# Running flag
reading = True


def send_uid(uid):
    """Function queries the server if the UID is in the database"""
    # The payload to send to the endpoint to be checked
    param = {'uid': uid}
    try:
        # Sending the request
        response = requests.get(URL, params=param)
        return True if response.status_code == 200 else False

    except Exception as e:
        print(f'Error: {e}')


def write_attendance(uid, lectureId):
    """
    It sends the UID and LectureId to the Server which will create an entry in the database.
    It then returns the status of the student based on time.

    :param uid: The card's Unique ID
    :param lectureId: The lecture ID used by the specific scanner
    :returns: The Student Status 
    """
    data = {'uid': uid, 'lectureId': lectureId}
    try:
        response = requests.post(ATTENDANCE_URL, json=data)
        json_response = response.json()
        # The status as response from the request
        json_status = response.json()
        for key in json_response:
            if key == 'error':
                status = json_response['error']
                break
            else:
                status = json_response['status']
                break
        return status
    
    except Exception as e:
        print(f'Error:  {e}')

    
def light(color):
    """It lights the LED in different colors for 1 second and turns it off"""

    # Red Color
    if color == Colour.RED.value:
        LED.red = 1
        sleep(1)
        LED.off()
    # Green Color
    elif color == Colour.GREEN.value:
        LED.green = 1
        sleep(1)
        LED.off()
    # Amber Color
    elif color == Colour.AMBER.value:
        LED.color = (1, 0.5, 0)
        sleep(1)
        LED.off()


if __name__ == '__main__':
    try:
        while reading:
            print("\nScan Card")
            # Fetching the card UID and converting it to HEX
            card_id = f'{reader.read_id():X}'
            # Printing on terminal the UID for reference
            print(card_id)
            status = write_attendance(card_id, lectureId=LectureId.COMP_ASD)
            
            # Light will go green or red based on the status returned from the API call
            match status:
                case Status.PRESENT.value:
                    light(Colour.GREEN.value)
                
                case Status.LATE.value:
                    light(Colour.AMBER.value)
                    
                case _:
                    light(Colour.RED.value)
            sleep(1)

    except KeyboardInterrupt as error:
        # Resetting the running flag
        reading = False
        print(f"Exiting: {error}")
    
    finally:
        # Freeing the GPIO resources for the reader
        reader.MFRC522.Close()
