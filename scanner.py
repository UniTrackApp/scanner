import os

import psycopg2
import psycopg2 as pgdb
from dotenv import load_dotenv

# Loading env variables
load_dotenv()

DB_HOST = os.getenv('PGHOST')
DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_PORT = os.getenv('POSTGRES_PORT')

try:
    # Establishing connection with DB
    conn = pgdb.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT)
except Exception as error:
    # Handling connection errors
    print(f"Error on Connection: {type(error)}")


def check_uid(uid):
    """Function which checks the UID against the table on DB"""
    cursor = conn.cursor()
    # Query for the Database
    query = 'SELECT * FROM "Student" WHERE "studentCardId"=%s'
    try:
        # Executing the query
        cursor.execute(query, (uid,))
        result = cursor.fetchall()
        # If the Tuple returned is empty hence no results it will return False
        return True if result else False
    # Handling potential errors querying the database
    except psycopg2.Error:
        return False


def light(color):
    """
    Function which prints Red or Green light
    TODO: To be replaced with turning the LED on in Red and Green
    """
    print(f'{color} light')


if __name__ == '__main__':
    try:
        while True:
            uniqueid = input("Insert UID: ").capitalize()
            if check_uid(uniqueid):
                light("Green")
            else:
                light("Red")
    except KeyboardInterrupt:
        # Closing the connection to the database
        conn.close()
        pass
