import threading

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
message = ""


def input_thread():
    global message
    while True:
        message = input("Enter a message: ")


# Start a separate thread for continuously asking for input
input_thread = threading.Thread(target=input_thread)
input_thread.daemon = True
input_thread.start()


@app.route('/')
def display_hello():
    return jsonify({"hi": "Head to /message to see the message"})


@app.route('/message')
def get_message():
    return jsonify({"message": message})


if __name__ == '__main__':
    app.run(threaded=True)
