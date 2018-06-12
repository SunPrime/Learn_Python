import psycopg2.extras
import matplotlib.pyplot as plt

connect = psycopg2.connect(host='127.0.0.1', port=5432, database='test_db', user='postgres', password='Helen77')

pivot = []
sql = "SELECT number, time FROM multiprocessing_time ORDER BY number"
cursore = connect.cursor()
cursore.execute(sql)
for row in cursore:
    pivot.append(row)
connect.close()
print(pivot)
xs = [x[0] for x in pivot]
ys = [x[1] for x in pivot]
plt.plot(xs, ys)
plt.xlabel('number')
plt.ylabel('time')
plt.show()
