import psycopg2
import psycopg2.extras

connect = psycopg2.connect(host='127.0.0.1', port = 5432, database = 'test_db', user = 'postgres', password ='Helen77')
"""
sql = "insert into clients(name, address) values ('Ivanov', 'Kiev')"
cursore = connect.cursor()
cursore.execute(sql)
connect.commit()
connect.close()

sql = "SELECT * FROM Clients"
cursore = connect.cursor()
cursore.execute(sql)
for row in cursore:
    print(str(row[0]) + ' ' + row[1] + ' ' + row[2])
connect.close()
"""
sql = "SELECT * FROM Clients"
cursore = connect.cursor(cursor_factory = psycopg2.extras.DictCursor)
cursore.execute(sql)
for row in cursore:
    print(str(row['id']) + ' ' + row['name'] + ' ' + row['address'])
connect.close()