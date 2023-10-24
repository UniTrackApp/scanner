import requests
import os

uid = 123


def send_post(data):
    requests.post(os.getenv('API_HOST'), data)


def respond(response):
    if response == uid:
        print("Accepted")

    else:
        print("Refused")


if __name__ == '__main__':
    send_post(uid)
