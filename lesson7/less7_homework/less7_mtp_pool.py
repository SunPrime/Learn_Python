import multiprocessing, time
import psycopg2
import psycopg2.extras

def sum(begin, end):
    result = 0
    for i in range(begin, end):
        result += i
    return result

def main():
    connect = psycopg2.connect(host='127.0.0.1', port=5432, database='test_db', user='postgres', password='Helen77')
    start = time.clock()

    number = 100000000
    part = int(number/10)
    a = [1, part, part*2, part*3, part*4, part*5, part*6, part*7, part*8, part*9]
    b = [part, part*2, part*3, part*4, part*5, part*6, part*7, part*8, part*9, number+1]
    pool = multiprocessing.Pool(10)
    total = pool.starmap(sum, zip(a, b))
    res = 0
    for index in range(len(total)):
         res += total[index]

    print(res)
    end = time.clock()
    result = end - start
    sql = ("insert into mtp_pool(Number, Time) values (%d, %f)" % (10, result))
    cursore = connect.cursor()
    cursore.execute(sql)
    connect.commit()
    connect.close()
    print('time - %f' % result)

if __name__ == '__main__':
    main()