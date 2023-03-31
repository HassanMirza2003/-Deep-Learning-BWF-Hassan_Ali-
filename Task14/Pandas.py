import pandas as pd
import sqlite3 as sq
import sqlalchemy as sqla

data = pd.read_csv('Social_Network_Ads.csv')
print(data)

data1 = pd.read_json("Jsonfile1.Json")
print(data1)

data2 = pd.read_excel("ExcelFile.xlsx")
print(data2)

query = """
CREATE TABLE test (
    a VARCHAR(20),
    b VARCHAR(20),
    c REAL,
    d INTEGER
);"""
con = sq.connect('mydata.sqlite')
con.execute(query)
con.commit()

data4 = [('Atlanta', 'Georgia', 1.25, 6),         ('Tallahassee', 'Florida', 2.6, 3),         ('Sacramento', 'California', 1.7, 5)]

stmt = "INSERT INTO test VALUES (?, ?, ?, ?)"
con.executemany(stmt, data4)
con.commit()

cursor = con.execute('SELECT * FROM test')
rows = cursor.fetchall()
print(rows)

