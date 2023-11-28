from mfrc522 import BasicMFRC522

reader = BasicMFRC522()
reading = True

while reading:
    print("\nScan Card")
    # Fetching the card UID and converting it to HEX
    card_id = f'{reader.read_id():X}'
    # Printing on terminal the UID for reference
    print(card_id)
    break
