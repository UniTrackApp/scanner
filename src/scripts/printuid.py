from mfrc522 import BasicMFRC522

reader = BasicMFRC522()
reading = True

if __name__ == "__main__":
    try:
        while reading:
            print("\n✨ Welcome to UniTrack ✨")
            print("\n-------------------")

            print("\nScan card: ")
            # Fetching the card UID and converting it to HEX
            card_id = f"{reader.read_id():X}"
            # Printing on terminal the UID for reference
            print(card_id)

    except KeyboardInterrupt as error:
        print(f"Exiting: {error}")

    finally:
        reader.MFRC522.Close()
