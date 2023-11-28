#from mfrc522 import BasicMFRC522

#reader = BasicMFRC522()


def confirmation():
    print("\n-------------------")
    print("\nConfirm Registration? (y/n)")
    return input().upper().strip()


if __name__ == "__main__":
    try:
        print("\n✨ Welcome to UniTrack ✨")
        print("\nRegister Student 👇")
        print("\n-------------------")

        print("\nScan your card first to start registration")
        # Fetching the card UID and converting it to HEX
        #card_id = f"{reader.read_id():X}"
        card_id = input().strip().upper()
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

        confirm = confirmation()

        match confirm:
            case "Y":
                print("\n-------------------")
                print("\nRegistering Student...")
                # TODO: Register student in database using all info using an API

            case "N":
                print("\n-------------------")
                print("\nExiting...")
                exit()

            case _:
                print("\n-------------------")
                print("\nWrong input...")
                confirm = confirmation()

    except KeyboardInterrupt as error:
        print(f"Exiting: {error}")

    finally:
        #reader.MFRC522.Close()
        pass
