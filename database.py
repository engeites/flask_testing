import sqlite3
from time import time


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("btc_history.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

        command1 = """CREATE TABLE IF NOT EXISTS
        btc_history(price REAL, time TEXT)"""
        self.cursor.execute(command1)

    def add_entry(self, price):
        milliseconds = lambda: int(time() * 1000)
        self.cursor.execute("""INSERT INTO btc_history VALUES (?, ?)""", (price, milliseconds()))


if __name__ == '__main__':
    milliseconds = lambda: int(time() * 1000)
    print(milliseconds())
