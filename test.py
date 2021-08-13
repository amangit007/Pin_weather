import sqlite3
conn =sqlite3.connect('weather.db')
conn.execute('insert into city (name) values ("kalka")')
conn.commit()
result=conn.execute('SELECT * FROM city')
for i in result:
    print(i)