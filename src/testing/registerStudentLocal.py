import requests
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("API_CREATE_STUDENT")


def confirmation():
    print("\n-------------------")
    print("\nConfirm Registration? (y/n)")
    return input().upper().strip()


def registerStudent(url, studentInfo):
    try:
        response = requests.post(url, json=studentInfo)
        if response.status_code == 400:
            raise Exception("Bad Request")
        else:
            return True

    except Exception as e:
        print(f"Error: {e} - {response.json().get('error')}")
        return False


if __name__ == "__main__":
    try:
        print("\n✨ Welcome to UniTrack ✨")
        print("\nRegister Student 👇")
        print("\n-------------------")

        print("\nScan your card first to start registration")
        card_id = input().strip().upper()
        # Printing on terminal the UID for reference
        print(f"This is your card UID: {card_id}")

        print("\nEnter Student ID: ")
        student_id = input().strip()
        print("\nEnter Fist Name: ")
        first_name = input().capitalize().strip()
        print("\nEnter Last Name: ")
        last_name = input()

        print("\n-------------------")
        print("\nConfirm Registration 👇")
        print("\n-------------------")
        print(f"\nStudent ID: {student_id}")
        print(f"\nFirst Name: {first_name}")
        print(f"\nLast Name: {last_name}")
        print(f"\nCard UID: {card_id}")

        data = {
            "studentId": student_id,
            "studentCardId": card_id,
            "firstName": first_name,
            "lastName": last_name,
        }

        confirm = confirmation()

        match confirm:
            case "Y":
                print("\n-------------------")
                print("\nRegistering Student...")

                if registerStudent(URL, data):
                    print("\n-------------------")
                    print("\nRegistration Successful")
                else:
                    print("\n-------------------")
                    print("\nRegistration Failed")
                    print("\n-------------------")

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
        pass
