import multiprocessing, time
import psycopg2
import psycopg2.extras

def sum(begin, end, queue):
    result = 0
    for i in range(begin, end):
        result += i
    queue.put(result)

def main():
    connect = psycopg2.connect(host='127.0.0.1', port=5432, database='test_db', user='postgres', password='Helen77')
    start = time.clock()

    queue1 = multiprocessing.Queue()
    queue2 = multiprocessing.Queue()
    queue3 = multiprocessing.Queue()
    queue4 = multiprocessing.Queue()
    queue5 = multiprocessing.Queue()
    queue6 = multiprocessing.Queue()
    queue7 = multiprocessing.Queue()
    queue8 = multiprocessing.Queue()
    queue9 = multiprocessing.Queue()
    queue10 = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=sum, args=(1, 10000000, queue1))
    p2 = multiprocessing.Process(target=sum, args=(10000000, 10000000, queue2))
    p3 = multiprocessing.Process(target=sum, args=(10000000, 10000000, queue3))
    p4 = multiprocessing.Process(target=sum, args=(10000000, 10000000, queue4))
    p5 = multiprocessing.Process(target=sum, args=(10000000, 10000000, queue5))
    p6 = multiprocessing.Process(target=sum, args=(10000000, 10000000, queue6))
    p7 = multiprocessing.Process(target=sum, args=(10000000, 10000000, queue7))
    p8 = multiprocessing.Process(target=sum, args=(10000000, 10000000, queue8))
    p9 = multiprocessing.Process(target=sum, args=(10000000, 10000000, queue9))
    p10 = multiprocessing.Process(target=sum, args=(10000000, 100000001, queue10))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()

    total = queue1.get() + queue2.get() + queue3.get() + queue4.get() + queue5.get() + queue6.get() + queue7.get() + queue8.get() + queue9.get() + queue10.get()
    print(total)
    end = time.clock()
    result = end - start
    sql = ("insert into multiprocessing_time(Number, Time) values (%d, %f)" % (10, result))
    cursore = connect.cursor()
    cursore.execute(sql)
    connect.commit()
    connect.close()
    print('time - %f' % result)

if __name__ == '__main__':
    main()
