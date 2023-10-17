# Client for the Attendance System
# Author: Andrea La Fauci
# Group 7 - Lewis Johnson, Aryan Prince Santy, Andrea La Fauci De Leo

import socket
from mfrc522 import MFRC522 as MF


def connect(host, port):
    """
    Connect function which will be called to connect to a socket.
    :param host: The host to connect to
    :param port: The port used for the communication
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print("Connected")
            if cardIdentifier:
                s.send(str(cardIdentifier).encode("utf-8"))

        except ConnectionError:
            print(CON_ERROR)


# Constants # Host for now will be local host and port using a non-reserved port
HOST = "127.0.0.1"
PORT = 42069
CON_ERROR = "Error trying to connect to the host"

# The data to send likely a UID
cardIdentifier = None
# The card reader
reader = MF()
# Setting the status of the reader
status = None

# TODO: Change to an infinite loop to keep reading cards
# Establish a connection with the card
while status != reader.MI_OK:
    (status, uid) = reader.Request(reader.PICC_REQIDL)
    # If a card is nearby change the status
    if status == reader.MI_OK:
        # Fetch the UID from the card and store it into the variable
        cardIdentifier = reader.SelectTag(uid)
        # Connecting to the server
        connect(HOST, PORT)
        # Closing the reader releasing any data
        reader.Close()
        # TODO: Check UID and then confirm it is the same with Server
        # This is unsafe and ideally we need to read a block from a sector and check if it's the card.
        # To do this is easy based on documentation at https://pypi.org/project/mfrc522-python/
