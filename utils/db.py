import os

import psycopg2
from dotenv import load_dotenv


load_dotenv()


class Database():
    _instance = None
    _parameters: str

    def __init__(self, parameters: str = f"host={os.getenv('DB_HOST')} dbname={os.getenv('DB_NAME')} user={os.getenv('DB_USER')} password={os.getenv('DB_PASSWORD')} port={os.getenv('DB_PORT')}"):
        if Database._instance != None:
            raise Exception("There is another database instace running")
        else:
            print("creating database")
            Database._instance = self
            self._parameters = parameters

    @staticmethod
    def getInstance():
        if Database._instance == None:
            Database()
        return Database._instance

    def execute(self, sql_query):
        connection = psycopg2.connect(self._parameters)
        cursor = connection.cursor()
        result = self.query(cursor, sql_query)
        self.close(cursor, connection)
        return result

    def query(self, cursor, sql_query):
        cursor.execute(sql_query)
        return cursor.fetchall()

    def close(self, cursor, connection):
        if cursor:
            cursor.close()
        if connection:
            connection.close()
