import os
import requests
from dotenv import load_dotenv

# Loading the Env variables - Be sure to have them
load_dotenv()

# The URL for the endpoint in the env variables
URL = os.getenv('API_UID')


def check_uid(uid):
    """Function queries the server if the UID is in the database"""
    # The payload to send to the endpoint to be checked
    param = {'uid': uid}
    try:
        # Sending the request
        response = requests.get(URL, params=param)
        # Converting it into dictionary
        data = response.json()
        # If the data is empty will return false
        return True if data else False
    except Exception as e:
        print(f'Error: {e}')


def light(color):
    """
    Function which prints Red or Green light
    TODO: To be replaced with turning the LED on in Red and Green
    """
    print(f'{color} light')


if __name__ == '__main__':
    try:
        while True:
            uniqueid = input("Insert UID: ").upper().strip()
            if check_uid(uniqueid):
                light("Green")
            else:
                light("Red")
    except KeyboardInterrupt:
        print("\nExiting")
