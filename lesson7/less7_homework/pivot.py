import psycopg2.extras
import matplotlib.pyplot as plt

connect = psycopg2.connect(host='127.0.0.1', port=5432, database='test_db', user='postgres', password='Helen77')

pivot1 = []
pivot2 = []
sql = "SELECT number, time FROM multiprocessing_time ORDER BY number"
cursore = connect.cursor()
cursore.execute(sql)

sql2 = "SELECT number, time FROM mtp_pool ORDER BY number"
cursore2 = connect.cursor()
cursore2.execute(sql2)

for row in cursore:
    pivot1.append(row)

for row in cursore2:
    pivot2.append(row)
connect.close()

print(pivot1)
print(pivot2)
x1 = [x[0] for x in pivot1]
y1 = [x[1] for x in pivot1]
x2 = [x[0] for x in pivot2]
y2 = [x[1] for x in pivot2]

line_up, = plt.plot(x1, y1, label='multiprocessing')
line_down, = plt.plot(x2, y2, label='multiprocessing pool')
plt.xlabel('number')
plt.ylabel('time, c')
plt.legend(handles=[line_up, line_down])
plt.show()
