import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3 as sql # sqlite3 is built into Python

d = pd.read_csv('/Users/aitorcalero/Downloads/data.csv')
print(type(d))
print(d.columns)

print(d['Name']+' '+d['Release Clause'])

print(d['Age'].mean())


con = sql.connect("/Users/aitorcalero/Downloads/example_1.db")
pd_sql.to_sql(d,'data',con) # write to DB as table named "data"
con.close()