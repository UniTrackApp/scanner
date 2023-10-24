# Client for the Attendance System
# Author: Andrea La Fauci
# Group 7 - Lewis Johnson, Aryan Prince Santy, Andrea La Fauci De Leo
import json
import os
from mfrc522 import MFRC522
import requests

reader = MFRC522()
cardIdentifier = None
status = None

CON_ERROR = "Error trying to connect to the host"


# Establish a connection with the card
def turnLightGreen():
    print("The light is green")


def turnLightRed():
    print("The light is red")


while status != reader.MI_OK:
    (status, uid) = reader.Request(reader.PICC_REQIDL)
    # If a card is nearby change the status
    if status == reader.MI_OK:
        # Fetch the UID from the card and store it into the variable
        cardIdentifier = reader.SelectTag(uid)
        # Connecting to the server
        try:
            request = requests.post(os.getenv('REST_API'), cardIdentifier)
            # TODO: Below is pseudo code to receive the request. To implement!
            response = requests.get('REST_API').json()
            responseID = json.loads(response)

            if responseID == True:
                turnLightGreen()
            else:
                turnLightRed()

        except ConnectionError:
            print(CON_ERROR)
        # Closing the reader releasing any data
        reader.StopAuth()

        # TODO: Check UID and then confirm it is the same with Server
        # This is unsafe and ideally we need to read a block from a sector and check if it's the card.
        # To do this is easy based on documentation at https://pypi.org/project/mfrc522-python/
