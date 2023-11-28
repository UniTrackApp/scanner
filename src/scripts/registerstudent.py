from mfrc522 import BasicMFRC522

reader = BasicMFRC522()

if __name__ == "__main__":
    try:
        print("\n✨ Welcome to UniTrack ✨")
        print("\nRegister Student 👇")
        print("\n-------------------")

        print("\nScan your card first to start registration")
        # Fetching the card UID and converting it to HEX
        card_id = f"{reader.read_id():X}"
        # Printing on terminal the UID for reference
        print(f"This is your card UID: {card_id}")

        print("\nEnter Student ID: ")
        student_id = input()
        print("\nEnter Fist Name: ")
        first_name = input()
        print("\nEnter Last Name: ")
        last_name = input()

        print("\n-------------------")
        print("\nConfirm Registration 👇")
        print("\n-------------------")
        print(f"\nStudent ID: {student_id}")
        print(f"\nFirst Name: {first_name}")
        print(f"\nLast Name: {last_name}")
        print(f"\nCard UID: {card_id}")

        print("\n-------------------")
        print("\nConfirm Registration? (y/n)")
        confirm = input()

        if confirm == "y":
            print("\n-------------------")
            print("\nRegistering Student...")
            # TODO: Register student in database using all info using an API
        else:
            print("\n-------------------")
            print("\nExiting...")
            exit()

    except KeyboardInterrupt as error:
        print(f"Exiting: {error}")

    finally:
        reader.MFRC522.Close()
