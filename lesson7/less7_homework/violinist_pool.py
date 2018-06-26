import multiprocessing, time
from multiprocessing import current_process

def play_violin(violin, bow):
    name = current_process().name
    time.sleep(2)
    res = 'Voilinist' + name.replace('SpawnPoolWorker-','') +' plays the ' + violin + ' and ' + bow
    return res


def main():
    start = time.clock()
    violins = ['violin1', 'violin2', 'violin3']
    bows = ['bow1', 'bow2', 'bow3']

    pool = multiprocessing.Pool(6)
    i = 0
    while i < 6:
        res = pool.starmap(play_violin, zip(violins, bows))
        for index in range(len(res)):
            print(res[index])
        i += 1

    end = time.clock()
    result_time = end - start
    print('time is %f' % result_time)

if __name__ == '__main__':
    main()